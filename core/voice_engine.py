import asyncio
import subprocess
import json
from pathlib import Path
from typing import Tuple, Dict, Any, List
import edge_tts
from config import DEFAULT_VOICE

class VoiceEngine:
    def __init__(self, voice: str = DEFAULT_VOICE):
        self.voice = voice

    async def _synthesize(self, text: str, output_audio: Path, rate: str = "+5%", pitch: str = "+0Hz") -> List[Dict[str, Any]]:
        """
        Sintetiza la voz neuronal usando Edge-TTS y captura los eventos de sincronización de palabras.
        """
        output_audio.parent.mkdir(parents=True, exist_ok=True)
        communicate = edge_tts.Communicate(text, self.voice, rate=rate, pitch=pitch)
        
        word_boundaries = []
        with open(output_audio, "wb") as f:
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    f.write(chunk["data"])
                elif chunk["type"] == "WordBoundary":
                    # Offset y Duration vienen en ticks de 100ns (1 segundo = 10,000,000 ticks)
                    offset_sec = chunk["offset"] / 10_000_000.0
                    duration_sec = chunk["duration"] / 10_000_000.0
                    word_boundaries.append({
                        "word": chunk["text"],
                        "start": offset_sec,
                        "end": offset_sec + duration_sec
                    })
                    
        return word_boundaries

    def generate_voice(self, text: str, output_audio: Path, rate: str = "+5%", max_retries: int = 3) -> Tuple[float, List[Dict[str, Any]]]:
        """
        Genera el audio en MP3 con reintentos automáticos ante cortes momentáneos de red.
        """
        import time
        word_timings = []
        
        for attempt in range(1, max_retries + 1):
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    word_timings = loop.run_until_complete(self._synthesize(text, output_audio, rate=rate))
                finally:
                    loop.close()

                if output_audio.exists() and output_audio.stat().st_size > 100:
                    break
            except Exception as e:
                print(f"[VoiceEngine] Intento {attempt}/{max_retries} falló: {e}. Reintentando...", flush=True)
                time.sleep(1.5)
                if attempt == max_retries:
                    raise e

        # Medir duración real con ffprobe
        duration = self.get_audio_duration(output_audio)
        
        # Si edge-tts no emitió eventos WordBoundary, generar estimación proporcional exacta
        if not word_timings and duration > 0:
            words = text.split()
            if words:
                time_per_word = duration / len(words)
                for i, w in enumerate(words):
                    word_timings.append({
                        "word": w,
                        "start": i * time_per_word,
                        "end": (i + 1) * time_per_word
                    })

        return duration, word_timings

    @staticmethod
    def get_audio_duration(audio_path: Path) -> float:
        """Obtiene la duración exacta de un archivo de audio usando ffprobe."""
        cmd = [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(audio_path)
        ]
        try:
            res = subprocess.run(cmd, capture_output=True, text=True)
            return float(res.stdout.strip())
        except Exception:
            return 5.0

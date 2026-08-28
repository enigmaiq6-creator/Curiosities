import os
import json
import base64
import asyncio
import subprocess
import urllib.request
import urllib.error
from pathlib import Path
from typing import Tuple, Dict, Any, List
import edge_tts
from config import DEFAULT_VOICE, GOOGLE_TTS_API_KEY, VOICES

class VoiceEngine:
    """
    Motor de Voz Ultra-Realista de Grado Documental:
    - Primario: Google Cloud Text-to-Speech (Studio Ultra-HD 24kHz / Neural2).
    - Respaldo: Microsoft Edge-TTS Neuronal.
    - Sincronización acústica milimétrica de subtítulos con ffprobe.
    """

    def __init__(self, voice: str = DEFAULT_VOICE, api_key: str = GOOGLE_TTS_API_KEY):
        self.voice = VOICES.get(voice, voice)
        self.api_key = api_key or os.getenv("GOOGLE_TTS_API_KEY", "")

    def _synthesize_google(self, text: str, output_audio: Path) -> Tuple[float, List[Dict[str, Any]]]:
        """Sintetiza voz documental ultra-realista con Google Cloud TTS REST API."""
        if not self.api_key:
            raise ValueError("No Google Cloud TTS API key configured")

        output_audio.parent.mkdir(parents=True, exist_ok=True)
        url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={self.api_key}"
        
        lang_code = "en-GB" if "en-GB" in self.voice else "en-US"
        voice_name = self.voice if ("Studio" in self.voice or "Neural2" in self.voice) else "en-US-Studio-Q"

        payload = {
            "input": {"text": text},
            "voice": {
                "languageCode": lang_code,
                "name": voice_name
            },
            "audioConfig": {
                "audioEncoding": "MP3",
                "speakingRate": 0.98,
                "pitch": -0.5
            }
        }

        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "User-Agent": "Curiosities-DocVoice/3.0"}
        )

        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            audio_bytes = base64.b64decode(data["audioContent"])
            with open(output_audio, "wb") as f:
                f.write(audio_bytes)

        duration = self.get_audio_duration(output_audio)
        
        words = text.split()
        word_timings = []
        cur_t = 0.0
        total_chars = max(1, sum(len(w) for w in words))
        for w in words:
            w_dur = (len(w) / total_chars) * (duration - 0.08)
            word_timings.append({
                "word": w,
                "start": cur_t,
                "end": cur_t + w_dur
            })
            cur_t += w_dur

        return duration, word_timings

    async def _synthesize_edge(self, text: str, output_audio: Path, rate: str = "+0%", pitch: str = "-1Hz") -> List[Dict[str, Any]]:
        """Sintetiza la voz neuronal usando Edge-TTS."""
        output_audio.parent.mkdir(parents=True, exist_ok=True)
        edge_voice = "en-US-ChristopherNeural" if "Studio" in self.voice else self.voice
        communicate = edge_tts.Communicate(text, edge_voice, rate=rate, pitch=pitch)
        
        word_boundaries = []
        with open(output_audio, "wb") as f:
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    f.write(chunk["data"])
                elif chunk["type"] == "WordBoundary":
                    offset_sec = chunk["offset"] / 10_000_000.0
                    duration_sec = chunk["duration"] / 10_000_000.0
                    word_boundaries.append({
                        "word": chunk["text"],
                        "start": offset_sec,
                        "end": offset_sec + duration_sec
                    })
                    
        return word_boundaries

    def generate_voice(self, text: str, output_audio: Path, rate: str = "+0%", max_retries: int = 3) -> Tuple[float, List[Dict[str, Any]]]:
        """
        Genera el audio con Google Cloud Studio TTS ultra-realista y respaldo Edge-TTS.
        """
        # 1. Intentar Google Cloud TTS Studio
        if self.api_key:
            try:
                duration, word_timings = self._synthesize_google(text, output_audio)
                print(f"[VoiceEngine] [GOOGLE CLOUD STUDIO TTS] Voz '{self.voice}' generada ({duration:.2f}s)", flush=True)
                return duration, word_timings
            except Exception as e:
                print(f"[VoiceEngine] [!] Google Cloud TTS error: {e}. Usando respaldo Edge-TTS...", flush=True)

        # 2. Respaldo Edge-TTS
        import time
        word_timings = []
        for attempt in range(1, max_retries + 1):
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    word_timings = loop.run_until_complete(self._synthesize_edge(text, output_audio, rate=rate))
                finally:
                    loop.close()

                if output_audio.exists() and output_audio.stat().st_size > 100:
                    break
            except Exception as e:
                print(f"[VoiceEngine] Intento Edge-TTS {attempt}/{max_retries} fallo: {e}. Reintentando...", flush=True)
                time.sleep(1.5)
                if attempt == max_retries:
                    raise e

        duration = self.get_audio_duration(output_audio)
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

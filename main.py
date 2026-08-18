import sys
import os
import argparse
from pathlib import Path
from datetime import datetime

# Asegurar codificación UTF-8 en terminal de Windows
try:
    if sys.platform.startswith("win"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
        sys.stderr.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
except Exception:
    pass

from config import (
    TEMP_DIR,
    OUTPUT_DIR,
    MUSIC_DIR,
    VOICES,
    DEFAULT_VOICE,
    DEFAULT_ASPECT
)
from core.script_engine import ScriptEngine
from core.voice_engine import VoiceEngine
from core.subtitle_engine import SubtitleEngine
from core.video_composer import VideoComposer
from core.audio_sfx_engine import generate_cinematic_whoosh, generate_ambient_cinematic_music
from fetchers.media_manager import MediaManager

def generate_curiosity_video(
    script_text: str = None,
    topic: str = "animales",
    aspect_ratio: str = "vertical",
    voice: str = DEFAULT_VOICE,
    output_filename: str = None
) -> Path:
    """
    Ejecuta el pipeline completo de creación de video de curiosidades.
    """
    print("\n=======================================================")
    print("   GENERADOR AUTOMÁTICO DE VIDEOS DE CURIOSIDADES     ")
    print("=======================================================\n")
    print(f"[+] Formato: {aspect_ratio.upper()}")
    print(f"[+] Voz seleccionada: {voice}")

    # 1. Preparar el Guion
    if script_text:
        print("[+] Parseando guion personalizado...")
        scenes = ScriptEngine.parse_curiosity_script(script_text)
    else:
        print(f"[+] Utilizando guion temático: '{topic}'...")
        scenes = ScriptEngine.create_sample_script(topic)

    if not scenes:
        raise ValueError("No se encontraron escenas válidas en el guion.")

    print(f"[+] Total de escenas a procesar: {len(scenes)}")

    # 1. Componentes del motor
    voice_engine = VoiceEngine(voice=voice)
    subtitle_engine = SubtitleEngine(aspect_ratio=aspect_ratio)
    composer = VideoComposer(aspect_ratio=aspect_ratio)
    media_manager = MediaManager(temp_dir=TEMP_DIR)

    scene_audio_files = []
    processed_clip_files = []
    global_time = 0.0

    # 2. Generar Voz y Descargar Videos para cada escena
    total_curiosities = max((len(scenes) + 1) // 2, 1)
    
    for scene in scenes:
        s_id = scene["scene_id"]
        text = scene["text"]
        keywords = scene["keywords"]
        curiosity_num = (s_id + 1) // 2

        print(f"\n--- [Escena {s_id} / Curiosidad #{curiosity_num}] ---")
        print(f"Texto: \"{text}\"")
        print(f"Keywords: {keywords}")

        # Generar Audio
        audio_path = TEMP_DIR / f"scene_{s_id}_voice.mp3"
        duration, word_timings = voice_engine.generate_voice(text, audio_path)
        print(f"[Voz] Duración: {duration:.2f}s | Palabras detectadas: {len(word_timings)}")

        scene["duration"] = duration
        scene["global_start"] = global_time
        scene["word_timings"] = word_timings
        global_time += duration
        scene_audio_files.append(audio_path)

        # Descargar Clip de video multi-fuente con validación estricta de sujeto
        required_subject = scene.get("subject", "")
        raw_clip_path = media_manager.fetch_clip_for_scene(
            s_id, 
            keywords, 
            required_subject=required_subject, 
            target_duration=duration
        )
        if not raw_clip_path or not raw_clip_path.exists():
            raise RuntimeError(f"No se pudo obtener video para la escena {s_id}")

        # Procesar y normalizar clip con FFmpeg a 30 FPS constantes
        normalized_clip_path = TEMP_DIR / f"scene_{s_id}_norm.mp4"
        print(f"[Video] Normalizando y adaptando clip a {duration:.2f}s (CFR 30 FPS)...")
        if not composer.process_scene_clip(
            input_video=raw_clip_path,
            output_clip=normalized_clip_path,
            duration=duration
        ):
            raise RuntimeError(f"Error procesando el clip de la escena {s_id}")

        processed_clip_files.append(normalized_clip_path)

    # 3. Generar Subtítulos Dinámicos (.ass) con Branding Completo
    print("\n[+] Generando subtítulos dinámicos de alto impacto y elementos de marca...")
    ass_path = TEMP_DIR / "subtitles.ass"
    subtitle_engine.create_ass_subtitles(scenes, ass_path, total_video_duration=global_time)

    # 4. Generar Efectos de Sonido SFX Profesionales y Concatenar Audio
    print("\n[+] Generando efectos de sonido (SFX Whoosh) profesionales...")
    sfx_whoosh_path = generate_cinematic_whoosh(TEMP_DIR / "sfx_whoosh.wav")
    
    print("[+] Uniendo pistas de audio con transiciones sonoras SFX...")
    combined_audio = TEMP_DIR / "combined_voice.mp3"
    scene_durations = [s["duration"] for s in scenes]
    composer.concatenate_audio_tracks_with_sfx(
        audio_paths=scene_audio_files,
        scene_durations=scene_durations,
        sfx_whoosh_path=sfx_whoosh_path,
        output_path=combined_audio
    )

    print("[+] Uniendo clips de video (CFR 30 FPS)...")
    combined_video = TEMP_DIR / "combined_video.mp4"
    composer.concatenate_video_clips(processed_clip_files, combined_video)

    # 5. Render Final con Banda Sonora Cinemática y Audio Ducking
    if not output_filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"curiosidades_{topic}_{aspect_ratio}_{timestamp}.mp4"

    final_output = OUTPUT_DIR / output_filename

    # Buscar música personalizada en MUSIC_DIR o generar banda sonora cinemática atmosférica
    bg_music = None
    music_files = list(MUSIC_DIR.glob("*.mp3")) + list(MUSIC_DIR.glob("*.wav"))
    if music_files:
        bg_music = music_files[0]
        print(f"[+] Usando música de fondo personalizada: {bg_music.name}")
    else:
        print("[+] Generando banda sonora ambiental cinemática...")
        bg_music = generate_ambient_cinematic_music(
            output_wav=TEMP_DIR / "ambient_soundtrack.wav",
            duration=global_time + 8.0
        )

    print(f"\n[+] Renderizando video final (Audio Pro + SFX + Viral Minimalist) en: {final_output}...")
    success = composer.build_final_video(
        video_path=combined_video,
        voice_audio_path=combined_audio,
        ass_subtitles_path=ass_path,
        output_final_path=final_output,
        total_duration=global_time,
        bg_music_path=bg_music
    )

    if success:
        print("\n=======================================================")
        print("   ¡VIDEO GENERADO CON ÉXITO! 🎉                      ")
        print(f"   Ruta: {final_output.resolve()}")
        print(f"   Duración aproximada: {global_time:.1f} segundos")
        print("=======================================================\n")
        return final_output
    else:
        raise RuntimeError("Hubo un fallo durante el renderizado final de FFmpeg.")

def main():
    parser = argparse.ArgumentParser(description="Generador de Videos de Curiosidades Multi-Fuente")
    parser.add_argument("--topic", type=str, default="komodo", help="Tema del video (ej. komodo, animales, espacio, oceano, humano)")
    parser.add_argument("--script", type=str, default=None, help="Texto del guion personalizado (cada línea es una escena)")
    parser.add_argument("--aspect", type=str, default="vertical", choices=["vertical", "horizontal"], help="Formato de video")
    parser.add_argument("--voice", type=str, default=DEFAULT_VOICE, help="Voz de Edge-TTS a utilizar")
    parser.add_argument("--output", type=str, default=None, help="Nombre del archivo de salida")

    args = parser.parse_args()

    generate_curiosity_video(
        script_text=args.script,
        topic=args.topic,
        aspect_ratio=args.aspect,
        voice=args.voice,
        output_filename=args.output
    )

if __name__ == "__main__":
    main()

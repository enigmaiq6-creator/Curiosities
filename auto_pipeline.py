import os
import random
import argparse
from pathlib import Path
from datetime import datetime

from main import generate_curiosity_video
from uploader.facebook_uploader import upload_to_facebook_reels
from config import OUTPUT_DIR, VOICES

TOPICS_CATALOG = [
    # Inglés
    {"topic": "egypt", "voice": "en-US-ChristopherNeural", "lang": "en", "title": "5 Mind-Blowing Secrets of Ancient Egypt! 🏺✨"},
    {"topic": "ocean", "voice": "en-US-ChristopherNeural", "lang": "en", "title": "5 Terrifying Mysteries of the Deep Ocean! 🌊🦈"},
    # Español
    {"topic": "humano", "voice": "es-MX-JorgeNeural", "lang": "es", "title": "¡5 Datos Increíbles del Cuerpo Humano que NO Sabías! 🧬⚡"},
    {"topic": "espacio", "voice": "es-MX-JorgeNeural", "lang": "es", "title": "¡5 Misterios Asombrosos del Espacio Profundo! 🌌🚀"},
    {"topic": "komodo", "voice": "es-MX-JorgeNeural", "lang": "es", "title": "¡5 Curiosidades Extremas del Dragón de Komodo! 🦎🔥"},
    {"topic": "animales", "voice": "es-MX-JorgeNeural", "lang": "es", "title": "¡5 Animales con Superpoderes Reales en la Naturaleza! 🦅🌿"}
]

HASHTAGS_EN = "#curiosities #mindblowing #facts #didyouknow #science #education #shorts #reels #viral #explore #fyp #ancient #ocean"
HASHTAGS_ES = "#curiosidades #datoscuriosos #sabiasque #ciencia #aprender #shorts #reels #viral #parati #tendencias #interesante #datos"

def run_automated_pipeline(topic_key: str = None):
    """
    Ejecuta el ciclo completo de automatización:
    1. Selecciona o recibe un tema.
    2. Renderiza el video con voz neuronal, 4K clips, SFX y CTA.
    3. Genera títulos y descripción viral.
    4. Sube a Facebook Reels de forma desatendida.
    """
    print("\n" + "="*60)
    print("   🤖 INICIANDO PIPELINE AUTOMÁTICO DE CURIOSIDADES   ")
    print("="*60 + "\n")

    # 1. Selección de Tema
    if topic_key:
        selected = next((item for item in TOPICS_CATALOG if item["topic"] == topic_key), None)
        if not selected:
            selected = {"topic": topic_key, "voice": "en-US-ChristopherNeural", "lang": "en", "title": f"5 Amazing Facts About {topic_key.title()}!"}
    else:
        selected = random.choice(TOPICS_CATALOG)

    topic = selected["topic"]
    voice = selected["voice"]
    lang = selected["lang"]
    base_title = selected["title"]

    print(f"[Pipeline] [+] Tema seleccionado: '{topic.upper()}' (Idioma: {lang.upper()})")
    print(f"[Pipeline] [+] Voz: {voice}")

    # 2. Renderizado del Video
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"curiosities_{topic}_vertical_{timestamp}.mp4"

    video_path = generate_curiosity_video(
        topic=topic,
        voice=voice,
        aspect_ratio="vertical",
        output_filename=output_filename
    )

    if not video_path or not video_path.exists():
        raise RuntimeError("[Pipeline] Error: El video no fue generado correctamente.")

    # 3. Generación de Metadatos y Descripción Viral
    hashtags = HASHTAGS_EN if lang == "en" else HASHTAGS_ES
    if lang == "en":
        full_description = f"{base_title}\n\nDid you know these fascinating facts? Drop your thoughts below and follow for daily curiosities!\n\n{hashtags}"
    else:
        full_description = f"{base_title}\n\n¿Cuál de estos datos te sorprendió más? ¡Comenta abajo y síguenos para más curiosidades diarias!\n\n{hashtags}"

    meta_file = OUTPUT_DIR / f"metadata_{topic}_{timestamp}.txt"
    with open(meta_file, "w", encoding="utf-8") as f:
        f.write(full_description)
    print(f"[Pipeline] [+] Metadatos guardados en: {meta_file.name}")

    # 4. Subida Automática a Redes Sociales (Facebook Reels)
    print("\n[Pipeline] Intentando subida automática a Facebook Reels...")
    upload_result = upload_to_facebook_reels(
        video_path=video_path,
        description=full_description
    )

    print("\n" + "="*60)
    print("   🎉 PIPELINE COMPLETADO EXITOSAMENTE              ")
    print(f"   Video: {video_path.name}")
    print(f"   Estado de Subida: {upload_result.get('status', 'unknown')}")
    print("="*60 + "\n")

    return video_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline Automático de Videos")
    parser.add_argument("--topic", type=str, default=None, help="Tema específico o aleatorio si se omite")
    args = parser.parse_args()
    
    run_automated_pipeline(topic_key=args.topic)

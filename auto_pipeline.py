import os
import random
import argparse
from pathlib import Path
from datetime import datetime

from main import generate_curiosity_video
from uploader.facebook_uploader import upload_to_facebook_reels
from config import OUTPUT_DIR

# Catálogo 100% en INGLÉS con títulos virales optimizados para engagement
TOPICS_CATALOG_EN = [
    {
        "topic": "egypt",
        "voice": "en-US-ChristopherNeural",
        "title": "5 Mind-Blowing Secrets of Ancient Egypt & The Pyramids! 🏺👑",
        "intro_tag": "Ancient Egypt and the Great Pyramids"
    },
    {
        "topic": "ocean",
        "voice": "en-US-ChristopherNeural",
        "title": "5 Terrifying Mysteries of the Deep Abyss! 🌊🦈",
        "intro_tag": "the Mysterious Deep Ocean"
    },
    {
        "topic": "space",
        "voice": "en-US-ChristopherNeural",
        "title": "5 Insane Mysteries of Deep Space & The Universe! 🌌🚀",
        "intro_tag": "Deep Space and the Universe"
    },
    {
        "topic": "human",
        "voice": "en-US-ChristopherNeural",
        "title": "5 Unbelievable Superpowers of the Human Body! 🧬⚡",
        "intro_tag": "the Human Body"
    },
    {
        "topic": "animals",
        "voice": "en-US-ChristopherNeural",
        "title": "5 Animals with Real Superpowers in Nature! 🦅🦎",
        "intro_tag": "Animals with Real Superpowers"
    }
]

HASHTAGS_EN = "#curiosities #mindblowing #facts #didyouknow #science #education #shorts #reels #viral #explore #fyp #amazingfacts #history #space #ocean"

def run_automated_pipeline(topic_key: str = None):
    """
    Ejecuta el ciclo de automatización 100% EN INGLÉS:
    1. Selecciona un tema en inglés.
    2. Renderiza el video con voz neuronal en inglés, 4K clips, SFX Whoosh y CTA en inglés.
    3. Genera títulos y descripción viral en inglés.
    4. Sube a Facebook Reels con metadatos en inglés.
    """
    print("\n" + "="*60)
    print("   🤖 INICIANDO PIPELINE AUTOMÁTICO DE CURIOSIDADES (100% ENGLISH)   ")
    print("="*60 + "\n")

    # 1. Selección de Tema en Inglés
    if topic_key:
        selected = next((item for item in TOPICS_CATALOG_EN if item["topic"] == topic_key), None)
        if not selected:
            selected = {
                "topic": topic_key,
                "voice": "en-US-ChristopherNeural",
                "title": f"5 Amazing Facts About {topic_key.title()}! 🌟",
                "intro_tag": topic_key.title()
            }
    else:
        selected = random.choice(TOPICS_CATALOG_EN)

    topic = selected["topic"]
    voice = selected["voice"]
    base_title = selected["title"]

    print(f"[Pipeline] [+] Selected Topic: '{topic.upper()}' (Language: ENGLISH)")
    print(f"[Pipeline] [+] Voice: {voice}")

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
        raise RuntimeError("[Pipeline] Error: Video was not generated successfully.")

    # 3. Generación de Metadatos y Descripción Viral 100% en Inglés
    full_description = (
        f"{base_title}\n\n"
        f"Did you know these fascinating facts? Which one surprised you the most?\n"
        f"Drop your thoughts in the comments, hit LIKE, and FOLLOW for daily mind-blowing curiosities! 🔔✨\n\n"
        f"{HASHTAGS_EN}"
    )

    meta_file = OUTPUT_DIR / f"metadata_{topic}_{timestamp}.txt"
    with open(meta_file, "w", encoding="utf-8") as f:
        f.write(full_description)
    print(f"[Pipeline] [+] English metadata saved to: {meta_file.name}")

    # 4. Subida Automática a Redes Sociales (Facebook Reels)
    print("\n[Pipeline] Uploading Reel to Facebook with English metadata...")
    upload_result = upload_to_facebook_reels(
        video_path=video_path,
        description=full_description
    )

    print("\n" + "="*60)
    print("   🎉 PIPELINE COMPLETED SUCCESSFULLY               ")
    print(f"   Video File: {video_path.name}")
    print(f"   Upload Status: {upload_result.get('status', 'unknown')}")
    print("="*60 + "\n")

    return video_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated English Curiosity Video Pipeline")
    parser.add_argument("--topic", type=str, default=None, help="Specific topic or random if omitted")
    args = parser.parse_args()
    
    run_automated_pipeline(topic_key=args.topic)

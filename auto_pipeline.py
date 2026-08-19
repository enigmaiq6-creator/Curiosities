import os
import argparse
from pathlib import Path
from datetime import datetime

from main import generate_curiosity_video
from uploader.facebook_uploader import upload_to_facebook_reels
from core.topic_catalog import TOPICS_DB
from core.history_manager import HistoryManager
from config import OUTPUT_DIR

HASHTAGS_EN = "#curiosities #mindblowing #facts #didyouknow #science #education #shorts #reels #viral #explore #fyp #amazingfacts #history #space #ocean"

def run_automated_pipeline(topic_key: str = None):
    """
    Ejecuta el ciclo de automatización 100% EN INGLÉS con garantía anti-repetición:
    1. Consulta el historial persistente (history.json) y selecciona un tema NUNCA usado.
    2. Renderiza el video con voz neuronal en inglés, 4K clips, SFX Whoosh y CTA en inglés.
    3. Genera títulos y descripción viral en inglés.
    4. Sube a Facebook Reels con metadatos en inglés.
    5. Registra el tema en history.json de forma permanente.
    """
    print("\n" + "="*60)
    print("   🤖 INICIANDO PIPELINE AUTOMÁTICO DE CURIOSIDADES (100% ENGLISH)   ")
    print("="*60 + "\n")

    available_topic_keys = list(TOPICS_DB.keys())

    # 1. Selección de Tema con Garantía Anti-Repetición
    if topic_key:
        topic = topic_key.lower().strip()
    else:
        topic = HistoryManager.get_next_unique_topic(available_topic_keys)

    topic_data = TOPICS_DB.get(topic, TOPICS_DB.get("egypt"))
    voice = "en-US-ChristopherNeural"
    base_title = topic_data.get("title", f"5 Amazing Facts About {topic.title()}!")

    print(f"[Pipeline] [+] Selected Unseen Topic: '{topic.upper()}' (Language: ENGLISH)")
    print(f"[Pipeline] [+] Voice: {voice}")
    print(f"[Pipeline] [+] Title: {base_title}")

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

    post_id = upload_result.get("result", {}).get("post_id") or upload_result.get("post_id")

    # 5. Registro Permanente en History Manager (Anti-Repetición)
    HistoryManager.record_published(
        topic_key=topic,
        title=base_title,
        post_id=post_id
    )

    print("\n" + "="*60)
    print("   🎉 PIPELINE COMPLETED SUCCESSFULLY               ")
    print(f"   Topic: {topic}")
    print(f"   Video File: {video_path.name}")
    print(f"   Upload Status: {upload_result.get('status', 'unknown')}")
    print("="*60 + "\n")

    return video_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated English Curiosity Video Pipeline")
    parser.add_argument("--topic", type=str, default=None, help="Specific topic or auto-select from unseen history")
    args = parser.parse_args()
    
    run_automated_pipeline(topic_key=args.topic)

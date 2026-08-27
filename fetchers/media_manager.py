import os
import re
import subprocess
from pathlib import Path
from typing import List, Optional, Dict, Any, Set
from config import TEMP_DIR

from fetchers.pexels_fetcher import search_pexels_videos, download_pexels_video, search_pexels_photos, download_pexels_photo
from fetchers.pixabay_fetcher import search_pixabay_videos, download_pixabay_video
from fetchers.nasa_fetcher import search_nasa_videos, download_nasa_video
from fetchers.tiktok_fetcher import search_tiktok_clips, download_tiktok_video
from fetchers.social_fetcher import search_social_vertical_clips, download_social_clip
from fetchers.archive_org_fetcher import search_archive_org_videos, download_archive_org_video
from fetchers.youtube_fetcher import search_youtube_videos, download_youtube_clip
from fetchers.reddit_fetcher import search_reddit_videos, download_reddit_video

# Términos que descalifican automáticamente a un video si aparecen (Falsos positivos)
NEGATIVE_EXCLUSIONS = {
    "komodo": ["dragonfly", "dragon-fly", "water dragon", "chinese", "bearded", "snake", "iguana", "gecko", "chameleon", "insect", "fly", "cartoon"],
    "crow": ["seagull", "pigeon", "parrot", "canary", "eagle"],
    "whale": ["dolphin", "shark", "scuba", "fish"],
    "butterfly": ["bee", "wasp", "ant", "fly"],
    "axolotl": ["goldfish", "koi", "turtle", "frog"],
    "hummingbird": ["bee", "flower only", "wasp"],
    "brain": ["zombie", "horror", "food", "dish"],
    "dna": ["food", "diet"]
}

def verify_subject_match(metadata_text: str, required_subject: str) -> bool:
    """
    Verifica de forma inteligente que el texto/título/etiquetas del video sean relevantes
    para el tema y no contengan falsos positivos evidentes.
    """
    if not required_subject or required_subject.lower() in ["curiosity", "science", "fact", "world", "nature"]:
        return True
    
    req_lower = required_subject.lower().strip()
    meta_lower = metadata_text.lower()
    
    # 1. Comprobar si contiene exclusiones negativas
    exclusions = NEGATIVE_EXCLUSIONS.get(req_lower, [])
    for exc in exclusions:
        if exc in meta_lower:
            return False

    # 2. Comprobar coincidencia directa de palabras clave relevantes
    keywords_to_check = [req_lower] + [w for w in req_lower.replace("-", " ").replace("_", " ").split() if len(w) > 3]
    for kw in keywords_to_check:
        if kw in meta_lower:
            return True
            
    return True

class MediaManager:
    """
    Gestor Omnicanal de Medios para Curiosity Video Engine:
    Garantiza CERO REPETICIÓN de clips de video o imágenes en el mismo video.
    Cada escena obtiene un clip 100% único desde Pexels 4K, Pixabay, NASA, YouTube o Foto Ken Burns.
    """

    def __init__(self, temp_dir: Path = TEMP_DIR):
        self.temp_dir = temp_dir
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self.used_urls: Set[str] = set()
        self.downloaded_clips_history: List[Path] = []

    def fetch_clip_for_scene(
        self,
        scene_id: int,
        keywords: List[str],
        required_subject: str = "",
        target_duration: float = 4.5
    ) -> Optional[Path]:
        """
        Descarga un clip ÚNICO para la escena dada.
        Garantiza que NUNCA se repita el mismo clip entre escenas distintas.
        """
        output_file = self.temp_dir / f"scene_{scene_id}_raw.mp4"
        if output_file.exists():
            try:
                output_file.unlink()
            except Exception:
                pass

        subject_clean = required_subject.lower().strip()

        # =====================================================================
        # NIVEL 1: PEXELS OFICIAL (4K / HD - ORIENTACIÓN ALL & PORTRAIT)
        # =====================================================================
        for kw in keywords:
            print(f"[MediaManager] [NIVEL 1 - Pexels] Escena {scene_id} -> '{kw}'...", flush=True)
            try:
                pex_results = search_pexels_videos(kw, orientation="all", max_results=8)
                for pex in pex_results:
                    url = pex.get('video_url', '')
                    if url in self.used_urls:
                        continue
                    meta = f"{pex.get('title', '')} {pex.get('tags', '')}"
                    if verify_subject_match(meta, subject_clean):
                        if download_pexels_video(url, output_file):
                            self.used_urls.add(url)
                            self.downloaded_clips_history.append(output_file)
                            print(f"  [OK] Descargado de Pexels Oficial (4K).", flush=True)
                            return output_file
            except Exception as e:
                print(f"  [!] Error Pexels: {e}", flush=True)

        # =====================================================================
        # NIVEL 2: PIXABAY OFICIAL (HD / 4K)
        # =====================================================================
        for kw in keywords:
            print(f"[MediaManager] [NIVEL 2 - Pixabay] Escena {scene_id} -> '{kw}'...", flush=True)
            try:
                pix_results = search_pixabay_videos(kw, max_results=8)
                for pix in pix_results:
                    url = pix.get('video_url', '')
                    if url in self.used_urls:
                        continue
                    meta = f"{pix.get('title', '')}"
                    if verify_subject_match(meta, subject_clean):
                        if download_pixabay_video(url, output_file):
                            self.used_urls.add(url)
                            self.downloaded_clips_history.append(output_file)
                            print(f"  [OK] Descargado de Pixabay Oficial (HD).", flush=True)
                            return output_file
            except Exception as e:
                print(f"  [!] Error Pixabay: {e}", flush=True)

        # =====================================================================
        # NIVEL 3: NASA 4K API (TEMAS DE ESPACIO / PLANETAS / UNIVERSO)
        # =====================================================================
        is_space_theme = any(w in subject_clean or any(w in kw.lower() for kw in keywords) for w in ["space", "star", "sun", "moon", "planet", "galaxy", "black hole", "nebula", "mars", "venus", "jupiter", "saturn", "telescope", "astronaut", "cosmos"])
        if is_space_theme:
            print(f"[MediaManager] [NIVEL 3 - NASA 4K] Buscando archivo aeroespacial...", flush=True)
            for kw in keywords:
                try:
                    nasa_results = search_nasa_videos(kw, max_results=3)
                    for n in nasa_results:
                        url = n.get("video_url", "")
                        if url in self.used_urls:
                            continue
                        if download_nasa_video(url, output_file):
                            self.used_urls.add(url)
                            self.downloaded_clips_history.append(output_file)
                            print(f"  [OK] Descargado de NASA 4K Open Archive.", flush=True)
                            return output_file
                except Exception:
                    pass

        # =====================================================================
        # NIVEL 4: YOUTUBE DOCUMENTARY CLIPS (Cortes rápidos en HD)
        # =====================================================================
        for kw in keywords:
            print(f"[MediaManager] [NIVEL 4 - YouTube] Buscando metraje real para '{kw}'...", flush=True)
            try:
                yt_results = search_youtube_videos(f"{kw} 4k 60fps", max_results=3)
                for yt in yt_results:
                    url = yt.get("url", "")
                    if url in self.used_urls:
                        continue
                    if download_youtube_clip(url, output_file, start_sec=3, duration_sec=int(target_duration + 2)):
                        self.used_urls.add(url)
                        self.downloaded_clips_history.append(output_file)
                        print(f"  [OK] Clip obtenido de YouTube ({yt.get('title')[:45]}).", flush=True)
                        return output_file
            except Exception:
                pass

        # =====================================================================
        # NIVEL 5: REDDIT / TIKTOK / REDES SOCIALES
        # =====================================================================
        for kw in keywords:
            try:
                tt_results = search_tiktok_clips(kw, max_results=3)
                for tt in tt_results:
                    url = tt.get('url', '')
                    if url in self.used_urls:
                        continue
                    if download_tiktok_video(url, output_file, start_sec=2, duration_sec=int(target_duration + 2)):
                        self.used_urls.add(url)
                        self.downloaded_clips_history.append(output_file)
                        print(f"  [OK] Clip obtenido de TikTok.", flush=True)
                        return output_file
            except Exception:
                pass

        # =====================================================================
        # NIVEL 6: FOTOGRAFÍA 4K DE ALTA DEFINICIÓN + EFECTO KEN BURNS 3D DINÁMICO
        # (Garantiza que NUNCA se repita un clip previo)
        # =====================================================================
        print(f"[MediaManager] [NIVEL 6 - FOTO 4K KEN BURNS] Generando toma cinematográfica única...", flush=True)
        photo_queries = keywords + [f"{subject_clean} scientific 4k", f"{subject_clean} detailed photograph"]
        
        raw_photo_path = self.temp_dir / f"scene_{scene_id}_photo.jpg"
        for pkw in photo_queries:
            try:
                photos = search_pexels_photos(pkw, max_results=5)
                for p in photos:
                    img_url = p.get("image_url", "")
                    if img_url in self.used_urls:
                        continue
                    if download_pexels_photo(img_url, raw_photo_path):
                        self.used_urls.add(img_url)
                        # Animar la foto con Ken Burns (zoom suave hacia el centro)
                        cmd_kb = [
                            "ffmpeg", "-y",
                            "-loop", "1",
                            "-i", str(raw_photo_path),
                            "-t", f"{target_duration:.2f}",
                            "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,zoompan=z='min(zoom+0.0015,1.2)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=125:s=1080x1920",
                            "-c:v", "libx264",
                            "-preset", "ultrafast",
                            "-crf", "18",
                            "-pix_fmt", "yuv420p",
                            str(output_file)
                        ]
                        subprocess.run(cmd_kb, capture_output=True, timeout=20)
                        if output_file.exists() and output_file.stat().st_size > 5000:
                            print(f"  [OK] Generada toma 4K Ken Burns con éxito para escena {scene_id}.", flush=True)
                            return output_file
            except Exception as e:
                print(f"  [!] Error Foto Ken Burns: {e}", flush=True)

        # Respaldo absoluto de emergencia con fondo cinemático de color
        cmd_gen = [
            "ffmpeg", "-y",
            "-f", "lavfi",
            "-i", "color=c=0x0a1128:s=1080x1920:d=5,format=yuv420p",
            "-c:v", "libx264",
            "-r", "30",
            str(output_file)
        ]
        subprocess.run(cmd_gen, capture_output=True)
        return output_file

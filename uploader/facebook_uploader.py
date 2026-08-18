import os
import time
import requests
from pathlib import Path
from typing import Optional, Dict, Any

class FacebookReelsUploader:
    def __init__(self, page_id: Optional[str] = None, access_token: Optional[str] = None):
        """
        Inicializa el publicador oficial de Facebook Reels vía Meta Graph API.
        Lee las credenciales de variables de entorno si no se pasan explícitamente.
        """
        self.page_id = page_id or os.environ.get("FACEBOOK_PAGE_ID", "")
        self.access_token = access_token or os.environ.get("FACEBOOK_ACCESS_TOKEN", "")
        self.graph_version = "v19.0"

    def upload_reel(
        self,
        video_path: Path,
        description: str,
        publish_now: bool = True,
        scheduled_epoch_time: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Sube un video MP4 a Facebook Reels en 3 sencillos pasos oficiales de Meta:
        1. Iniciar sesión de subida (/video_reels)
        2. Transferir archivo binario (rupload.facebook.com)
        3. Publicar o programar el Reel
        """
        if not self.page_id or not self.access_token:
            print("[FacebookUploader] [!] Falta FACEBOOK_PAGE_ID o FACEBOOK_ACCESS_TOKEN. Omitiendo subida.")
            return {"status": "skipped", "message": "Missing credentials"}

        if not video_path.exists():
            raise FileNotFoundError(f"El archivo de video no existe: {video_path}")

        file_size = video_path.stat().st_size
        print(f"[FacebookUploader] Iniciando subida de Reel ({file_size / (1024*1024):.2f} MB)...")

        # -------------------------------------------------------------
        # PASO 1: Iniciar Sesión de Subida en Facebook Reels
        # -------------------------------------------------------------
        init_url = f"https://graph.facebook.com/{self.graph_version}/{self.page_id}/video_reels"
        init_payload = {
            "upload_phase": "start",
            "access_token": self.access_token
        }
        
        init_res = requests.post(init_url, data=init_payload, timeout=30)
        if init_res.status_code != 200:
            err = init_res.json()
            print(f"[FacebookUploader] [ERROR Fase 1 - Start]: {err}")
            return {"status": "error", "step": "start", "response": err}

        init_data = init_res.json()
        video_id = init_data.get("video_id")
        upload_url = init_data.get("upload_url")
        print(f"[FacebookUploader] Sesión iniciada con éxito. Video ID: {video_id}")

        # -------------------------------------------------------------
        # PASO 2: Transferir el Archivo Binario (.mp4)
        # -------------------------------------------------------------
        if not upload_url:
            upload_url = f"https://rupload.facebook.com/video-upload/{self.graph_version}/{video_id}"

        headers = {
            "Authorization": f"OAuth {self.access_token}",
            "offset": "0",
            "file_size": str(file_size),
            "Content-Type": "application/octet-stream"
        }

        print("[FacebookUploader] Transfiriendo archivo binario de video a los servidores de Meta...")
        with open(video_path, "rb") as video_file:
            upload_res = requests.post(upload_url, headers=headers, data=video_file, timeout=120)

        if upload_res.status_code not in [200, 201]:
            err = upload_res.text
            print(f"[FacebookUploader] [ERROR Fase 2 - Transfer]: {err}")
            return {"status": "error", "step": "transfer", "response": err}

        print("[FacebookUploader] Transferencia de video completada al 100%.")

        # -------------------------------------------------------------
        # PASO 3: Publicar o Programar el Reel
        # -------------------------------------------------------------
        publish_url = f"https://graph.facebook.com/{self.graph_version}/{self.page_id}/video_reels"
        publish_payload = {
            "upload_phase": "finish",
            "access_token": self.access_token,
            "video_id": video_id,
            "video_state": "PUBLISHED" if publish_now else "SCHEDULED",
            "description": description
        }

        if not publish_now and scheduled_epoch_time:
            publish_payload["scheduled_publish_time"] = str(scheduled_epoch_time)

        print("[FacebookUploader] Publicando Reel con descripción y hashtags...")
        publish_res = requests.post(publish_url, data=publish_payload, timeout=30)
        
        if publish_res.status_code == 200:
            result = publish_res.json()
            print(f"[FacebookUploader] [¡ÉXITO TOTAL! 🎉] Reel publicado en Facebook: {result}")
            return {"status": "success", "video_id": video_id, "result": result}
        else:
            err = publish_res.json()
            print(f"[FacebookUploader] [ERROR Fase 3 - Publish]: {err}")
            return {"status": "error", "step": "publish", "response": err}

def upload_to_facebook_reels(video_path: Path, description: str) -> Dict[str, Any]:
    """Función de acceso directo para subir un video a Facebook Reels."""
    uploader = FacebookReelsUploader()
    return uploader.upload_reel(video_path, description)

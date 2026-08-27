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

    def post_comment(self, object_id: str, message: str, video_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Publica un auto-comentario interactivo (Poll / Pregunta) en el Reel de Facebook.
        Prueba inteligentemente los formatos soportados por la Graph API de Meta (video_id y page_id_post_id).
        """
        if not self.page_id or not self.access_token or not message:
            return None

        # Esperar 8 segundos para que Meta termine de transcodificar e indexar el Reel
        print("[FacebookUploader] Esperando 8 segundos para que el Reel esté listo para comentar...")
        time.sleep(8)

        candidate_targets = []
        if video_id:
            candidate_targets.append(video_id)
        if object_id:
            if "_" not in object_id and self.page_id != object_id:
                candidate_targets.append(f"{self.page_id}_{object_id}")
            candidate_targets.append(object_id)

        for target in candidate_targets:
            url = f"https://graph.facebook.com/{self.graph_version}/{target}/comments"
            payload = {
                "message": message,
                "access_token": self.access_token
            }
            try:
                print(f"[FacebookUploader] [+] Publicando auto-comentario en destino '{target}'...")
                res = requests.post(url, data=payload, timeout=20)
                if res.status_code == 200:
                    result = res.json()
                    print(f"[FacebookUploader] [✓] ¡Auto-comentario publicado con éxito en Facebook! (ID: {result.get('id')})")
                    return result
                else:
                    print(f"[FacebookUploader] [!] Intento en '{target}' respondió ({res.status_code}): {res.text[:120]}...")
            except Exception as e:
                print(f"[FacebookUploader] [!] Excepción en '{target}': {e}")
        return None

    def upload_reel(
        self,
        video_path: Path,
        description: str,
        publish_now: bool = True,
        scheduled_epoch_time: Optional[int] = None,
        comment_text: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Sube un video MP4 a Facebook Reels en 3 pasos oficiales de Meta:
        1. Iniciar sesión de subida (/video_reels)
        2. Transferir archivo binario (rupload.facebook.com)
        3. Publicar o programar el Reel
        4. Publicar auto-comentario de interacción
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
            upload_res = requests.post(upload_url, headers=headers, data=video_file, timeout=180)

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
            post_id = result.get("post_id") or video_id
            print(f"[FacebookUploader] [¡ÉXITO TOTAL! 🎉] Reel publicado en Facebook: {result}")

            # -------------------------------------------------------------
            # PASO 4: Auto-comentario de alta interacción
            # -------------------------------------------------------------
            if comment_text:
                self.post_comment(post_id, comment_text, video_id=video_id)

            return {"status": "success", "video_id": video_id, "post_id": post_id, "result": result}
        else:
            err = publish_res.json()
            print(f"[FacebookUploader] [ERROR Fase 3 - Publish]: {err}")
            return {"status": "error", "step": "publish", "response": err}

def upload_to_facebook_reels(video_path: Path, description: str, comment_text: Optional[str] = None) -> Dict[str, Any]:
    """Función de acceso directo para subir un video a Facebook Reels con auto-comment."""
    uploader = FacebookReelsUploader()
    return uploader.upload_reel(video_path, description, comment_text=comment_text)

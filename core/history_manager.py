import json
import os
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime

HISTORY_FILE = Path(__file__).resolve().parent.parent / "history.json"

class HistoryManager:
    @staticmethod
    def load_history() -> Dict[str, Any]:
        """Carga el historial persistente de videos publicados."""
        if not HISTORY_FILE.exists():
            default_history = {
                "published_topics": [],
                "total_published_count": 0,
                "history_log": []
            }
            HistoryManager.save_history(default_history)
            return default_history

        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[HistoryManager] [!] Error leyendo history.json: {e}. Creando nuevo.")
            return {"published_topics": [], "total_published_count": 0, "history_log": []}

    @staticmethod
    def save_history(data: Dict[str, Any]):
        """Guarda atómicamente el historial en history.json."""
        HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def get_next_unique_topic(available_topics: List[str]) -> str:
        """
        Garantiza de forma ultra estricta que NO SE REPITA ningún tema.
        Selecciona el primer tema del catálogo que nunca haya sido utilizado.
        """
        history = HistoryManager.load_history()
        published = set(history.get("published_topics", []))

        print(f"[HistoryManager] Temas previamente publicados ({len(published)}): {list(published)}")

        # 1. Filtrar temas estrictamente no utilizados
        unused = [t for t in available_topics if t not in published]

        if unused:
            chosen = unused[0]
            print(f"[HistoryManager] [+] Tema nuevo e inédito seleccionado: '{chosen.upper()}' (Restantes en ciclo: {len(unused)-1})")
            return chosen

        # 2. Si todos los temas del catálogo ya se publicaron, se reinicia el ciclo de temas
        print("[HistoryManager] [!] Todos los temas del catálogo actual han sido publicados. Reiniciando ciclo con nuevos hooks.")
        history["published_topics"] = []
        HistoryManager.save_history(history)
        return available_topics[0]

    @staticmethod
    def record_published(topic_key: str, title: str, post_id: Optional[str] = None):
        """Registra de forma permanente un video publicado para evitar duplicados."""
        history = HistoryManager.load_history()
        
        if topic_key not in history["published_topics"]:
            history["published_topics"].append(topic_key)
            
        history["total_published_count"] = history.get("total_published_count", 0) + 1
        
        entry = {
            "timestamp": datetime.now().isoformat(),
            "topic": topic_key,
            "title": title,
            "facebook_post_id": post_id or "local_only"
        }
        
        history["history_log"].append(entry)
        HistoryManager.save_history(history)
        print(f"[HistoryManager] [OK] Registrado '{topic_key}' en history.json con éxito.")

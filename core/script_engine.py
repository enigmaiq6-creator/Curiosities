import random
import re
from typing import List, Dict, Any
from core.topic_catalog import TOPICS_DB

HOOKS_EN = [
    "Did you know these five unbelievable facts about {topic}?",
    "Here are five mind-blowing secrets about {topic} that will shock you!",
    "You won't believe these five crazy truths about {topic}!",
    "Scientists were stunned to discover these five facts about {topic}!",
    "Think you know everything about {topic}? These five secrets will blow your mind!"
]

class ScriptEngine:
    @staticmethod
    def get_dynamic_hook(topic_name: str, lang: str = "en") -> str:
        """Devuelve un gancho inicial viral aleatorio y adaptado al tema en inglés."""
        template = random.choice(HOOKS_EN)
        return template.format(topic=topic_name)

    @staticmethod
    def parse_curiosity_script(raw_text: str) -> List[Dict[str, Any]]:
        """Divide un texto de curiosidades en escenas individuales e infiere palabras clave."""
        lines = [l.strip() for l in raw_text.strip().split("\n") if l.strip()]
        scenes = []
        
        for i, line in enumerate(lines):
            clean_line = re.sub(r'^(?:Curiosity\s*\d+:?|\d+[\.\-\)]|\-)\s*', '', line, flags=re.IGNORECASE).strip()
            if not clean_line:
                continue

            words = re.findall(r'\b[a-zA-Z]{4,}\b', clean_line)
            stopwords = {"this", "that", "these", "those", "with", "from", "have", "make", "about", "which", "number", "will", "more"}
            keywords = [w for w in words if w.lower() not in stopwords]
            
            main_subject = keywords[0].lower() if keywords else "curiosity"

            scenes.append({
                "scene_id": i + 1,
                "text": clean_line,
                "subject": main_subject,
                "keywords": keywords[:3] if keywords else ["curiosities", "science"]
            })

        return scenes

    @staticmethod
    def create_sample_script(topic: str = "egypt") -> List[Dict[str, Any]]:
        """
        Crea guiones 100% en INGLÉS a partir del Mega Catálogo TOPICS_DB:
        1. Gancho inicial dinámico y variado (Intro Hook).
        2. 5 Curiosidades científicas / históricas de impacto.
        3. Call To Action (CTA) al final.
        """
        t_key = topic.lower().strip()
        
        # Buscar coincidencia en TOPICS_DB
        topic_info = TOPICS_DB.get(t_key)
        if not topic_info:
            for key, val in TOPICS_DB.items():
                if key in t_key or t_key in key:
                    topic_info = val
                    t_key = key
                    break

        if not topic_info:
            topic_info = TOPICS_DB["egypt"]
            t_key = "egypt"

        intro_tag = topic_info.get("intro_tag", "this incredible topic")
        hook_text = ScriptEngine.get_dynamic_hook(intro_tag, lang="en")
        
        # Obtener palabras clave cinematográficas específicas para el gancho
        clean_topic_name = intro_tag.replace("_", " ")
        hook_keywords = [
            f"{clean_topic_name} mysterious cinematic 4k",
            f"{clean_topic_name} documentary 4k",
            f"{clean_topic_name} epic 4k"
        ]
        hook_subject = clean_topic_name

        hook_scene = {
            "scene_id": 1,
            "is_hook": True,
            "text": hook_text,
            "subject": hook_subject,
            "keywords": hook_keywords
        }

        return [hook_scene] + topic_info["scenes"]

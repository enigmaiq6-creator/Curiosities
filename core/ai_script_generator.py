import os
import json
import urllib.request
import urllib.error
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv
from core.history_manager import HistoryManager

load_dotenv()

SYSTEM_PROMPT = """You are an elite scientific documentary researcher and viral scriptwriter for YouTube Shorts, TikTok, and Facebook Reels (Curiosities Channel).
Your task is to invent a BRAND NEW, 100% FACTUAL, MIND-BLOWING curiosity topic in English that has NEVER been covered before.

You must output ONLY valid JSON matching this exact structure:
{
  "topic_id": "unique_slug_lowercase",
  "title": "5 Insane Facts About [Topic Name]! 🌌✨",
  "intro_tag": "short engaging topic description",
  "scenes": [
    {
      "scene_id": 2,
      "curiosity_index": 1,
      "text": "Number one: [First sentence of fact 1, shocking and punchy].",
      "subject": "natural concrete subject keyword (e.g. black hole, glacier, supernova, mammoth, volcano, brain, deep sea creature, pyramid, diamond, amazon river)",
      "keywords": ["specific visual query 1 4k", "specific visual query 2 cinematic", "specific visual query 3"]
    },
    {
      "scene_id": 3,
      "curiosity_index": 1,
      "text": "[Second sentence of fact 1 explaining why or scientific context].",
      "subject": "same or related visual subject",
      "keywords": ["specific visual query 1 4k", "specific visual query 2 cinematic", "specific visual query 3"]
    },
    {
      "scene_id": 4,
      "curiosity_index": 2,
      "text": "Number two: [First sentence of fact 2].",
      "subject": "visual subject",
      "keywords": ["specific visual query 1 4k", "specific visual query 2 cinematic", "specific visual query 3"]
    },
    {
      "scene_id": 5,
      "curiosity_index": 2,
      "text": "[Second sentence of fact 2].",
      "subject": "visual subject",
      "keywords": ["specific visual query 1 4k", "specific visual query 2 cinematic", "specific visual query 3"]
    },
    {
      "scene_id": 6,
      "curiosity_index": 3,
      "text": "Number three: [First sentence of fact 3].",
      "subject": "visual subject",
      "keywords": ["specific visual query 1 4k", "specific visual query 2 cinematic", "specific visual query 3"]
    },
    {
      "scene_id": 7,
      "curiosity_index": 3,
      "text": "[Second sentence of fact 3].",
      "subject": "visual subject",
      "keywords": ["specific visual query 1 4k", "specific visual query 2 cinematic", "specific visual query 3"]
    },
    {
      "scene_id": 8,
      "curiosity_index": 4,
      "text": "Number four: [First sentence of fact 4].",
      "subject": "visual subject",
      "keywords": ["specific visual query 1 4k", "specific visual query 2 cinematic", "specific visual query 3"]
    },
    {
      "scene_id": 9,
      "curiosity_index": 4,
      "text": "[Second sentence of fact 4].",
      "subject": "visual subject",
      "keywords": ["specific visual query 1 4k", "specific visual query 2 cinematic", "specific visual query 3"]
    },
    {
      "scene_id": 10,
      "curiosity_index": 5,
      "text": "Number five: [First sentence of fact 5].",
      "subject": "visual subject",
      "keywords": ["specific visual query 1 4k", "specific visual query 2 cinematic", "specific visual query 3"]
    },
    {
      "scene_id": 11,
      "curiosity_index": 5,
      "text": "[Second sentence of fact 5].",
      "subject": "visual subject",
      "keywords": ["specific visual query 1 4k", "specific visual query 2 cinematic", "specific visual query 3"]
    },
    {
      "scene_id": 12,
      "is_cta": true,
      "text": "Which of these incredible facts blew your mind? Drop a comment, hit LIKE, and FOLLOW for daily wonders!",
      "subject": "visual subject",
      "keywords": ["deep space universe stars 4k", "majestic nature landscape 4k", "cinematic cosmos 4k"]
    }
  ]
}

STRICT RULES:
1. Every fact must be 100% scientifically or historically verified (zero fake news/myths).
2. Use simple, natural English words that sound engaging when spoken by a narrator.
3. Write numbers as words when necessary for smooth speech synthesis.
4. Provide highly descriptive, real-world keywords for each scene that stock photo/video sites can easily find.
5. Output raw JSON only with NO markdown fences or additional explanation."""

class AIScriptGenerator:
    @staticmethod
    def generate_unique_topic_with_ai() -> Optional[Dict[str, Any]]:
        """
        Consulta a la IA de Groq para inventar un tema 100% inédito en inglés,
        excluyendo todo lo previamente publicado en history.json.
        Soporta rotación de claves primarias y de respaldo (GROQ_API_KEY y GROQ_API_KEY_BACKUP).
        """
        keys_to_try = [
            os.getenv("GROQ_API_KEY", "").strip(),
            os.getenv("GROQ_API_KEY_BACKUP", "").strip()
        ]
        valid_keys = [k for k in keys_to_try if k]

        if not valid_keys:
            print("[AIScriptGenerator] [!] No GROQ_API_KEY provided in environment.", flush=True)
            return None

        history = HistoryManager.load_history()
        published_topics = history.get("published_topics", [])
        
        user_prompt = (
            f"Here are the topics already published (DO NOT REPEAT ANY OF THESE OR SIMILAR CONCEPTS):\n"
            f"{', '.join(published_topics[-60:])}\n\n"
            f"Please invent a brand-new, completely different, ultra-fascinating curiosity topic in JSON format about astrophysics, ancient history, paleontology, quantum science, deep biology, geology, human body mysteries, or nature extremes."
        )

        models_to_try = [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "gemma2-9b-it"
        ]

        for key_idx, api_key in enumerate(valid_keys, 1):
            for model in models_to_try:
                try:
                    key_tag = f"Key {key_idx}" if len(valid_keys) > 1 else "Primary Key"
                    print(f"[AIScriptGenerator] [+] Consultando Groq AI ({model}) [{key_tag}] para generar tema inedito...", flush=True)
                    url = "https://api.groq.com/openai/v1/chat/completions"
                    headers = {
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                        "User-Agent": "CuriositiesEngine/1.0"
                    }
                    payload = {
                        "model": model,
                        "messages": [
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": user_prompt}
                        ],
                        "temperature": 0.85,
                        "response_format": {"type": "json_object"}
                    }

                    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
                    with urllib.request.urlopen(req, timeout=30) as resp:
                        res_data = json.loads(resp.read().decode("utf-8"))
                        raw_content = res_data["choices"][0]["message"]["content"]
                        
                        topic_data = json.loads(raw_content)
                        
                        # Validar estructura minima
                        if "topic_id" in topic_data and "scenes" in topic_data and len(topic_data["scenes"]) >= 10:
                            safe_title = str(topic_data.get('title', '')).encode('ascii', 'ignore').decode()
                            print(f"[AIScriptGenerator] [EXITO TOTAL] Tema creado con IA: '{topic_data['topic_id'].upper()}' - {safe_title}", flush=True)
                            return topic_data

                except Exception as e:
                    print(f"[AIScriptGenerator] [!] Fallo con modelo {model} ({key_tag}): {e}. Probando siguiente opcion...", flush=True)

        # Respaldo con Google Gemini si está configurado
        gemini_key = os.getenv("GEMINI_API_KEY", "").strip() or os.getenv("GEMINI_API_KEY_2", "").strip()
        if gemini_key:
            print("[AIScriptGenerator] [+] Intentando generacion con Google Gemini API...", flush=True)
            for g_model in ["gemini-1.5-flash", "gemini-2.0-flash"]:
                try:
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{g_model}:generateContent?key={gemini_key}"
                    headers = {"Content-Type": "application/json"}
                    payload = {
                        "contents": [
                            {"role": "user", "parts": [{"text": f"{SYSTEM_PROMPT}\n\n{user_prompt}"}]}
                        ],
                        "generationConfig": {
                            "responseMimeType": "application/json",
                            "temperature": 0.85
                        }
                    }
                    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
                    with urllib.request.urlopen(req, timeout=30) as resp:
                        res_data = json.loads(resp.read().decode("utf-8"))
                        text_resp = res_data["candidates"][0]["content"]["parts"][0]["text"]
                        topic_data = json.loads(text_resp)
                        if "topic_id" in topic_data and "scenes" in topic_data and len(topic_data["scenes"]) >= 10:
                            safe_title = str(topic_data.get('title', '')).encode('ascii', 'ignore').decode()
                            print(f"[AIScriptGenerator] [EXITO TOTAL GEMINI] Tema creado con Gemini: '{topic_data['topic_id'].upper()}' - {safe_title}", flush=True)
                            return topic_data
                except Exception as ge:
                    print(f"[AIScriptGenerator] [!] Fallo Gemini {g_model}: {ge}", flush=True)

        print("[AIScriptGenerator] [!] No se pudo generar con IA tras probar todas las claves/modelos, usando catalogo preconstruido.", flush=True)
        return None

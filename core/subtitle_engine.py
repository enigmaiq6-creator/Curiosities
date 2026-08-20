import re
from pathlib import Path
from typing import List, Dict, Any
from config import RESOLUTIONS

def format_ass_time(seconds: float) -> str:
    """Convierte segundos a formato de tiempo ASS: H:MM:SS.cs con precisión de centésimas."""
    seconds = max(0.0, seconds)
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    cs = int(round((seconds - int(seconds)) * 100))
    if cs >= 100:
        cs = 99
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"

def wrap_text_lines(text: str, max_chars_per_line: int = 34) -> str:
    """Divide oraciones largas en máximo 2 líneas equilibradas usando \\N."""
    words = text.split()
    if len(text) <= max_chars_per_line or len(words) <= 4:
        return text

    # Buscar punto medio para partir en 2 líneas equilibradas
    mid = len(words) // 2
    line1 = " ".join(words[:mid])
    line2 = " ".join(words[mid:])
    return f"{line1}\\N{line2}"

class SubtitleEngine:
    def __init__(self, aspect_ratio: str = "vertical"):
        self.res = RESOLUTIONS.get(aspect_ratio, RESOLUTIONS["vertical"])
        self.width = self.res["width"]
        self.height = self.res["height"]

    def create_ass_subtitles(self, scene_data: List[Dict[str, Any]], output_ass_path: Path, total_video_duration: float = 60.0):
        """
        Genera subtítulos estilo DOCUMENTAL CLÁSICO (BBC / National Geographic):
        1. Frases completas y legibles de 4 a 7 palabras por bloque.
        2. Texto en mayúsculas/minúsculas naturales (Sentence Case) de alta elegancia.
        3. Transición cinemática suave con Fade (fad) sin saltos bruscos ni parpadeos.
        4. Ubicación en tercio inferior optimizada para Reels/Shorts sin tapar la UI.
        5. Sello numérico minimalista (#01 a #05) dorado en la esquina superior.
        """
        output_ass_path.parent.mkdir(parents=True, exist_ok=True)
        
        font_size = 44 if self.width == 1080 else 48
        margin_v = 200 if self.width == 1080 else 100

        header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {self.width}
PlayResY: {self.height}
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: NumberStamp,Arial,68,&H0000D4FF,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,5,2,7,60,60,110,1
Style: DocSubtitle,Arial,{font_size},&H00FFFFFF,&H0000D4FF,&H00000000,&HA0000000,-1,0,0,0,100,100,0,0,1,3.5,2,2,50,50,{margin_v},1
Style: DocHook,Arial,{font_size + 4},&H0000FFFF,&H00FFFFFF,&H00000000,&HA0000000,-1,0,0,0,100,100,0,0,1,4,2,2,40,40,{margin_v},1
Style: DocCTA,Arial,{font_size + 2},&H0000D4FF,&H00FFFFFF,&H00000000,&HA0000000,-1,0,0,0,100,100,0,0,1,4,2,2,40,40,{margin_v - 20},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

        events = []
        curiosity_seen = set()

        for scene in scene_data:
            scene_start = scene.get("global_start", 0.0)
            scene_dur = scene.get("duration", 5.0)
            scene_end = scene_start + scene_dur
            is_hook = scene.get("is_hook", False)
            is_cta = scene.get("is_cta", False)
            curiosity_num = scene.get("curiosity_index", None)

            # 1. Sello numérico sutil (#01 a #05)
            if curiosity_num and curiosity_num not in curiosity_seen:
                curiosity_seen.add(curiosity_num)
                stamp_start = scene_start
                stamp_end = scene_start + min(2.2, scene_dur)
                
                s_t = format_ass_time(stamp_start)
                e_t = format_ass_time(stamp_end)
                
                stamp_text = f"{{\\fad(150,300)\\c&H0000D4FF&\\3c&H00000000&\\bord5\\shad2}}#{curiosity_num:02d}"
                events.append(f"Dialogue: 1,{s_t},{e_t},NumberStamp,,0,0,0,,{stamp_text}")

            # 2. Determinar estilo documental
            if is_hook:
                style_name = "DocHook"
            elif is_cta:
                style_name = "DocCTA"
            else:
                style_name = "DocSubtitle"

            word_timings = scene.get("word_timings", [])
            raw_text = scene.get("text", "").strip()

            if not word_timings:
                formatted_text = wrap_text_lines(raw_text)
                s_time = format_ass_time(scene_start)
                e_time = format_ass_time(scene_end)
                events.append(f"Dialogue: 0,{s_time},{e_time},{style_name},,0,0,0,,{{\\fad(100,100)}}{formatted_text}")
                continue

            # 3. Agrupar palabras en frases completas naturales (4 a 7 palabras o por puntuación)
            sentence_chunks = []
            current_chunk = []
            
            for w_idx, w_info in enumerate(word_timings):
                w_text = w_info["word"].strip()
                if not w_text:
                    continue
                current_chunk.append(w_info)
                
                has_strong_punct = any(p in w_text for p in [".", "!", "?", ":", ";"])
                has_soft_punct = any(p in w_text for p in [",", "—", "-"])
                
                # Partir si hay punto/dos puntos, o si supera 5 palabras con coma, o al llegar a 7 palabras
                if has_strong_punct or (has_soft_punct and len(current_chunk) >= 4) or len(current_chunk) >= 6 or w_idx == len(word_timings) - 1:
                    sentence_chunks.append(current_chunk)
                    current_chunk = []

            # 4. Generar eventos con transición suave
            for idx_c, chunk in enumerate(sentence_chunks):
                chunk_raw_start = scene_start + chunk[0]["start"]
                chunk_raw_end = scene_start + chunk[-1]["end"]
                
                c_start = max(scene_start, chunk_raw_start)
                
                # Extender suavemente hasta el inicio del siguiente bloque o fin de escena
                if idx_c < len(sentence_chunks) - 1:
                    next_start = scene_start + sentence_chunks[idx_c + 1][0]["start"]
                    c_end = min(next_start, chunk_raw_end + 0.2)
                else:
                    c_end = min(scene_end, chunk_raw_end + 0.3)

                c_start_str = format_ass_time(c_start)
                c_end_str = format_ass_time(c_end)

                # Construir texto de la frase completa con formato limpio
                chunk_words = [w["word"] for w in chunk]
                clause_text = " ".join(chunk_words)
                
                # Ajustar a máximo 2 líneas si es larga
                wrapped_clause = wrap_text_lines(clause_text, max_chars_per_line=36)
                
                # Animación suave de aparición y desaparición (Fade in/out de 100ms)
                dialogue_text = f"{{\\fad(100,100)}}{wrapped_clause}"
                events.append(f"Dialogue: 0,{c_start_str},{c_end_str},{style_name},,0,0,0,,{dialogue_text}")

        with open(output_ass_path, "w", encoding="utf-8") as f:
            f.write(header + "\n".join(events) + "\n")
            
        return output_ass_path

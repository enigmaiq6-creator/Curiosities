import re
from pathlib import Path
from typing import List, Dict, Any
from config import RESOLUTIONS

def format_ass_time(seconds: float) -> str:
    """Convierte segundos a formato de tiempo ASS: H:MM:SS.cs"""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    cs = int(round((seconds - int(seconds)) * 100))
    if cs >= 100:
        cs = 99
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"

class SubtitleEngine:
    def __init__(self, aspect_ratio: str = "vertical"):
        self.res = RESOLUTIONS.get(aspect_ratio, RESOLUTIONS["vertical"])
        self.width = self.res["width"]
        self.height = self.res["height"]

    def create_ass_subtitles(self, scene_data: List[Dict[str, Any]], output_ass_path: Path, total_video_duration: float = 60.0):
        """
        Genera subtítulos dinámicos de alto impacto con:
        1. Gancho inicial (Intro Hook) con tipografía destacada de gran retención.
        2. Sello numérico flotante (#01 a #05) al inicio de cada curiosidad.
        3. Subtítulos dinámicos palabra por palabra con resaltado dorado.
        4. Escena final de CTA (Call To Action) animada para conversión.
        """
        output_ass_path.parent.mkdir(parents=True, exist_ok=True)
        
        font_size = 46 if self.width == 1080 else 52
        margin_v = 280 if self.width == 1080 else 120

        header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {self.width}
PlayResY: {self.height}
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: NumberStamp,Arial Black,72,&H0000FFFF,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,6,3,7,60,60,100,1
Style: HookStyle,Arial Black,{font_size + 4},&H00FFFFFF,&H0000FFFF,&H00000000,&HB0000000,-1,0,0,0,100,100,0,0,1,6,4,2,30,30,{margin_v},1
Style: SubtitleActive,Arial Black,{font_size},&H00FFFFFF,&H0000FFFF,&H00000000,&HB0000000,-1,0,0,0,100,100,0,0,1,5,3,2,40,40,{margin_v},1
Style: CTAStyle,Arial Black,{font_size + 4},&H0000FFFF,&H00FFFFFF,&H00000000,&HB0000000,-1,0,0,0,100,100,0,0,1,6,4,2,30,30,{margin_v - 20},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

        events = []
        curiosity_seen = set()

        for scene in scene_data:
            scene_start = scene.get("global_start", 0.0)
            scene_dur = scene.get("duration", 5.0)
            is_hook = scene.get("is_hook", False)
            is_cta = scene.get("is_cta", False)
            curiosity_num = scene.get("curiosity_index", None)

            # 1. Sello numérico flotante (#01 a #05) (solo en curiosidades reales)
            if curiosity_num and curiosity_num not in curiosity_seen:
                curiosity_seen.add(curiosity_num)
                stamp_start = scene_start
                stamp_end = scene_start + min(1.8, scene_dur)
                
                s_t = format_ass_time(stamp_start)
                e_t = format_ass_time(stamp_end)
                
                stamp_text = f"{{\\fad(150,300)\\c&H0000FFFF&\\3c&H00000000&\\bord6\\shad2}}#{curiosity_num:02d}"
                events.append(f"Dialogue: 1,{s_t},{e_t},NumberStamp,,0,0,0,,{stamp_text}")

            # 2. Determinar estilo de subtítulo
            if is_hook:
                style_name = "HookStyle"
            elif is_cta:
                style_name = "CTAStyle"
            else:
                style_name = "SubtitleActive"

            word_timings = scene.get("word_timings", [])
            if not word_timings:
                text = scene.get("text", "").upper()
                s_time = format_ass_time(scene_start)
                e_time = format_ass_time(scene_start + scene_dur)
                events.append(f"Dialogue: 0,{s_time},{e_time},{style_name},,0,0,0,,{text}")
                continue

            chunk_size = 3
            for i in range(0, len(word_timings), chunk_size):
                chunk = word_timings[i:i+chunk_size]
                chunk_start = scene_start + chunk[0]["start"]
                chunk_end = scene_start + chunk[-1]["end"]
                chunk_end = max(chunk_end, chunk_start + 0.6)

                c_start_str = format_ass_time(chunk_start)
                c_end_str = format_ass_time(chunk_end)

                styled_words = []
                for idx, w_info in enumerate(chunk):
                    w_text = w_info["word"].upper()
                    
                    if is_hook:
                        # Palabras clave del gancho en amarillo brillante
                        if any(k in w_text for k in ["FIVE", "FACTS", "SECRETS", "CRAZY", "SHOCK", "MIND", "UNBELIEVABLE", "DATOS", "CINCO", "SECRETOS", "FASCINANTES"]):
                            styled_words.append(f"{{\\c&H0000FFFF&\\fscx108\\fscy108}}{w_text}")
                        else:
                            styled_words.append(f"{{\\c&H00FFFFFF&}}{w_text}")
                    elif is_cta:
                        # Palabras clave de llamada a la acción en amarillo brillante
                        if any(k in w_text for k in ["LIKE", "COMMENT", "FOLLOW", "AMAZED", "DISCOVERIES", "COMENTA", "SÍGUENOS", "SIGUENOS", "FAVORITO"]):
                            styled_words.append(f"{{\\c&H0000FFFF&\\fscx110\\fscy110}}{w_text}")
                        else:
                            styled_words.append(f"{{\\c&H00FFFFFF&}}{w_text}")
                    else:
                        # Curiosidad normal: última palabra clave resaltada
                        if idx == len(chunk) - 1:
                            styled_words.append(f"{{\\c&H0000FFFF&}}{w_text}")
                        else:
                            styled_words.append(f"{{\\c&H00FFFFFF&}}{w_text}")

                full_chunk_str = " ".join(styled_words)
                events.append(f"Dialogue: 0,{c_start_str},{c_end_str},{style_name},,0,0,0,,{full_chunk_str}")

        with open(output_ass_path, "w", encoding="utf-8") as f:
            f.write(header + "\n".join(events) + "\n")
            
        return output_ass_path

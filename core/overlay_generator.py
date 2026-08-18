import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from typing import Tuple, Optional

FONT_PATH_BOLD = "C:/Windows/Fonts/segoeuib.ttf" if os.path.exists("C:/Windows/Fonts/segoeuib.ttf") else "C:/Windows/Fonts/arialbd.ttf"
FONT_PATH_REGULAR = "C:/Windows/Fonts/segoeui.ttf" if os.path.exists("C:/Windows/Fonts/segoeui.ttf") else "C:/Windows/Fonts/arial.ttf"

class OverlayGenerator:
    def __init__(self, temp_dir: Path, width: int = 1080, height: int = 1920):
        self.temp_dir = temp_dir / "overlays"
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self.width = width
        self.height = height

    def generate_header_badge(self, curiosity_num: int, total_num: int = 5, topic_name: str = "CURIOSIDADES") -> Path:
        """
        Genera una cápsula de cabecera con estilo Glassmorphic prémium (estudio documental / Vox / Apple TV).
        """
        out_path = self.temp_dir / f"header_badge_{curiosity_num}.png"
        
        # Crear lienzo transparente 1080x1920
        img = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Dimensiones de la cápsula
        pill_w = 640
        pill_h = 86
        pill_x1 = (self.width - pill_w) // 2
        pill_y1 = 120
        pill_x2 = pill_x1 + pill_w
        pill_y2 = pill_y1 + pill_h
        radius = pill_h // 2

        # 1. Sombra difusa exterior para profundidad
        shadow_img = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow_img)
        shadow_draw.rounded_rectangle(
            [pill_x1 - 4, pill_y1 + 4, pill_x2 + 4, pill_y2 + 8],
            radius=radius + 2,
            fill=(0, 0, 0, 160)
        )
        shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(10))
        img = Image.alpha_composite(img, shadow_img)
        draw = ImageDraw.Draw(img)

        # 2. Fondo principal oscuro tipo vidrio ahumado (Glassmorphism)
        draw.rounded_rectangle(
            [pill_x1, pill_y1, pill_x2, pill_y2],
            radius=radius,
            fill=(12, 18, 28, 235),
            outline=(255, 215, 0, 180), # Borde dorado fino de lujo
            width=2
        )

        # 3. Badge numérico a la izquierda (Cápsula dorada sólida '#01', '#02')
        num_w = 110
        num_h = pill_h - 16
        num_x1 = pill_x1 + 10
        num_y1 = pill_y1 + 8
        num_x2 = num_x1 + num_w
        num_y2 = num_y1 + num_h
        
        draw.rounded_rectangle(
            [num_x1, num_y1, num_x2, num_y2],
            radius=(num_h // 2),
            fill=(255, 210, 30, 255) # Amarillo/Dorado vibrante
        )

        # Texto del número '#01'
        font_num = ImageFont.truetype(FONT_PATH_BOLD, 36)
        num_text = f"#{curiosity_num:02d}"
        bbox_num = font_num.getbbox(num_text)
        text_num_w = bbox_num[2] - bbox_num[0]
        text_num_h = bbox_num[3] - bbox_num[1]
        draw.text(
            (num_x1 + (num_w - text_num_w) // 2, num_y1 + (num_h - text_num_h) // 2 - 4),
            num_text,
            fill=(10, 15, 25, 255),
            font=font_num
        )

        # 4. Texto del Tópico a la derecha (Ej. 'MISTERIOS DEL OCÉANO')
        font_title = ImageFont.truetype(FONT_PATH_BOLD, 28)
        clean_topic = topic_name.upper().replace("_", " ")
        if len(clean_topic) > 22:
            clean_topic = clean_topic[:20] + "..."
        
        title_display = f"{clean_topic}  •  {curiosity_num}/{total_num}"
        bbox_title = font_title.getbbox(title_display)
        title_h = bbox_title[3] - bbox_title[1]
        
        text_x = num_x2 + 25
        text_y = pill_y1 + (pill_h - title_h) // 2 - 4
        
        draw.text(
            (text_x, text_y),
            title_display,
            fill=(255, 255, 255, 245),
            font=font_title
        )

        img.save(out_path, "PNG")
        return out_path

    def generate_vignette_overlay(self) -> Path:
        """
        Crea una máscara de viñeta profesional para oscurecer suavemente la parte superior e inferior.
        """
        out_path = self.temp_dir / "cinematic_vignette.png"
        if out_path.exists():
            return out_path

        img = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Gradiente superior (0 a 300px)
        for y in range(320):
            alpha = int(170 * (1 - (y / 320) ** 1.5))
            draw.line([(0, y), (self.width, y)], fill=(0, 0, 0, alpha))

        # Gradiente inferior (1400 a 1920px) para respaldar los subtítulos
        for y in range(1450, self.height):
            progress = (y - 1450) / (self.height - 1450)
            alpha = int(190 * (progress ** 1.3))
            draw.line([(0, y), (self.width, y)], fill=(0, 0, 0, alpha))

        img.save(out_path, "PNG")
        return out_path

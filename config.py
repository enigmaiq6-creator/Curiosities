import os
from pathlib import Path

# Directorio raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent

# Directorios de trabajo
ASSETS_DIR = BASE_DIR / "assets"
MUSIC_DIR = ASSETS_DIR / "music"
FONTS_DIR = ASSETS_DIR / "fonts"
TEMP_DIR = BASE_DIR / "temp"
OUTPUT_DIR = BASE_DIR / "output"

# Asegurar que existan los directorios
for folder in [ASSETS_DIR, MUSIC_DIR, FONTS_DIR, TEMP_DIR, OUTPUT_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

# Opciones de Resolución de Video
RESOLUTIONS = {
    "vertical": {"width": 1080, "height": 1920, "aspect": "9:16"},    # TikTok / Shorts / Reels
    "horizontal": {"width": 1920, "height": 1080, "aspect": "16:9"}   # YouTube estándar
}

# Configuración de Video por defecto
DEFAULT_ASPECT = "vertical"
DEFAULT_FPS = 30
DEFAULT_VIDEO_BITRATE = "4500k"
DEFAULT_AUDIO_BITRATE = "192k"

# Voces neuronales disponibles en Edge-TTS (gratuitas y ultra-realistas)
VOICES = {
    # Español
    "es-MX-Dalia": "es-MX-DaliaNeural",          # Femenina mexicana (natural, dinámica)
    "es-MX-Jorge": "es-MX-JorgeNeural",          # Masculina mexicana (enérgica)
    "es-ES-Alvaro": "es-ES-AlvaroNeural",        # Masculina española (documental/serio)
    "es-ES-Elvira": "es-ES-ElviraNeural",        # Femenina española (clara)
    "es-CO-Gonzalo": "es-CO-GonzaloNeural",      # Masculina colombiana (cálida)
    # Inglés (Alta conversión y RPM en USA / Global)
    "en-US-Christopher": "en-US-ChristopherNeural", # Masculina profunda (estilo documental National Geographic)
    "en-US-Guy": "en-US-GuyNeural",                 # Masculina conversacional viral
    "en-US-Jenny": "en-US-JennyNeural",             # Femenina profesional
    "en-US-Aria": "en-US-AriaNeural"                # Femenina enérgica
}

DEFAULT_VOICE = VOICES["es-MX-Jorge"]

# Configuración de Subtítulos (.ass)
SUBTITLE_CONFIG = {
    "font_name": "Arial",
    "font_size": 42,                             # Tamaño de fuente
    "primary_color": "&H0000FFFF",              # Amarillo brillante en ASS (&HAABBGGRR)
    "secondary_color": "&H00FFFFFF",            # Blanco
    "outline_color": "&H00000000",              # Negro
    "back_color": "&H80000000",                 # Sombra semi-transparente
    "outline_width": 3,
    "shadow_depth": 2,
    "margin_v": 280                             # Distancia desde la parte inferior
}

# Claves de API oficiales configuradas
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY", "qbp4umsXdbrpdEUx2NgVdlCudGEhtJ7rXgZZ5Uql2Euo0S1y5LxpQ4zm")
PIXABAY_API_KEY = os.environ.get("PIXABAY_API_KEY", "57182356-903be23968c4863c98e1f2f78")
GIPHY_API_KEY = os.environ.get("GIPHY_API_KEY", "")

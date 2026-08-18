# 🎬 Curiosities — Automated Video Production & Publishing Engine 🚀

Un motor completamente autónomo diseñado para crear videos cortos de curiosidades científicas e históricas en **formato vertical 1080x1920 (9:16)** para **YouTube Shorts, TikTok, Instagram Reels y Facebook Reels**, con publicación automática en la nube mediante **GitHub Actions**.

---

## 🌟 Características Principales

* 🧠 **Ganchos Dinámicos Virales (*Intro Hooks*):** Ningún video empieza igual; se selecciona aleatoriamente una apertura adaptada al tema.
* 🎙️ **Locución Neuronal Ultra-Realista:** Voces de estudio en español (`es-MX-JorgeNeural`) e inglés (`en-US-ChristopherNeural` estilo documental National Geographic).
* 📹 **Clips 4K Reales sin Falsos Positivos:** Integración oficial con Pexels 4K, Pixabay HD y TikTok con filtrado semántico estricto.
* 🎵 **Audio Pro & SFX:** Efectos de sonido *Whoosh* cinemáticos de transición a -16 dB y banda sonora ambiental con *Audio Ducking* inteligente.
* ✨ **Estilo Viral Minimalista:** Sellos `#01` a `#05` animados que desaparecen a los 1.8 segundos, barra superior de 4px y subtítulos dinámicos palabra por palabra.
* 🔥 **Call To Action (CTA):** Cierre interactivo para maximizar *likes*, comentarios y suscriptores.
* ☁️ **100% Piloto Automático en GitHub Actions:** Se ejecuta 2 veces al día en la nube y sube automáticamente los videos a Facebook Reels.

---

## 🛠️ Cómo Subir este Proyecto a GitHub (`Curiosities`)

### Paso 1: Inicializar Git y Crear el Repositorio
En tu terminal (dentro de la carpeta del proyecto):

```bash
git init
git add .
git commit -m "feat: initial release of Curiosities engine with GitHub Actions"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/Curiosities.git
git push -u origin main
```

---

### Paso 2: Configurar los Secretos en GitHub (*GitHub Secrets*)

Para que GitHub Actions pueda renderizar y publicar tus videos en la nube, añade estas 4 variables en tu repositorio de GitHub:

1. Entra a tu repositorio en GitHub: `https://github.com/TU_USUARIO/Curiosities`
2. Ve a **Settings** -> **Secrets and variables** -> **Actions** -> **New repository secret**.
3. Añade los siguientes secretos:

| Nombre del Secreto | Descripción | ¿Es Obligatorio? |
| :--- | :--- | :---: |
| `PEXELS_API_KEY` | Tu API Key oficial de Pexels | **Sí** (para descargar clips 4K) |
| `PIXABAY_API_KEY` | Tu API Key oficial de Pixabay | **Sí** (para clips de respaldo) |
| `FACEBOOK_PAGE_ID` | El ID numérico de tu Página de Facebook | Opcional (si vas a auto-publicar) |
| `FACEBOOK_ACCESS_TOKEN` | Tu Token de acceso de Página de Meta Graph API | Opcional (si vas a auto-publicar) |

---

## ⏰ Programación Automática (*Cron Schedule*)

El archivo [`.github/workflows/auto_publish.yml`](.github/workflows/auto_publish.yml) está configurado para ejecutarse **2 veces al día**:
* **14:00 UTC** (9:00 AM hora de Colombia/México/Perú)
* **21:00 UTC** (4:00 PM hora de Colombia/México/Perú)

> También puedes ejecutarlo en cualquier momento manualmente entrando a la pestaña **Actions** en GitHub y pulsando el botón **"Run workflow"**.

---

## 💻 Ejecución Local en tu Computadora

Si deseas generar videos localmente en tu equipo:

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Generar video en Inglés (National Geographic Voice)
python main.py --topic egypt --voice en-US-ChristopherNeural --aspect vertical
python main.py --topic ocean --voice en-US-ChristopherNeural --aspect vertical

# 3. Generar video en Español
python main.py --topic humano --voice es-MX-JorgeNeural --aspect vertical
python main.py --topic espacio --voice es-MX-JorgeNeural --aspect vertical
```

---

## 📂 Estructura del Proyecto

```text
Curiosities/
├── .github/
│   └── workflows/
│       └── auto_publish.yml        # Flujo de trabajo automático de GitHub Actions
├── uploader/
│   └── facebook_uploader.py        # Módulo de subida a Facebook Reels vía Meta Graph API
├── core/
│   ├── audio_sfx_engine.py         # Sintetizador de SFX Whoosh y banda sonora ambiental
│   ├── script_engine.py            # Guiones con ganchos dinámicos virales y CTA
│   ├── subtitle_engine.py          # Subtítulos dinámicos (.ass) con estilo minimalista
│   ├── video_composer.py           # Compositor FFmpeg a 30 FPS CFR + faststart
│   └── voice_engine.py             # Generador de voz Edge-TTS con detección de palabras
├── fetchers/
│   ├── media_manager.py            # Gestor multi-plataforma con filtro semántico estricto
│   ├── pexels_fetcher.py           # API oficial de Pexels 4K
│   └── pixabay_fetcher.py          # API oficial de Pixabay HD
├── auto_pipeline.py                # Runner maestro para ejecución desatendida
├── main.py                         # CLI principal de generación
├── config.py                       # Configuración y claves de API
├── requirements.txt                # Dependencias de Python
└── .gitignore                      # Archivos excluidos de Git
```

---

## 📜 Licencia
Proyecto creado para la producción y automatización de canales de contenido educativo y de curiosidades.

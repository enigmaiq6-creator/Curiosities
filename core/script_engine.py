import random
import re
from typing import List, Dict, Any

HOOKS_EN = [
    "Did you know these five unbelievable facts about {topic}?",
    "Here are five mind-blowing secrets about {topic} that will shock you!",
    "You won't believe these five crazy truths about {topic}!",
    "Scientists were stunned to discover these five facts about {topic}!",
    "Think you know everything about {topic}? These five secrets will blow your mind!"
]

HOOKS_ES = [
    "¿Sabías estos cinco datos increíbles sobre {topic}?",
    "Aquí tienes cinco secretos fascinantes sobre {topic} que te dejarán sin palabras.",
    "¡No vas a creer estos cinco datos asombrosos sobre {topic}!",
    "Los científicos quedaron impactados al descubrir estas cinco verdades sobre {topic}.",
    "¿Crees saber todo sobre {topic}? Estas cinco curiosidades te van a volar la cabeza."
]

class ScriptEngine:
    @staticmethod
    def get_dynamic_hook(topic_name: str, lang: str = "es") -> str:
        """Devuelve un gancho inicial viral aleatorio y adaptado al tema y al idioma."""
        pool = HOOKS_EN if lang == "en" else HOOKS_ES
        template = random.choice(pool)
        return template.format(topic=topic_name)

    @staticmethod
    def parse_curiosity_script(raw_text: str) -> List[Dict[str, Any]]:
        """Divide un texto de curiosidades en escenas individuales e infiere palabras clave."""
        lines = [l.strip() for l in raw_text.strip().split("\n") if l.strip()]
        scenes = []
        
        for i, line in enumerate(lines):
            clean_line = re.sub(r'^(?:Curiosidad\s*\d+:?|\d+[\.\-\)]|\-)\s*', '', line, flags=re.IGNORECASE).strip()
            if not clean_line:
                continue

            words = re.findall(r'\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]{4,}\b', clean_line)
            stopwords = {"este", "esta", "estos", "estas", "para", "como", "pero", "porque", "cuando", "donde", "sobre", "entre", "hacer", "tener", "saber", "puede", "pueden", "sabias", "sabías", "sabiasque", "numero", "número"}
            keywords = [w for w in words if w.lower() not in stopwords]
            
            main_subject = keywords[0].lower() if keywords else "curiosidad"

            scenes.append({
                "scene_id": i + 1,
                "text": clean_line,
                "subject": main_subject,
                "keywords": keywords[:3] if keywords else ["curiosidades", "ciencia"]
            })

        return scenes

    @staticmethod
    def create_sample_script(topic: str = "egypt") -> List[Dict[str, Any]]:
        """
        Crea guiones enriquecidos con:
        1. Gancho inicial dinámico y variado (Intro Hook).
        2. 5 Curiosidades científicas / históricas de impacto.
        3. Call To Action (CTA) al final.
        """
        t = topic.lower()

        # ---------------------------------------------------------
        # TEMA: ANCIENT EGYPT & THE PYRAMIDS (ENGLISH)
        # ---------------------------------------------------------
        if "egypt" in t or "pyramid" in t:
            hook_text = ScriptEngine.get_dynamic_hook("Ancient Egypt and the Great Pyramids", lang="en")
            return [
                # INTRO HOOK (Dinámico y diferente en cada video)
                {
                    "scene_id": 1,
                    "is_hook": True,
                    "text": hook_text,
                    "subject": "pyramid",
                    "keywords": ["great pyramids of giza 4k cinematic", "ancient egypt desert landscape 4k", "pyramids egypt"]
                },
                # 1. White Polished Limestone Casing
                {
                    "scene_id": 2,
                    "curiosity_index": 1,
                    "text": "Number one: The Great Pyramid was originally covered in polished white limestone that shone like a giant jewel in the desert sun.",
                    "subject": "pyramid",
                    "keywords": ["pyramids of giza glowing sun 4k", "white limestone ancient egypt", "great pyramid"]
                },
                {
                    "scene_id": 3,
                    "curiosity_index": 1,
                    "text": "It reflected sunlight so intensely that it could be seen from miles away and even from the mountains of Israel.",
                    "subject": "pyramid",
                    "keywords": ["ancient pyramids aerial view 4k", "giza pyramid complex desert", "egyptian monuments"]
                },
                # 2. Respected Builders, Not Slaves
                {
                    "scene_id": 4,
                    "curiosity_index": 2,
                    "text": "Number two: The pyramids were not built by slaves, but by respected and well-fed Egyptian craftsmen.",
                    "subject": "pharaoh",
                    "keywords": ["ancient egyptian hieroglyphics wall 4k", "egyptian temple carving stone", "ancient egypt art"]
                },
                {
                    "scene_id": 5,
                    "curiosity_index": 2,
                    "text": "Archaeological records show workers were paid with meat, medical care, and daily rations of nutritious beer.",
                    "subject": "pharaoh",
                    "keywords": ["ancient egyptian statues museum 4k", "egyptian pharaoh gold relic", "ancient craftsmen"]
                },
                # 3. 3,000-Year-Old Edible Honey
                {
                    "scene_id": 6,
                    "curiosity_index": 3,
                    "text": "Number three: Honey found sealed inside ancient Egyptian tombs over three thousand years ago is still perfectly edible today.",
                    "subject": "honey",
                    "keywords": ["golden honey dripping jar 4k", "honeycomb organic golden honey", "miel dorada"]
                },
                {
                    "scene_id": 7,
                    "curiosity_index": 3,
                    "text": "Its lack of moisture and natural acidity prevents bacteria from ever growing, making honey truly immortal.",
                    "subject": "honey",
                    "keywords": ["golden honey macro close up 4k", "ancient jar relic gold", "pure honey"]
                },
                # 4. Alignment with True North
                {
                    "scene_id": 8,
                    "curiosity_index": 4,
                    "text": "Number four: The Great Pyramid aligns with True North with an error of just five hundredths of a degree.",
                    "subject": "pyramid",
                    "keywords": ["pyramids starry night sky cosmos 4k", "constellation orion pyramids alignment", "giza night stars"]
                },
                {
                    "scene_id": 9,
                    "curiosity_index": 4,
                    "text": "That is higher architectural precision than the Greenwich Royal Observatory built thousands of years later.",
                    "subject": "pyramid",
                    "keywords": ["great pyramid astronomy stars 4k", "egyptian night sky galaxy", "ancient pyramid cosmos"]
                },
                # 5. Cleopatra and the Moon Landing
                {
                    "scene_id": 10,
                    "curiosity_index": 5,
                    "text": "Number five: Cleopatra lived closer in time to the Moon Landing and the iPhone than to the construction of the Great Pyramids.",
                    "subject": "pharaoh",
                    "keywords": ["cleopatra statue golden ancient egypt 4k", "golden pharaoh mask tutankhamun 4k", "cleopatra gold"]
                },
                {
                    "scene_id": 11,
                    "curiosity_index": 5,
                    "text": "Over two thousand five hundred years separated the building of Giza from the reign of Egypt's last queen.",
                    "subject": "pharaoh",
                    "keywords": ["ancient egyptian golden artifacts 4k", "luxor temple columns egypt 4k", "pharaoh treasures"]
                },
                # 6. CALL TO ACTION (CTA)
                {
                    "scene_id": 12,
                    "is_cta": True,
                    "text": "Which of these ancient secrets surprised you the most? Drop a comment, hit like, and follow for more mind-blowing history!",
                    "subject": "pyramid",
                    "keywords": ["majestic pyramids sunset desert 4k", "ancient egypt golden sphinx 4k", "pyramids of giza"]
                }
            ]

        # ---------------------------------------------------------
        # TEMA: DEEP OCEAN MYSTERIES (ENGLISH)
        # ---------------------------------------------------------
        elif "ocean" in t or "abyss" in t or "deep" in t:
            hook_text = ScriptEngine.get_dynamic_hook("the Mysterious Deep Ocean", lang="en")
            return [
                {
                    "scene_id": 1,
                    "is_hook": True,
                    "text": hook_text,
                    "subject": "jellyfish",
                    "keywords": ["deep ocean underwater abyss 4k", "glowing ocean creatures dark", "deep sea exploration"]
                },
                {
                    "scene_id": 2,
                    "curiosity_index": 1,
                    "text": "Number one: Over eighty percent of all creatures living in the midnight zone produce their own living light.",
                    "subject": "jellyfish",
                    "keywords": ["bioluminescent jellyfish glowing deep ocean", "glowing underwater creatures 4k", "jellyfish dark ocean"]
                },
                {
                    "scene_id": 3,
                    "curiosity_index": 1,
                    "text": "They use glowing chemical reactions to attract prey, communicate, and blind predators in total darkness.",
                    "subject": "jellyfish",
                    "keywords": ["deep sea bioluminescence glowing 4k", "bioluminescent sea creatures", "glowing jellyfish"]
                },
                {
                    "scene_id": 4,
                    "curiosity_index": 2,
                    "text": "Number two: The Greenland shark is the longest-living vertebrate on Earth, surviving for over four hundred years.",
                    "subject": "shark",
                    "keywords": ["greenland shark swimming deep ocean", "ancient shark arctic ocean underwater", "deep sea shark 4k"]
                },
                {
                    "scene_id": 5,
                    "curiosity_index": 2,
                    "text": "Some sharks swimming in the Arctic depths today were already alive during the time of the Renaissance.",
                    "subject": "shark",
                    "keywords": ["giant shark deep cold ocean", "arctic sea shark underwater 4k", "shark deep water"]
                },
                {
                    "scene_id": 6,
                    "curiosity_index": 3,
                    "text": "Number three: At the bottom of the Mariana Trench, the water pressure is over one thousand times greater than at sea level.",
                    "subject": "submarine",
                    "keywords": ["deep sea submarine abyss exploration", "deep ocean submersible rover 4k", "mariana trench submarine"]
                },
                {
                    "scene_id": 7,
                    "curiosity_index": 3,
                    "text": "That is equivalent to having the weight of fifty jumbo jets pressing down on your entire body at once.",
                    "subject": "submarine",
                    "keywords": ["deep ocean seabed submersible lights", "abyss ocean exploration 4k", "submersible deep sea"]
                },
                {
                    "scene_id": 8,
                    "curiosity_index": 4,
                    "text": "Number four: There are actual rivers and lakes flowing along the very bottom of the ocean.",
                    "subject": "submarine",
                    "keywords": ["underwater brine pool deep ocean lake", "deep sea seabed landscape 4k", "underwater river abyss"]
                },
                {
                    "scene_id": 9,
                    "curiosity_index": 4,
                    "text": "These dense underwater brine pools have distinct shorelines and waves, completely separate from the surrounding seawater.",
                    "subject": "submarine",
                    "keywords": ["deep ocean floor exploration 4k", "mysterious underwater abyss landscape", "deep seabed lights"]
                },
                {
                    "scene_id": 10,
                    "curiosity_index": 5,
                    "text": "Number five: The colossal squid possesses the largest eyes in the animal kingdom, as big as basketballs.",
                    "subject": "squid",
                    "keywords": ["giant squid swimming deep ocean", "colossal squid underwater creature 3d", "squid deep sea 4k"]
                },
                {
                    "scene_id": 11,
                    "curiosity_index": 5,
                    "text": "These massive lenses allow them to detect faint shadows and glowing bioluminescence from hundreds of meters away.",
                    "subject": "squid",
                    "keywords": ["deep sea giant squid tentacle 4k", "bioluminescent squid deep ocean", "colossal squid"]
                },
                {
                    "scene_id": 12,
                    "is_cta": True,
                    "text": "Which of these deep sea mysteries amazed you the most? Drop a comment, hit like, and follow for more mind-blowing discoveries!",
                    "subject": "jellyfish",
                    "keywords": ["deep sea glowing creatures abyss 4k", "bioluminescent jellyfish dark ocean", "deep ocean"]
                }
            ]

        # ---------------------------------------------------------
        # TEMA: EL INCREÍBLE CUERPO HUMANO (ESPAÑOL)
        # ---------------------------------------------------------
        elif "humano" in t or "cuerpo" in t:
            hook_text = ScriptEngine.get_dynamic_hook("el Asombroso Cuerpo Humano", lang="es")
            return [
                {
                    "scene_id": 1,
                    "is_hook": True,
                    "text": hook_text,
                    "subject": "brain",
                    "keywords": ["human anatomy body digital 4k", "human brain glowing 3d", "cuerpo humano 4k"]
                },
                {
                    "scene_id": 2,
                    "curiosity_index": 1,
                    "text": "Número uno: Tu cerebro despierto genera suficiente electricidad como para encender una bombilla LED.",
                    "subject": "brain",
                    "keywords": ["human brain glowing neurons 3d", "brain electrical synapses", "cerebro humano"]
                },
                {
                    "scene_id": 3,
                    "curiosity_index": 1,
                    "text": "Contiene más de ochenta y seis mil millones de neuronas que transmiten información a más de cuatrocientos kilómetros por hora.",
                    "subject": "brain",
                    "keywords": ["neuron firing brain cell", "brain neural network 4k", "neuronas"]
                },
                {
                    "scene_id": 4,
                    "curiosity_index": 2,
                    "text": "Número dos: Tus huesos son proporcionalmente más resistentes que el acero macizo.",
                    "subject": "bone",
                    "keywords": ["human skeleton bones 3d", "femur bone strength human", "huesos esqueleto"]
                },
                {
                    "scene_id": 5,
                    "curiosity_index": 2,
                    "text": "Un solo centímetro cúbico de hueso puede soportar una carga de hasta nueve toneladas de peso sin romperse.",
                    "subject": "bone",
                    "keywords": ["skeleton human anatomy 3d", "human bones structure", "esqueleto 3d"]
                },
                {
                    "scene_id": 6,
                    "curiosity_index": 3,
                    "text": "Número tres: El ácido de tu estómago es tan potente que podría disolver hojas de afeitar de acero.",
                    "subject": "acid",
                    "keywords": ["chemical liquid acid bubbling", "digestive stomach acid 3d", "liquido acido"]
                },
                {
                    "scene_id": 7,
                    "curiosity_index": 3,
                    "text": "Para evitar autodestruirse, las paredes internas de tu estómago renuevan su mucosa celular cada cuatro días.",
                    "subject": "acid",
                    "keywords": ["human cells multiplying microscope", "cells regeneration biology", "celulas"]
                },
                {
                    "scene_id": 8,
                    "curiosity_index": 4,
                    "text": "Número cuatro: Si desenrollaras todo el ADN de tus células, llegaría desde la Tierra hasta el planeta Plutón.",
                    "subject": "dna",
                    "keywords": ["dna helix spinning 3d 4k", "glowing dna strand science", "adn humano"]
                },
                {
                    "scene_id": 9,
                    "curiosity_index": 4,
                    "text": "En total son más de diez mil millones de kilómetros de código genético comprimidos en tu cuerpo.",
                    "subject": "dna",
                    "keywords": ["dna sequence genetics 3d", "microscopic dna biology", "cadena de adn"]
                },
                {
                    "scene_id": 10,
                    "curiosity_index": 5,
                    "text": "Número cinco: Si unieras todos los vasos sanguíneos de tu cuerpo, darían dos vueltas y media al planeta Tierra.",
                    "subject": "heart",
                    "keywords": ["human blood vessels circulation 3d", "beating heart blood flow", "sistema circulatorio"]
                },
                {
                    "scene_id": 11,
                    "curiosity_index": 5,
                    "text": "Son más de cien mil kilómetros de arterias y capilares que transportan oxígeno a cada rincón de tu organismo.",
                    "subject": "heart",
                    "keywords": ["red blood cells flowing vein 4k", "blood circulation heart 3d", "globulos rojos"]
                },
                {
                    "scene_id": 12,
                    "is_cta": True,
                    "text": "¿Cuál de estos datos te sorprendió más? ¡Dale like, comenta cuál fue tu favorito y síguenos para más curiosidades increíbles!",
                    "subject": "brain",
                    "keywords": ["human brain futuristic technology", "digital brain thinking 4k", "mente humana"]
                }
            ]

        # ---------------------------------------------------------
        # TEMA: MISTERIOS DEL ESPACIO PROFUNDO (ESPAÑOL)
        # ---------------------------------------------------------
        else:
            hook_text = ScriptEngine.get_dynamic_hook("el Espacio Profundo y el Universo", lang="es")
            return [
                {
                    "scene_id": 1,
                    "is_hook": True,
                    "text": hook_text,
                    "subject": "astronaut",
                    "keywords": ["universe galaxy cosmos deep space 4k", "planet earth space view 4k", "espacio universo"]
                },
                {
                    "scene_id": 2,
                    "curiosity_index": 1,
                    "text": "Número uno: Un día en el planeta Venus dura más que un año entero en la Tierra.",
                    "subject": "venus",
                    "keywords": ["planet venus rotating", "venus 3d space", "planeta venus"]
                },
                {
                    "scene_id": 3,
                    "curiosity_index": 1,
                    "text": "Su atmósfera tiene densas nubes de ácido sulfúrico con temperaturas de cuatrocientos setenta y cinco grados.",
                    "subject": "venus",
                    "keywords": ["venus atmosphere", "burning hot planet surface", "venus surface"]
                },
                {
                    "scene_id": 4,
                    "curiosity_index": 2,
                    "text": "Número dos: En el vacío del espacio reina el silencio más absoluto que puedas imaginar.",
                    "subject": "astronaut",
                    "keywords": ["astronaut floating space", "spacewalk earth", "astronauta en el espacio"]
                },
                {
                    "scene_id": 5,
                    "curiosity_index": 2,
                    "text": "Al no existir aire, incluso si una gigantesca supernova explota a tu lado, no escucharías absolutamente nada.",
                    "subject": "supernova",
                    "keywords": ["supernova explosion space", "exploding star supernova", "supernova"]
                },
                {
                    "scene_id": 6,
                    "curiosity_index": 3,
                    "text": "Número tres: Las huellas de los astronautas del Apolo en la Luna durarán más de cien millones de años.",
                    "subject": "moon",
                    "keywords": ["apollo moon footprint", "astronaut moon walking", "huella en la luna"]
                },
                {
                    "scene_id": 7,
                    "curiosity_index": 3,
                    "text": "Esto se debe a que la Luna no tiene atmósfera, por lo que no hay viento ni lluvia que borre el polvo.",
                    "subject": "moon",
                    "keywords": ["moon craters surface", "lunar orbit space", "superficie luna"]
                },
                {
                    "scene_id": 8,
                    "curiosity_index": 4,
                    "text": "Número cuatro: En los gigantes helados Neptuno y Urano llueven diamantes reales.",
                    "subject": "neptune",
                    "keywords": ["neptune planet 3d", "planet neptune space", "planeta neptuno"]
                },
                {
                    "scene_id": 9,
                    "curiosity_index": 4,
                    "text": "La presión extrema comprime el gas metano convirtiéndolo en cristales de carbono puro que caen hacia su núcleo.",
                    "subject": "diamond",
                    "keywords": ["sparkling diamonds falling", "diamonds crystals close up", "diamantes brillantes"]
                },
                {
                    "scene_id": 10,
                    "curiosity_index": 5,
                    "text": "Número cinco: El Sol es tan descomunal que en su interior cabrían más de un millón trescientas mil Tierras.",
                    "subject": "sun",
                    "keywords": ["sun solar flare space", "giant burning sun", "sol llamaradas"]
                },
                {
                    "scene_id": 11,
                    "curiosity_index": 5,
                    "text": "En su núcleo, la fusión nuclear genera temperaturas de quince millones de grados Celsius.",
                    "subject": "sun",
                    "keywords": ["sun surface plasma", "solar corona glowing", "sol plasma"]
                },
                {
                    "scene_id": 12,
                    "is_cta": True,
                    "text": "¿Qué misterio del cosmos te fascina más? ¡Comenta, dale like y síguenos para seguir explorando el universo!",
                    "subject": "astronaut",
                    "keywords": ["astronaut looking at galaxy", "galaxy cosmos stars", "espacio"]
                }
            ]

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
        Crea guiones 100% en INGLÉS enriquecidos con:
        1. Gancho inicial dinámico y variado (Intro Hook).
        2. 5 Curiosidades científicas / históricas de impacto.
        3. Call To Action (CTA) al final.
        """
        t = topic.lower()

        # ---------------------------------------------------------
        # 1. TEMA: ANCIENT EGYPT & THE PYRAMIDS (ENGLISH)
        # ---------------------------------------------------------
        if "egypt" in t or "pyramid" in t:
            hook_text = ScriptEngine.get_dynamic_hook("Ancient Egypt and the Great Pyramids", lang="en")
            return [
                {
                    "scene_id": 1,
                    "is_hook": True,
                    "text": hook_text,
                    "subject": "pyramid",
                    "keywords": ["great pyramids of giza 4k cinematic", "ancient egypt desert landscape 4k", "pyramids egypt"]
                },
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
                {
                    "scene_id": 12,
                    "is_cta": True,
                    "text": "Which of these ancient secrets surprised you the most? Drop a comment, hit like, and follow for more mind-blowing history!",
                    "subject": "pyramid",
                    "keywords": ["majestic pyramids sunset desert 4k", "ancient egypt golden sphinx 4k", "pyramids of giza"]
                }
            ]

        # ---------------------------------------------------------
        # 2. TEMA: DEEP OCEAN MYSTERIES (ENGLISH)
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
        # 3. TEMA: DEEP SPACE & THE UNIVERSE (ENGLISH)
        # ---------------------------------------------------------
        elif "space" in t or "espacio" in t or "universe" in t or "cosmos" in t:
            hook_text = ScriptEngine.get_dynamic_hook("Deep Space and the Universe", lang="en")
            return [
                {
                    "scene_id": 1,
                    "is_hook": True,
                    "text": hook_text,
                    "subject": "supernova",
                    "keywords": ["deep space nebula galaxy 4k", "universe stars cosmos cinematic 4k", "space galaxy"]
                },
                {
                    "scene_id": 2,
                    "curiosity_index": 1,
                    "text": "Number one: One day on Venus lasts longer than an entire year on Venus.",
                    "subject": "venus",
                    "keywords": ["planet venus rotating solar system 4k", "venus atmosphere planet space", "planet venus"]
                },
                {
                    "scene_id": 3,
                    "curiosity_index": 1,
                    "text": "It takes Venus two hundred and forty-three Earth days to rotate once, but only two hundred and twenty-five days to orbit the Sun.",
                    "subject": "venus",
                    "keywords": ["solar system planets orbit sun 4k", "planet venus glowing space", "orbit solar system"]
                },
                {
                    "scene_id": 4,
                    "curiosity_index": 2,
                    "text": "Number two: Footprints left by Apollo astronauts on the Moon will remain untouched for at least one hundred million years.",
                    "subject": "moon",
                    "keywords": ["apollo astronaut walking moon surface 4k", "moon surface crater lunar landscape", "astronaut moon"]
                },
                {
                    "scene_id": 5,
                    "curiosity_index": 2,
                    "text": "Because the Moon has no atmosphere, there is zero wind, rain, or erosion to ever erase them.",
                    "subject": "moon",
                    "keywords": ["moon crater lunar surface close up 4k", "earth rising over moon space", "lunar surface"]
                },
                {
                    "scene_id": 6,
                    "curiosity_index": 3,
                    "text": "Number three: It literally rains solid diamonds on Neptune and Uranus.",
                    "subject": "diamond",
                    "keywords": ["planet neptune deep blue space 4k", "sparkling crystals diamond glowing", "planet uranus space"]
                },
                {
                    "scene_id": 7,
                    "curiosity_index": 3,
                    "text": "Extreme atmospheric pressures crush methane into solid diamond hailstones that sink straight to the planetary core.",
                    "subject": "diamond",
                    "keywords": ["sparkling diamond rain crystal 4k", "planet neptune atmosphere clouds", "diamond crystal"]
                },
                {
                    "scene_id": 8,
                    "curiosity_index": 4,
                    "text": "Number four: The Sun accounts for ninety-nine point eighty-six percent of all mass in our entire Solar System.",
                    "subject": "sun",
                    "keywords": ["sun solar flare plasma surface 4k", "massive glowing sun space 4k", "sun corona solar system"]
                },
                {
                    "scene_id": 9,
                    "curiosity_index": 4,
                    "text": "Over one million three hundred thousand Earths could easily fit inside the Sun.",
                    "subject": "sun",
                    "keywords": ["solar system sun planets comparison 4k", "sun rays space cinematic", "sun flare"]
                },
                {
                    "scene_id": 10,
                    "curiosity_index": 5,
                    "text": "Number five: Space is completely, utterly silent.",
                    "subject": "supernova",
                    "keywords": ["astronaut floating silent deep space 4k", "milky way galaxy stars silent cosmos", "space silence"]
                },
                {
                    "scene_id": 11,
                    "curiosity_index": 5,
                    "text": "Sound waves require matter to travel through, and in the vacuum of space, even massive supernovae explode in absolute silence.",
                    "subject": "supernova",
                    "keywords": ["supernova explosion colorful nebula 4k", "deep space galaxy expanding cosmos", "supernova nebula"]
                },
                {
                    "scene_id": 12,
                    "is_cta": True,
                    "text": "Which cosmic mystery shocked you the most? Drop a comment, hit like, and follow for daily universe wonders!",
                    "subject": "supernova",
                    "keywords": ["colorful glowing galaxy cosmos 4k", "deep space nebula stars", "universe stars"]
                }
            ]

        # ---------------------------------------------------------
        # 4. TEMA: THE AMAZING HUMAN BODY (ENGLISH)
        # ---------------------------------------------------------
        elif "human" in t or "humano" in t or "body" in t or "cuerpo" in t:
            hook_text = ScriptEngine.get_dynamic_hook("the Human Body", lang="en")
            return [
                {
                    "scene_id": 1,
                    "is_hook": True,
                    "text": hook_text,
                    "subject": "brain",
                    "keywords": ["human brain glowing neurons neural network 4k", "human body anatomy medical 4k", "brain synapse"]
                },
                {
                    "scene_id": 2,
                    "curiosity_index": 1,
                    "text": "Number one: The human brain generates enough electricity to power a small LED lightbulb.",
                    "subject": "brain",
                    "keywords": ["neurons firing electrical synapse brain 4k", "glowing neural brain activity", "brain electrical"]
                },
                {
                    "scene_id": 3,
                    "curiosity_index": 1,
                    "text": "With over eighty-six billion neurons, your brain processes more computations per second than the most powerful supercomputer.",
                    "subject": "brain",
                    "keywords": ["neural network human brain thinking 4k", "futuristic neural brain concept", "brain network"]
                },
                {
                    "scene_id": 4,
                    "curiosity_index": 2,
                    "text": "Number two: Human bone is ounce for ounce four times stronger than concrete.",
                    "subject": "bone",
                    "keywords": ["human skeleton anatomy medical bone 4k", "bone structure microscopic 4k", "skeleton bone"]
                },
                {
                    "scene_id": 5,
                    "curiosity_index": 2,
                    "text": "A single cubic inch of human bone can withstand a load of over nineteen thousand pounds without breaking.",
                    "subject": "bone",
                    "keywords": ["human spine femur bone anatomy 4k", "medical bone scan 3d", "bone anatomy"]
                },
                {
                    "scene_id": 6,
                    "curiosity_index": 3,
                    "text": "Number three: Your stomach acid is powerful enough to dissolve razor blades and stainless steel.",
                    "subject": "acid",
                    "keywords": ["chemical acid reaction liquid laboratory 4k", "stomach digestive system anatomy 4k", "acid liquid"]
                },
                {
                    "scene_id": 7,
                    "curiosity_index": 3,
                    "text": "To protect itself from self-destruction, your stomach completely regenerates its inner lining every four days.",
                    "subject": "acid",
                    "keywords": ["cells dividing biological regeneration 4k", "microscopic cellular biology", "cells division"]
                },
                {
                    "scene_id": 8,
                    "curiosity_index": 4,
                    "text": "Number four: If you unraveled all the DNA in your body, it would stretch to Pluto and back twice.",
                    "subject": "dna",
                    "keywords": ["dna double helix rotating glowing 4k", "genetics dna strand molecular biology", "dna helix"]
                },
                {
                    "scene_id": 9,
                    "curiosity_index": 4,
                    "text": "That is over thirty-four billion miles of genetic code packed inside microscopic cells.",
                    "subject": "dna",
                    "keywords": ["dna sequence genetic molecular 4k", "microscopic cells dna glowing", "genetics code"]
                },
                {
                    "scene_id": 10,
                    "curiosity_index": 5,
                    "text": "Number five: Your heart beats over one hundred thousand times every single day.",
                    "subject": "heart",
                    "keywords": ["human heart beating 3d medical animation 4k", "cardiovascular blood vessels glowing", "heart beating"]
                },
                {
                    "scene_id": 11,
                    "curiosity_index": 5,
                    "text": "In an average lifetime, it pumps enough blood to fill three entire supertanker ships.",
                    "subject": "heart",
                    "keywords": ["red blood cells flowing artery 4k", "cardiovascular bloodstream medical", "blood flow"]
                },
                {
                    "scene_id": 12,
                    "is_cta": True,
                    "text": "Which human superpower surprised you the most? Drop a comment, hit like, and follow for more mind-blowing science!",
                    "subject": "brain",
                    "keywords": ["glowing neural brain network 4k", "human body medical animation", "brain neurons"]
                }
            ]

        # ---------------------------------------------------------
        # 5. TEMA: ANIMALS WITH SUPERPOWERS (ENGLISH)
        # ---------------------------------------------------------
        elif "animal" in t or "komodo" in t:
            hook_text = ScriptEngine.get_dynamic_hook("Animals with Real Superpowers", lang="en")
            return [
                {
                    "scene_id": 1,
                    "is_hook": True,
                    "text": hook_text,
                    "subject": "komodo",
                    "keywords": ["komodo dragon walking wild 4k", "komodo dragon lizard reptile 4k", "varanus komodoensis"]
                },
                {
                    "scene_id": 2,
                    "curiosity_index": 1,
                    "text": "Number one: The Komodo dragon is equipped with armor-plated chainmail beneath its scaly skin.",
                    "subject": "komodo",
                    "keywords": ["komodo dragon close up skin scales 4k", "komodo dragon lizard crawling", "komodo dragon"]
                },
                {
                    "scene_id": 3,
                    "curiosity_index": 1,
                    "text": "These microscopic bone deposits, called osteoderms, protect them during violent battles with rival dragons.",
                    "subject": "komodo",
                    "keywords": ["komodo dragon battle island 4k", "varanus komodoensis running", "komodo reptile"]
                },
                {
                    "scene_id": 4,
                    "curiosity_index": 2,
                    "text": "Number two: Crows understand the concept of zero and can remember human faces for their entire lives.",
                    "subject": "crow",
                    "keywords": ["black crow raven perched tree 4k", "intelligent crow flying close up 4k", "corvus raven"]
                },
                {
                    "scene_id": 5,
                    "curiosity_index": 2,
                    "text": "They teach their offspring which humans are trustworthy and which ones to avoid.",
                    "subject": "crow",
                    "keywords": ["crow flock perched intelligent bird 4k", "raven eyes close up bird", "crow bird"]
                },
                {
                    "scene_id": 6,
                    "curiosity_index": 3,
                    "text": "Number three: The Axolotl can completely regenerate not just lost limbs, but its heart, lungs, and parts of its brain.",
                    "subject": "axolotl",
                    "keywords": ["axolotl swimming aquarium water 4k", "pink axolotl salamander close up", "axolotl gills"]
                },
                {
                    "scene_id": 7,
                    "curiosity_index": 3,
                    "text": "Scientists are actively studying their genetic code to unlock tissue regeneration in human medicine.",
                    "subject": "axolotl",
                    "keywords": ["axolotl pink underwater swimming 4k", "mexican salamander axolotl", "axolotl"]
                },
                {
                    "scene_id": 8,
                    "curiosity_index": 4,
                    "text": "Number four: Hummingbirds are the only birds on Earth capable of flying backwards and upside down.",
                    "subject": "hummingbird",
                    "keywords": ["hummingbird hovering flower slow motion 4k", "colorful hummingbird wings flapping", "hummingbird slowmo"]
                },
                {
                    "scene_id": 9,
                    "curiosity_index": 4,
                    "text": "Their wings flap up to eighty times per second with a heart rate exceeding one thousand two hundred beats per minute.",
                    "subject": "hummingbird",
                    "keywords": ["hummingbird drinking nectar macro 4k", "hummingbird slow motion wings", "hummingbird flower"]
                },
                {
                    "scene_id": 10,
                    "curiosity_index": 5,
                    "text": "Number five: The blue whale's tongue weighs as much as an entire adult elephant.",
                    "subject": "whale",
                    "keywords": ["blue whale swimming ocean surface 4k", "giant humpback whale breaching 4k", "blue whale ocean"]
                },
                {
                    "scene_id": 11,
                    "curiosity_index": 5,
                    "text": "A human child could easily swim through the major blood vessels of its heart.",
                    "subject": "whale",
                    "keywords": ["giant whale underwater ocean 4k", "whale tail fluke diving blue water", "whale swimming"]
                },
                {
                    "scene_id": 12,
                    "is_cta": True,
                    "text": "Which animal superpower amazed you the most? Drop a comment, hit like, and follow for more wild discoveries!",
                    "subject": "komodo",
                    "keywords": ["majestic wild animals nature 4k", "komodo dragon landscape sunset", "wild wildlife"]
                }
            ]

        # Default fallback: Ancient Egypt
        return ScriptEngine.create_sample_script("egypt")

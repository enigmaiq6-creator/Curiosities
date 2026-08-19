from typing import List, Dict, Any

# ==============================================================================
# 📚 MEGA CATÁLOGO DE TEMAS VIRALES 100% EN INGLÉS (CURIOSIDADES CIENTÍFICAS E HISTÓRICAS)
# Cada tema cuenta con 5 datos únicos, verificados, ganchos y palabras clave 4K
# ==============================================================================

TOPICS_DB: Dict[str, Dict[str, Any]] = {
    # --------------------------------------------------------------------------
    # 🌌 CATEGORÍA: ESPACIO PROFUNDO Y ASTRONOMÍA
    # --------------------------------------------------------------------------
    "black_holes": {
        "title": "5 Terrifying Secrets of Supermassive Black Holes! 🕳️🌌",
        "intro_tag": "Supermassive Black Holes in Deep Space",
        "scenes": [
            {"scene_id": 2, "curiosity_index": 1, "text": "Number one: At the center of a black hole, gravitational pull is so extreme that time comes to a complete standstill.", "subject": "supernova", "keywords": ["black hole space horizon 4k", "supermassive black hole accretion disk", "black hole"]},
            {"scene_id": 3, "curiosity_index": 1, "text": "An outside observer would see you freeze in place for all eternity as you fall toward the event horizon.", "subject": "supernova", "keywords": ["event horizon black hole warp space 4k", "black hole gravity cosmos", "black hole distortion"]},
            {"scene_id": 4, "curiosity_index": 2, "text": "Number two: The process of falling into a black hole is officially called spaghettification by astrophysicists.", "subject": "supernova", "keywords": ["stars orbiting black hole gravity 4k", "astrophysics deep space galaxy", "black hole stars"]},
            {"scene_id": 5, "curiosity_index": 2, "text": "Gravitational forces on your feet would be millions of times stronger than on your head, stretching you into a thin noodle of atoms.", "subject": "supernova", "keywords": ["galaxy core spinning black hole 4k", "cosmic gravity spacetime", "galaxy core"]},
            {"scene_id": 6, "curiosity_index": 3, "text": "Number three: The largest known black hole, TON 618, has the mass of sixty-six billion Suns.", "subject": "supernova", "keywords": ["massive quasar glowing deep universe 4k", "quasar explosion universe", "ton 618 quasar"]},
            {"scene_id": 7, "curiosity_index": 3, "text": "It shines with the brilliance of one hundred and forty trillion Suns, visible across billions of light years.", "subject": "supernova", "keywords": ["bright cosmic light galaxy center 4k", "deep universe stars nebula", "quasar bright"]},
            {"scene_id": 8, "curiosity_index": 4, "text": "Number four: If our Sun were replaced by an equal-mass black hole, Earth would not get sucked in.", "subject": "sun", "keywords": ["earth orbiting glowing sun space 4k", "solar system planetary orbit", "earth sun orbit"]},
            {"scene_id": 9, "curiosity_index": 4, "text": "Its gravitational pull at Earth's distance would remain exactly the same, though our planet would freeze in eternal darkness.", "subject": "sun", "keywords": ["frozen planet dark space 4k", "ice earth solar system", "frozen cosmos"]},
            {"scene_id": 10, "curiosity_index": 5, "text": "Number five: Supermassive black holes shoot plasma jets across entire galaxies at ninety-nine percent the speed of light.", "subject": "supernova", "keywords": ["relativistic plasma jet galaxy 4k", "black hole laser energy beam", "plasma jet cosmic"]},
            {"scene_id": 11, "curiosity_index": 5, "text": "These cosmic energy beams carve colossal cavities across intergalactic space spanning millions of light years.", "subject": "supernova", "keywords": ["deep cosmic web galaxy clusters 4k", "universe expanding cosmos", "cosmic web"]},
            {"scene_id": 12, "is_cta": True, "text": "Which cosmic secret shocked you the most? Drop a comment, hit like, and follow for daily universe wonders!", "subject": "supernova", "keywords": ["deep space nebula galaxy 4k", "universe stars cosmos cinematic 4k", "space galaxy"]}
        ]
    },

    "space": {
        "title": "5 Insane Mysteries of Deep Space & The Universe! 🌌🚀",
        "intro_tag": "Deep Space and the Universe",
        "scenes": [
            {"scene_id": 2, "curiosity_index": 1, "text": "Number one: One day on Venus lasts longer than an entire year on Venus.", "subject": "venus", "keywords": ["planet venus rotating solar system 4k", "venus atmosphere planet space", "planet venus"]},
            {"scene_id": 3, "curiosity_index": 1, "text": "It takes Venus two hundred and forty-three Earth days to rotate once, but only two hundred and twenty-five days to orbit the Sun.", "subject": "venus", "keywords": ["solar system planets orbit sun 4k", "planet venus glowing space", "orbit solar system"]},
            {"scene_id": 4, "curiosity_index": 2, "text": "Number two: Footprints left by Apollo astronauts on the Moon will remain untouched for at least one hundred million years.", "subject": "moon", "keywords": ["apollo astronaut walking moon surface 4k", "moon surface crater lunar landscape", "astronaut moon"]},
            {"scene_id": 5, "curiosity_index": 2, "text": "Because the Moon has no atmosphere, there is zero wind, rain, or erosion to ever erase them.", "subject": "moon", "keywords": ["moon crater lunar surface close up 4k", "earth rising over moon space", "lunar surface"]},
            {"scene_id": 6, "curiosity_index": 3, "text": "Number three: It literally rains solid diamonds on Neptune and Uranus.", "subject": "diamond", "keywords": ["planet neptune deep blue space 4k", "sparkling crystals diamond glowing", "planet uranus space"]},
            {"scene_id": 7, "curiosity_index": 3, "text": "Extreme atmospheric pressures crush methane into solid diamond hailstones that sink straight to the planetary core.", "subject": "diamond", "keywords": ["sparkling diamond rain crystal 4k", "planet neptune atmosphere clouds", "diamond crystal"]},
            {"scene_id": 8, "curiosity_index": 4, "text": "Number four: The Sun accounts for ninety-nine point eighty-six percent of all mass in our entire Solar System.", "subject": "sun", "keywords": ["sun solar flare plasma surface 4k", "massive glowing sun space 4k", "sun corona solar system"]},
            {"scene_id": 9, "curiosity_index": 4, "text": "Over one million three hundred thousand Earths could easily fit inside the Sun.", "subject": "sun", "keywords": ["solar system sun planets comparison 4k", "sun rays space cinematic", "sun flare"]},
            {"scene_id": 10, "curiosity_index": 5, "text": "Number five: Space is completely, utterly silent.", "subject": "supernova", "keywords": ["astronaut floating silent deep space 4k", "milky way galaxy stars silent cosmos", "space silence"]},
            {"scene_id": 11, "curiosity_index": 5, "text": "Sound waves require matter to travel through, and in the vacuum of space, even massive supernovae explode in absolute silence.", "subject": "supernova", "keywords": ["supernova explosion colorful nebula 4k", "deep space galaxy expanding cosmos", "supernova nebula"]},
            {"scene_id": 12, "is_cta": True, "text": "Which cosmic mystery shocked you the most? Drop a comment, hit like, and follow for daily universe wonders!", "subject": "supernova", "keywords": ["colorful glowing galaxy cosmos 4k", "deep space nebula stars", "universe stars"]}
        ]
    },

    "neutron_stars": {
        "title": "5 Mind-Blowing Facts About Neutron Stars & Pulsars! ⚡🌌",
        "intro_tag": "Neutron Stars and Magnetic Monsters",
        "scenes": [
            {"scene_id": 2, "curiosity_index": 1, "text": "Number one: A single sugar-cube-sized amount of neutron star matter weighs over one billion tons on Earth.", "subject": "supernova", "keywords": ["neutron star spinning magnetic 4k", "pulsar beam cosmic space 4k", "neutron star"]},
            {"scene_id": 3, "curiosity_index": 1, "text": "That is equivalent to cramming the weight of Mount Everest into a single teaspoon.", "subject": "supernova", "keywords": ["mountain everest majestic summit 4k", "rocky mountain peak aerial", "everest peak"]},
            {"scene_id": 4, "curiosity_index": 2, "text": "Number two: Some pulsars spin up to seven hundred times per second.", "subject": "supernova", "keywords": ["pulsar lighthouse beam spinning space 4k", "fast spinning star cosmos", "pulsar space"]},
            {"scene_id": 5, "curiosity_index": 2, "text": "Their surface travels at nearly a quarter of the speed of light as they emit precise radio beams across the galaxy.", "subject": "supernova", "keywords": ["radio telescope array listening cosmos 4k", "astronomy deep space signal", "radio dish space"]},
            {"scene_id": 6, "curiosity_index": 3, "text": "Number three: Magnetars possess magnetic fields one quadrillion times stronger than Earth's.", "subject": "supernova", "keywords": ["magnetar cosmic magnetic field glowing 4k", "plasma aurora space storm", "magnetar space"]},
            {"scene_id": 7, "curiosity_index": 3, "text": "If a magnetar passed within one thousand kilometers of Earth, its magnetic field would dissolve the atoms in your body instantly.", "subject": "supernova", "keywords": ["cosmic radiation storm earth space 4k", "planetary magnetic shield", "solar wind earth"]},
            {"scene_id": 8, "curiosity_index": 4, "text": "Number four: When two neutron stars collide, they forge almost all the gold and platinum in the universe.", "subject": "diamond", "keywords": ["kilonova golden collision explosion 4k", "gold nuggets sparkling molten", "kilonova space"]},
            {"scene_id": 9, "curiosity_index": 4, "text": "Every piece of gold jewelry you wear was created during a violent neutron star merger billions of years ago.", "subject": "diamond", "keywords": ["pure gold bar jewelry glowing 4k", "golden luxury sparkle", "gold jewelry"]},
            {"scene_id": 10, "curiosity_index": 5, "text": "Number five: The crust of a neutron star is ten billion times stronger than steel.", "subject": "supernova", "keywords": ["dense crystalline atomic lattice 4k", "extreme density cosmic matter", "atomic structure"]},
            {"scene_id": 11, "curiosity_index": 5, "text": "Astrophysicists refer to this super-dense material as nuclear pasta, the hardest substance in the known universe.", "subject": "supernova", "keywords": ["deep space colorful stellar core 4k", "supernova remnant glowing", "neutron core"]},
            {"scene_id": 12, "is_cta": True, "text": "Which stellar phenomenon amazed you the most? Drop a comment, hit like, and follow for more mind-blowing science!", "subject": "supernova", "keywords": ["glowing starry galaxy cosmos 4k", "pulsar space nebula", "space galaxy"]}
        ]
    },

    # --------------------------------------------------------------------------
    # 🏺 CATEGORÍA: HISTORIA Y ANTIGUAS CIVILIZACIONES
    # --------------------------------------------------------------------------
    "egypt": {
        "title": "5 Mind-Blowing Secrets of Ancient Egypt & The Pyramids! 🏺👑",
        "intro_tag": "Ancient Egypt and the Great Pyramids",
        "scenes": [
            {"scene_id": 2, "curiosity_index": 1, "text": "Number one: The Great Pyramid was originally covered in polished white limestone that shone like a giant jewel in the desert sun.", "subject": "pyramid", "keywords": ["pyramids of giza glowing sun 4k", "white limestone ancient egypt", "great pyramid"]},
            {"scene_id": 3, "curiosity_index": 1, "text": "It reflected sunlight so intensely that it could be seen from miles away and even from the mountains of Israel.", "subject": "pyramid", "keywords": ["ancient pyramids aerial view 4k", "giza pyramid complex desert", "egyptian monuments"]},
            {"scene_id": 4, "curiosity_index": 2, "text": "Number two: The pyramids were not built by slaves, but by respected and well-fed Egyptian craftsmen.", "subject": "pharaoh", "keywords": ["ancient egyptian hieroglyphics wall 4k", "egyptian temple carving stone", "ancient egypt art"]},
            {"scene_id": 5, "curiosity_index": 2, "text": "Archaeological records show workers were paid with meat, medical care, and daily rations of nutritious beer.", "subject": "pharaoh", "keywords": ["ancient egyptian statues museum 4k", "egyptian pharaoh gold relic", "ancient craftsmen"]},
            {"scene_id": 6, "curiosity_index": 3, "text": "Number three: Honey found sealed inside ancient Egyptian tombs over three thousand years ago is still perfectly edible today.", "subject": "honey", "keywords": ["golden honey dripping jar 4k", "honeycomb organic golden honey", "miel dorada"]},
            {"scene_id": 7, "curiosity_index": 3, "text": "Its lack of moisture and natural acidity prevents bacteria from ever growing, making honey truly immortal.", "subject": "honey", "keywords": ["golden honey macro close up 4k", "ancient jar relic gold", "pure honey"]},
            {"scene_id": 8, "curiosity_index": 4, "text": "Number four: The Great Pyramid aligns with True North with an error of just five hundredths of a degree.", "subject": "pyramid", "keywords": ["pyramids starry night sky cosmos 4k", "constellation orion pyramids alignment", "giza night stars"]},
            {"scene_id": 9, "curiosity_index": 4, "text": "That is higher architectural precision than the Greenwich Royal Observatory built thousands of years later.", "subject": "pyramid", "keywords": ["great pyramid astronomy stars 4k", "egyptian night sky galaxy", "ancient pyramid cosmos"]},
            {"scene_id": 10, "curiosity_index": 5, "text": "Number five: Cleopatra lived closer in time to the Moon Landing and the iPhone than to the construction of the Great Pyramids.", "subject": "pharaoh", "keywords": ["cleopatra statue golden ancient egypt 4k", "golden pharaoh mask tutankhamun 4k", "cleopatra gold"]},
            {"scene_id": 11, "curiosity_index": 5, "text": "Over two thousand five hundred years separated the building of Giza from the reign of Egypt's last queen.", "subject": "pharaoh", "keywords": ["ancient egyptian golden artifacts 4k", "luxor temple columns egypt 4k", "pharaoh treasures"]},
            {"scene_id": 12, "is_cta": True, "text": "Which of these ancient secrets surprised you the most? Drop a comment, hit like, and follow for more mind-blowing history!", "subject": "pyramid", "keywords": ["majestic pyramids sunset desert 4k", "ancient egypt golden sphinx 4k", "pyramids of giza"]}
        ]
    },

    "rome": {
        "title": "5 Shocking Secrets of the Roman Empire! ⚔️🏛️",
        "intro_tag": "the Mighty Roman Empire",
        "scenes": [
            {"scene_id": 2, "curiosity_index": 1, "text": "Number one: Roman concrete was self-healing and actually grew stronger when exposed to seawater over thousands of years.", "subject": "bone", "keywords": ["colosseum rome ancient ruins 4k", "roman pantheon architecture sunny", "ancient rome colosseum"]},
            {"scene_id": 3, "curiosity_index": 1, "text": "Volcanic ash and quicklime formed rare crystals that sealed micro-cracks automatically during mineral reactions.", "subject": "bone", "keywords": ["ancient roman aqueduct masonry 4k", "roman stone columns temple", "roman architecture"]},
            {"scene_id": 4, "curiosity_index": 2, "text": "Number two: Ancient Romans used urine as mouthwash and laundry detergent.", "subject": "acid", "keywords": ["ancient roman baths architecture 4k", "roman mosaic floor ancient", "roman baths"]},
            {"scene_id": 5, "curiosity_index": 2, "text": "The ammonia in urine acted as a powerful natural bleach, and public urine was so valuable that Emperor Vespasian taxed it.", "subject": "pharaoh", "keywords": ["ancient roman coins gold silver 4k", "statue roman emperor caesar", "roman coins"]},
            {"scene_id": 6, "curiosity_index": 3, "text": "Number three: Romans occasionally flooded the Colosseum to stage real naval battles with warships.", "subject": "ocean", "keywords": ["colosseum arena aerial cinematic 4k", "ancient roman naval galley warship", "colosseum aerial"]},
            {"scene_id": 7, "curiosity_index": 3, "text": "Known as Naumachia, thousands of combatants fought in front of roaring crowds on millions of gallons of water.", "subject": "ocean", "keywords": ["roman soldiers legion armor 4k", "gladiator combat ancient arena", "roman legion"]},
            {"scene_id": 8, "curiosity_index": 4, "text": "Number four: Flaming pigs were used on ancient battlefields to terrify and route war elephants.", "subject": "komodo", "keywords": ["ancient war elephant marching army 4k", "ancient roman battlefield cinematic", "ancient army"]},
            {"scene_id": 9, "curiosity_index": 4, "text": "The panicked squeals of covered pigs caused multi-ton elephants to turn and trample their own armies in chaos.", "subject": "komodo", "keywords": ["ancient roman shields battle line 4k", "roman standard eagle army", "roman battle"]},
            {"scene_id": 10, "curiosity_index": 5, "text": "Number five: Julius Caesar was once kidnapped by pirates and demanded they double his ransom because he felt insulted.", "subject": "pharaoh", "keywords": ["statue julius caesar marble rome 4k", "ancient mediterranean pirate ship", "julius caesar statue"]},
            {"scene_id": 11, "curiosity_index": 5, "text": "After being paid, Caesar raised a private navy, tracked down the pirates, and captured every single one of them.", "subject": "pharaoh", "keywords": ["ancient roman warships sailing blue sea 4k", "ancient mediterranean coastline", "roman fleet"]},
            {"scene_id": 12, "is_cta": True, "text": "Which Roman secret surprised you the most? Drop a comment, hit like, and follow for more historic discoveries!", "subject": "pyramid", "keywords": ["colosseum sunset golden light rome 4k", "roman forum ancient ruins", "colosseum rome"]}
        ]
    },

    # --------------------------------------------------------------------------
    # 🌊 CATEGORÍA: OCÉANOS PROFUNDOS Y ABISALES
    # --------------------------------------------------------------------------
    "ocean": {
        "title": "5 Terrifying Mysteries of the Deep Abyss! 🌊🦈",
        "intro_tag": "the Mysterious Deep Ocean",
        "scenes": [
            {"scene_id": 2, "curiosity_index": 1, "text": "Number one: Over eighty percent of all creatures living in the midnight zone produce their own living light.", "subject": "jellyfish", "keywords": ["bioluminescent jellyfish glowing deep ocean", "glowing underwater creatures 4k", "jellyfish dark ocean"]},
            {"scene_id": 3, "curiosity_index": 1, "text": "They use glowing chemical reactions to attract prey, communicate, and blind predators in total darkness.", "subject": "jellyfish", "keywords": ["deep sea bioluminescence glowing 4k", "bioluminescent sea creatures", "glowing jellyfish"]},
            {"scene_id": 4, "curiosity_index": 2, "text": "Number two: The Greenland shark is the longest-living vertebrate on Earth, surviving for over four hundred years.", "subject": "shark", "keywords": ["greenland shark swimming deep ocean", "ancient shark arctic ocean underwater", "deep sea shark 4k"]},
            {"scene_id": 5, "curiosity_index": 2, "text": "Some sharks swimming in the Arctic depths today were already alive during the time of the Renaissance.", "subject": "shark", "keywords": ["giant shark deep cold ocean", "arctic sea shark underwater 4k", "shark deep water"]},
            {"scene_id": 6, "curiosity_index": 3, "text": "Number three: At the bottom of the Mariana Trench, the water pressure is over one thousand times greater than at sea level.", "subject": "submarine", "keywords": ["deep sea submarine abyss exploration", "deep ocean submersible rover 4k", "mariana trench submarine"]},
            {"scene_id": 7, "curiosity_index": 3, "text": "That is equivalent to having the weight of fifty jumbo jets pressing down on your entire body at once.", "subject": "submarine", "keywords": ["deep ocean seabed submersible lights", "abyss ocean exploration 4k", "submersible deep sea"]},
            {"scene_id": 8, "curiosity_index": 4, "text": "Number four: There are actual rivers and lakes flowing along the very bottom of the ocean.", "subject": "submarine", "keywords": ["underwater brine pool deep ocean lake", "deep sea seabed landscape 4k", "underwater river abyss"]},
            {"scene_id": 9, "curiosity_index": 4, "text": "These dense underwater brine pools have distinct shorelines and waves, completely separate from the surrounding seawater.", "subject": "submarine", "keywords": ["deep ocean floor exploration 4k", "mysterious underwater abyss landscape", "deep seabed lights"]},
            {"scene_id": 10, "curiosity_index": 5, "text": "Number five: The colossal squid possesses the largest eyes in the animal kingdom, as big as basketballs.", "subject": "squid", "keywords": ["giant squid swimming deep ocean", "colossal squid underwater creature 3d", "squid deep sea 4k"]},
            {"scene_id": 11, "curiosity_index": 5, "text": "These massive lenses allow them to detect faint shadows and glowing bioluminescence from hundreds of meters away.", "subject": "squid", "keywords": ["deep sea giant squid tentacle 4k", "bioluminescent squid deep ocean", "colossal squid"]},
            {"scene_id": 12, "is_cta": True, "text": "Which of these deep sea mysteries amazed you the most? Drop a comment, hit like, and follow for more mind-blowing discoveries!", "subject": "jellyfish", "keywords": ["deep sea glowing creatures abyss 4k", "bioluminescent jellyfish dark ocean", "deep ocean"]}
        ]
    },

    # --------------------------------------------------------------------------
    # 🧬 CATEGORÍA: CUERPO HUMANO Y NEUROCIENCIA
    # --------------------------------------------------------------------------
    "human": {
        "title": "5 Unbelievable Superpowers of the Human Body! 🧬⚡",
        "intro_tag": "the Human Body",
        "scenes": [
            {"scene_id": 2, "curiosity_index": 1, "text": "Number one: The human brain generates enough electricity to power a small LED lightbulb.", "subject": "brain", "keywords": ["neurons firing electrical synapse brain 4k", "glowing neural brain activity", "brain electrical"]},
            {"scene_id": 3, "curiosity_index": 1, "text": "With over eighty-six billion neurons, your brain processes more computations per second than the most powerful supercomputer.", "subject": "brain", "keywords": ["neural network human brain thinking 4k", "futuristic neural brain concept", "brain network"]},
            {"scene_id": 4, "curiosity_index": 2, "text": "Number two: Human bone is ounce for ounce four times stronger than concrete.", "subject": "bone", "keywords": ["human skeleton anatomy medical bone 4k", "bone structure microscopic 4k", "skeleton bone"]},
            {"scene_id": 5, "curiosity_index": 2, "text": "A single cubic inch of human bone can withstand a load of over nineteen thousand pounds without breaking.", "subject": "bone", "keywords": ["human spine femur bone anatomy 4k", "medical bone scan 3d", "bone anatomy"]},
            {"scene_id": 6, "curiosity_index": 3, "text": "Number three: Your stomach acid is powerful enough to dissolve razor blades and stainless steel.", "subject": "acid", "keywords": ["chemical acid reaction liquid laboratory 4k", "stomach digestive system anatomy 4k", "acid liquid"]},
            {"scene_id": 7, "curiosity_index": 3, "text": "To protect itself from self-destruction, your stomach completely regenerates its inner lining every four days.", "subject": "acid", "keywords": ["cells dividing biological regeneration 4k", "microscopic cellular biology", "cells division"]},
            {"scene_id": 8, "curiosity_index": 4, "text": "Number four: If you unraveled all the DNA in your body, it would stretch to Pluto and back twice.", "subject": "dna", "keywords": ["dna double helix rotating glowing 4k", "genetics dna strand molecular biology", "dna helix"]},
            {"scene_id": 9, "curiosity_index": 4, "text": "That is over thirty-four billion miles of genetic code packed inside microscopic cells.", "subject": "dna", "keywords": ["dna sequence genetic molecular 4k", "microscopic cells dna glowing", "genetics code"]},
            {"scene_id": 10, "curiosity_index": 5, "text": "Number five: Your heart beats over one hundred thousand times every single day.", "subject": "heart", "keywords": ["human heart beating 3d medical animation 4k", "cardiovascular blood vessels glowing", "heart beating"]},
            {"scene_id": 11, "curiosity_index": 5, "text": "In an average lifetime, it pumps enough blood to fill three entire supertanker ships.", "subject": "heart", "keywords": ["red blood cells flowing artery 4k", "cardiovascular bloodstream medical", "blood flow"]},
            {"scene_id": 12, "is_cta": True, "text": "Which human superpower surprised you the most? Drop a comment, hit like, and follow for more mind-blowing science!", "subject": "brain", "keywords": ["glowing neural brain network 4k", "human body medical animation", "brain neurons"]}
        ]
    },

    # --------------------------------------------------------------------------
    # 🦅 CATEGORÍA: REINO ANIMAL EXTREMO
    # --------------------------------------------------------------------------
    "animals": {
        "title": "5 Animals with Real Superpowers in Nature! 🦅🦎",
        "intro_tag": "Animals with Real Superpowers",
        "scenes": [
            {"scene_id": 2, "curiosity_index": 1, "text": "Number one: The Komodo dragon is equipped with armor-plated chainmail beneath its scaly skin.", "subject": "komodo", "keywords": ["komodo dragon close up skin scales 4k", "komodo dragon lizard crawling", "komodo dragon"]},
            {"scene_id": 3, "curiosity_index": 1, "text": "These microscopic bone deposits, called osteoderms, protect them during violent battles with rival dragons.", "subject": "komodo", "keywords": ["komodo dragon battle island 4k", "varanus komodoensis running", "komodo reptile"]},
            {"scene_id": 4, "curiosity_index": 2, "text": "Number two: Crows understand the concept of zero and can remember human faces for their entire lives.", "subject": "crow", "keywords": ["black crow raven perched tree 4k", "intelligent crow flying close up 4k", "corvus raven"]},
            {"scene_id": 5, "curiosity_index": 2, "text": "They teach their offspring which humans are trustworthy and which ones to avoid.", "subject": "crow", "keywords": ["crow flock perched intelligent bird 4k", "raven eyes close up bird", "crow bird"]},
            {"scene_id": 6, "curiosity_index": 3, "text": "Number three: The Axolotl can completely regenerate not just lost limbs, but its heart, lungs, and parts of its brain.", "subject": "axolotl", "keywords": ["axolotl swimming aquarium water 4k", "pink axolotl salamander close up", "axolotl gills"]},
            {"scene_id": 7, "curiosity_index": 3, "text": "Scientists are actively studying their genetic code to unlock tissue regeneration in human medicine.", "subject": "axolotl", "keywords": ["axolotl pink underwater swimming 4k", "mexican salamander axolotl", "axolotl"]},
            {"scene_id": 8, "curiosity_index": 4, "text": "Number four: Hummingbirds are the only birds on Earth capable of flying backwards and upside down.", "subject": "hummingbird", "keywords": ["hummingbird hovering flower slow motion 4k", "colorful hummingbird wings flapping", "hummingbird slowmo"]},
            {"scene_id": 9, "curiosity_index": 4, "text": "Their wings flap up to eighty times per second with a heart rate exceeding one thousand two hundred beats per minute.", "subject": "hummingbird", "keywords": ["hummingbird drinking nectar macro 4k", "hummingbird slow motion wings", "hummingbird flower"]},
            {"scene_id": 10, "curiosity_index": 5, "text": "Number five: The blue whale's tongue weighs as much as an entire adult elephant.", "subject": "whale", "keywords": ["blue whale swimming ocean surface 4k", "giant humpback whale breaching 4k", "blue whale ocean"]},
            {"scene_id": 11, "curiosity_index": 5, "text": "A human child could easily swim through the major blood vessels of its heart.", "subject": "whale", "keywords": ["giant whale underwater ocean 4k", "whale tail fluke diving blue water", "whale swimming"]},
            {"scene_id": 12, "is_cta": True, "text": "Which animal superpower amazed you the most? Drop a comment, hit like, and follow for more wild discoveries!", "subject": "komodo", "keywords": ["majestic wild animals nature 4k", "komodo dragon landscape sunset", "wild wildlife"]}
        ]
    },

    "tardigrade": {
        "title": "5 Shocking Truths About the Immortal Water Bear! 🔬🦠",
        "intro_tag": "the Indestructible Tardigrade",
        "scenes": [
            {"scene_id": 2, "curiosity_index": 1, "text": "Number one: Tardigrades can survive in the freezing vacuum of outer space and intense cosmic radiation.", "subject": "supernova", "keywords": ["tardigrade microscopic close up 4k", "water bear under microscope science", "tardigrade microscope"]},
            {"scene_id": 3, "curiosity_index": 1, "text": "In European Space Agency experiments, water bears were exposed to raw solar radiation and returned to life unaffected.", "subject": "astronaut", "keywords": ["iss international space station earth 4k", "astronaut spacewalk earth background", "space station orbit"]},
            {"scene_id": 4, "curiosity_index": 2, "text": "Number two: They can endure temperatures as low as minus four hundred and fifty-nine degrees Fahrenheit, near Absolute Zero.", "subject": "diamond", "keywords": ["freezing ice crystals forming macro 4k", "sub-zero frozen landscape arctic", "ice crystal formation"]},
            {"scene_id": 5, "curiosity_index": 2, "text": "They also survive boiling temperatures over three hundred degrees Fahrenheit without boiling their internal cells.", "subject": "acid", "keywords": ["boiling bubbling geothermal water 4k", "volcanic thermal pool bubbling", "boiling water steam"]},
            {"scene_id": 6, "curiosity_index": 3, "text": "Number three: Tardigrades enter a state called cryptobiosis, expelling ninety-nine percent of their body's water.", "subject": "dna", "keywords": ["microscopic biological organism 4k", "cell dehydration biology microscope", "microorganism"]},
            {"scene_id": 7, "curiosity_index": 3, "text": "Their metabolism drops to zero point zero one percent of normal, essentially pausing their biological clock for decades.", "subject": "dna", "keywords": ["clock ticking slow motion time lapse 4k", "biological cell division glowing", "time clock"]},
            {"scene_id": 8, "curiosity_index": 4, "text": "Number four: Water bears have survived all five mass extinction events in Earth's history.", "subject": "bone", "keywords": ["dinosaur extinction meteor impact 4k", "ancient prehistoric earth volcano", "meteor earth"]},
            {"scene_id": 9, "curiosity_index": 4, "text": "They were thriving six hundred million years ago, long before the first dinosaurs walked the Earth.", "subject": "bone", "keywords": ["prehistoric ocean ancient fossils 4k", "paleontology prehistoric landscape", "ancient fossils"]},
            {"scene_id": 10, "curiosity_index": 5, "text": "Number five: Thousands of dehydrated tardigrades were accidentally spilled on the Moon in twenty-nineteen.", "subject": "moon", "keywords": ["lunar lander crashing moon surface 4k", "moon surface dusty crater landscape", "moon lander"]},
            {"scene_id": 11, "curiosity_index": 5, "text": "Scientists believe these dormant micro-animals could remain viable on the lunar surface for centuries.", "subject": "moon", "keywords": ["astronaut footprint moon surface 4k", "earth rising over moon crater", "moon surface"]},
            {"scene_id": 12, "is_cta": True, "text": "Could tardigrades colonize the Moon? Drop your theory in the comments, hit like, and follow for more micro-wonders!", "subject": "supernova", "keywords": ["microscopic tardigrade swimming 4k", "deep space stars nebula cosmos", "tardigrade"]}
        ]
    }
}

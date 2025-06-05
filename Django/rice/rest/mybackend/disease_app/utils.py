# disease_app/utils.py
DISEASE_INFO = {
    "Bacterial Blight": {
        "pesticides": ["Copper hydroxide", "Streptomycin",
        ],
        "precautions": [
            
            "Preventive method:-" ,
            "-Seed treatment with bleaching powder (100g/l) and zinc sulfate (2%) reduce bacterial blight.",
            "-Seed treatment - seed soaking for 8 hours in Agrimycin (0.025%) and wettable ceresan (0.05%) followed by hot water treatment for 30 min at 52-54oC",
            "-seed soaking for 8 hours in ceresan (0.1%) and treat with Streptocyclin (3g in 1 litre);",
            "-Spray neem oil (3%) or NSKE 5%",
            "-Spray fresh cowdung extract for the control of bacterial blight.,",
            "Dissolve 20 g cowdung in one litre of water; allow to settle and sieve. Use supernatant liquid. (starting from initial appearance of the disease and another at fortnightly interval)",
            
            "Chemical methods:-:",
            "-Seed treatment with bleaching powder (100g/l) and zinc sulfate (2%) reduce bacterial blight.",
            "-Seed treatment - seed soaking for 8 hours in Agrimycin (0.025%) and wettable ceresan (0.05%) followed by hot water treatment for 30 min at 52-54oC",
            "-Seed soaking for 8 hours in ceresan (0.1%) and treat with Streptocyclin (3g in 1 litre)",
            "-Spray Streptomycin sulphate + Tetracycline combination 300 g + Copper oxychloride 1.25kg/ha. If necessary repeat 15 days later",
            "-Application of bleaching powder @ 5 kg/ha in the irrigation water is recommended in the kresek stage.",
            "-Foliar spray with copper fungicides alternatively with Strepto-cyclin (250 ppm) to check secondary spread.",
        ]
    },
    "Brown Spot": {
        "pesticides": ["Carbendazim", "Mancozeb"],
        "precautions": [
            "Preventive methods:-",
            "-Seed treatment with Pseudomonas fluorescens @ 10g/kg of seed followed by seedling dip @ of 2.5 kg or products/ha dissolved in 100 litres and dipping for 30 minutes.",
            "-seed soak / seed treatment with Captan or  Thiram at 2.0g /kg of seed.",
            "-Seed treatment with Agrosan or Ceresan 2.5 g/kg seed to ward off seedling blight stage",
            "-Since the fungus is seed transmitted, a hot water seed treatment (53-54°C) for 10-12 minutes may be effective before sowing." ,
            "This treatment controls primary infection at the seedling stage. Presoaking the seed in cold water for 8 hours increases effectivity of the treatment.",
            
            "Chemical methods:-",
            "-Seed soak / seed treatment with Captan or  Thiram at 2.0g /kg of seed",
            "-Spray Mancozeb (2.0g/lit) or Edifenphos (1ml/lit) - 2 to 3 times at 10 - 15 day intervals.",
            "-Spray preferably during early hours or afternoon at flowering and post - flowering stages.",
            "-Seed treatment with Agrosan or Ceresan 2.5 g/kg seed to ward off seedling blight stage; Spraying copper fungicides to control secondary spread",
            "-Grisepfulvin, nystatin, aureofungin, and similar antibiotics have been found effective in preventing primary seedling infection.",
            "-Seed treatment with captan, thiram, chitosan, carbendazim, or mancozeb has been found to reduce seedling infection.",
            "-Seed treatment with tricyclazole followed by spraying of mancozeb + tricyclazole at tillering and late booting stages gave good control of the disease. Application of edifenphos, chitosan, iprodione, or carbendazim in the field is also advisable.",
        ]
    },
    "Tungro": {
        "pesticides": ["Imidacloprid", "Carbosulfan"],
        "precautions": [
            "Trap methods:-",
            "-Light traps are to be set up to attract and control the leaf hopper vectors as well as to monitor the population.",
            "-Light traps are to be set up to attract and control the leaf hopper vectors as well as to monitor the population.",
            "In the early morning, the population of leafhopper alighting near the light trap should be killed by spraying/dusting the insecticides.",
            "This should be practiced every day.",
            
 	 	 
            "Cultural methods:-",
            "-Planting of resistant varieties against tungro virus disease is the most economical means of managing the disease.",
            "-Use  Resistant varieties like IR 36,  IR 50 ,ADT 37,  Ponmani, Co 45, Co 48, Surekha, Vikramarya, Bharani, IR 36   and white ponni .",
            "-Among the cultural management practices, adjusting the date of planting is recommended.",
            "-Likewise, observing a fallow period of at least a month to eliminate hosts and viruses and vectors of the disease.",
            "-In epidemic areas follow rotation with pulses or oil seeds.",
            "-Apply neem cake @ 12.5 kg/20 cent nursery as basal dose.",
            "-plouging and harrowing the field to destroy stubbles right after harvest in order to eradicate other tungro hosts are also advisable.",
            "Destruction of weed hosts on bunds.",
 	 	 
            "Chemical methods:-",
            "-Leaf yellowing can be minimized by spraying (2%) urea mixed with Mancozeb at 2.5 gm/lit.",
            "-Instead of urea foliar fertilizer like multi-K (potassium nitrate) can be sprayed at 1 per cent which impart resistance also because of high potassium content.",
            "-Green leaf hoppers as vectors are to be controlled effectively in time by spraying.",
            "-Spray insecticides twice, 15 and 30 days after transplanting",

            "---Spray Two rounds of any one of the following insecticides---",
            "-Fenthion 100 EC (40 ml/ha) may be sprayed 15 and 30 days after transplanting.",
            "-The vegetation on the bunds should also be sprayed with the insecticides. Maintain 2.5 cm of water in the nursery and broadcast anyone of the following in 20 cents Carbofuran 3 G 3.5 kg (or) Phorate 10 G 1.0 kg (or) Quinalphos 5 G 2.0 kg",
            "-In nursery when virus infection is low, apply Carbofuran granules @ 1 kg./ha to control vector population.",
            "-During pre-tillering to mid-tillering when one affected hill/m is observed apply Carbofuran granules @ 3.5kg/ha to control insect vector.",
        ]
    },
    "leaf Blast": {
        "pesticides": ["Tricyclazole", "Pyrazophos"],
        "precautions": [
            "Cultural methods:-",
            
            "-Planting resistant varieties against the rice blast is the most practical and economical way of controlling rice blast.",
            "-Use of Tolerant varieties (CO 47, CO 50, ADT 36,ADT 37,ASD 16,ASD 20,ADT 39,ASD 19,TPS 3,White ponni,ADT 44,BPT 5204,CORH , Palghuna, Swarnamukhi, Swathi, Prabhat, IR - 64, , IR - 36, Jaya)",
            "-Avoid excess N - fertilizer application",
            "-Apply nitrogen in three split doses.",
            "-Remove weed hosts from bunds.",
  
            "Preventive methods:-",
            "-Avoid dry nurseries.",
            "-Avoid late planting.",
            "-Burning of straw and stubbles after harvest",
            "-Avoid grasses and other weeds on bunds and inside.",
            "-Dry seed treatment with Pseudomonas fluorescens talc formulation @10g/kg of seed.",
            "-Stagnate water to a depth of 2.5cm over an area of 25m2 in the nursery. Sprinkle 2.5 kg of P. fluorescens (talc) and mix with stagnated water. Soak the root system of seedlings for 30 min and transplant.",
            "-Spray P. fluorescens talc formulation @ (0.5%) from 45 days after transplanting at 10 day intervals, three times.",

            "Chemical methods:-",
            "-Do not apply lower/higher doses of fungicides.",
            "-Spray before 11.00 AM/after 3.00 PM.",
            "-Avoid noon hours for spraying.",
            "-Seed treatment at 2.0 g/kg seed with Captan or Carbendazim or Thiram or Tricyclazole.",
            "-Systemic fungicides such as pyroquilon and tricyclazole are possible chemicals for controlling the disease.",
            "-praying of Tricyclazole at 1g/lit of water or Edifenphos at 1 ml/lit of water or Carbendazim at 1.0 gm/lit.",
            "-3 to 4 sprays each at nursery, tillering stage and panicle emergence stage may be required for complete control.",
            "-Nursery stage: Light infection - Spray Carbendazim or Edifenphos @ 1.0 gm/lit.",
            "-Pre-Tillering to Mid-Tillering: Light at (2 to 5%) disease severities - Apply Edifenphos or Carbendazim @ 1.0 gm/lit. Delay top dressing of N fertilizers when infection is seen.",
            "-Panicle initiation to booting: At (2 to 5%) leaf area damage- spray Edifenphos or Carbendazim or Tricyclazole @ 1.0 gm/lit.",
            "-Flowering and after: At (5%) leaf area damage or 1 to 2 % neck infection spray Edifenphos or Carbendazim or Tricyclazole @ 1 g /lit of water.",
        ]
    },
    "healthy": {
        "pesticides": [],
        "precautions": [],
    }
}

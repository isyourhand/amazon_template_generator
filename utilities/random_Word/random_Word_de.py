import random

def fabric_type_random():
    words = ["Alpaka","Angora","Baumwolle","Cord","Daunen","Filz","Fleece","Glattleder","Gummi","Hanf","Jeans","Kaschmir","Lackleder","Leder","Leinen","Merino","Mohair","Pailletten","Pelz","Pelzimitat","Samt","Satin","Seide","Synthetisch","Wildleder","Wolle","Angorawolle","Fur","Fellimitat","Paillettenbesetzt","Kashmir","Synthetik","Denim"]
    return random.choice(words)

def outer_material_type_random():
    words = ["Alpaka","Angora","Baumwolle","Cord","Daunen","Filz","Fleece","Glattleder","Gummi","Hanf","Jeans","Kaschmir","Lackleder","Leder","Leinen","Merino","Mohair","Pailletten","Pelz","Pelzimitat","Samt","Satin","Seide","Synthetisch","Wildleder","Wolle","Angorawolle","Fur","Fellimitat","Paillettenbesetzt","Kashmir","Synthetik","Denim"]
    return random.choice(words)

def lifestyle1_random():
    words = ["Nursing","Dress","Work Utility","Athletic","Casual","Uniform","Themed","Exotic","Contemporary","Sport","Comfort","Business Casual","Yoga","Performance","Fitness"]
    return random.choice(words)

def item_length_description_random():
    words = ["Knielang","Maxi","Midi","Mini","Unter dem Knie","Über dem Knie","High-Low","Bodenlang","Knöchellang","Mitte Oberschenkellang","Wadenlang","Kurz","Lang"]
    return random.choice(words)

def inner_material_type_random():
    words = ["Alpaka","Angora","Baumwolle","Cord","Daunen","Filz","Fleece","Glattleder","Gummi","Hanf","Jeans","Kaschmir","Lackleder","Leder","Leinen","Merino","Mohair","Pailletten","Pelz","Pelzimitat","Samt","Satin","Seide","Synthetisch","Wildleder","Wolle","Angorawolle","Fur","Fellimitat","Paillettenbesetzt","Kashmir","Synthetik","Denim"]
    return random.choice(words)

def material_type_random():
    words = ["Elasthan","Gummi","Kaschmir","Leder","Leinen","Neoprene","Nylon","Polyester","Seide","Viskose","Wildleder","Wolle"]
    return random.choice(words)

def sport_type_random():
    words = ["Motorschlittenfahren","Kajakfahren","Rugby","Bogenschießen","Trekking","Angeln","Badminton","Paddelboarden","T-Ball","Pferderennen","Training & Training","Straßenradfahren","Rollhockey","Surfen","Eistauchen","Cheerleading","Pferdesport","Golf","Triathlon","Bowling","Volleyball","Bootfahren","Cyclocross","Snowboarden","Wiffleball","Kricket","Bergsteigen","Laufen","Segeln","Baseball","Ringkampf","Kitesurfen","Yoga","Softball","Tanz","Fußball","Skateboarden","Wandern","Boxen","Gewichtheben","Yachtsport","Schwimmen","Tischtennis","Airsoft","American Football","Gehen","Basketball","Eislaufen","Skifahren","Squash","Racquetball","Paintball","Klettern","Jagd","Autorennsport","Mountain Biking","Felsklettern","Wakeboarden","Billard","Multi-Sport","Radfahren","Tennis","Gymnastik","Mixed Martial Arts","Hockey","Ski Alpin","Tauchen","Kanufahren","BMX","Outdoor-Lifestyle","Rennsport","Schnorcheln","Wasserpolo","Kampfkünste","Skitourengehen","Rollschuhlaufen","Lacrosse","Wasserskilaufen","Rafting","Windsurfen","Track"]
    return random.choice(words)

# def pattern_name_random():
#     words = ["Animal Print","Argyle","Camouflage","Cartoon","Checkered","Chevron","Floral","Fruits","Geometric","Hearts","Herringbone","Houndstooth","Letter Print","Moire","Paisley","Plaid","Polka Dots","Solid","Stars","Striped"]
#     return random.choice(words)

def pocket_description_random():
    words = ["Cargotasche","Gerade Tasche","Kängurutasche","Leistentasche","Münztasche","Nahttasche","Paspeltasche","Pattentasche","Schlitztasche","Schrägtasche"]
    return random.choice(words)

def top_style_random():
    words = ["Bandeau","Neckholder","Push-Up","Racerback","Schalen","Triangel","mit Bügel","Bralette","Stehkragen","Bügel","Crossback","Rashguard","Eine Schulter","Schulterfrei","Tankini","Monokini","Trägerlos","Leibchen","Ausgestellt","Longline","T-Back","Einteilig","Vorderer Bindeverschluss","Rüsche","Über die Schulter","Button-down"]
    return random.choice(words)

def special_features_random():
    words = ["Adjustable","Built In Scale","Carry-On","Checkpoint Friendly","Elastic Band","Lightweight","Reversible","Sun Protection","Tsa Lock","Tsa Ready","Wrinkle-Free","Telescoping Handles","Expandable","Includes Card Holders","Includes Coin Pouch","Laptop Compartment","Waterproof","Stretch","Heavy Duty","elastic-band","fade resistant","hypoallergenic","super soft","scented","high color fastness","patterned","low linting","hanging loop","bleach resistant","super absorbent","zero twist","light weight","embroidered","quick dry"]
    return random.choice(words)

def front_style_random():
    words = ["Flache Vorderseite","Plissierte Vorderseite"]
    return random.choice(words)

def rise_style_random():
    words = ["Hohe Taille","MittlereTaille","Niedrige Taille"]
    return random.choice(words)

def weave_type_random():
    words = ["Gewebt","Gestrickt"]
    return random.choice(words)

def collar_style_random():
    words = ["Button-down","Grandad","Haifisch","Kent","Kläppchenkragen","Rundkragen","Stehkragen","Tab-Kragen","Versteckte Button-down","Tab","Club","Flügelspitze","Gerade Spitze","Camp","Spreizkragen"]
    return random.choice(words)

def fabric_wash_random():
    words = ["Mittel","Light","Dunkel"]
    return random.choice(words)

def bottom_style_random():
    words = ["Rock","Shorts","Slip","String","Hipster","Boardshorts","G-String","Trunk","Skimpy","Jammer","Skirted","Banded Bottoms","Boy Shorts"]
    return random.choice(words)

def leg_style_random():
    words = ["Ankle","Boot Cut","Cropped","Flared","Skinny","Straight","Tapered","Trouser","Wide","Cuffed","Stirrup","Pencil"]
    return random.choice(words)

def strap_type_random():
    words = ["Abnehmbar","Spaghetti","Halfter","One-Shoulder","Trägerlos","Verstellbar"]
    return random.choice(words)

def waist_style_random():
    words = ["Hoher Bund","Normaler Bund","Sehr tiefer Bund","Tiefer Bund"]
    return random.choice(words)

def item_weight_random():
    return random.randint(100, 250)

def occasion_types_random():
    words = [
                "Abschluss","Abschlussball und Ehrungsfeier","Babyparty","Beerdigung","Brautparty","Erntedankfest","Flitterwochen","Geburt","Geburtstag","Halloween","Hochzeit","Jahrestag","Junggesellenabschied","Junggesellinnenabschied","Kommunion","Muttertag","Neues Jahr","Ostern","St. Patrick's Day","Taufe","Unabhängigkeitstag","Valentinstag","Vatertag","Verlobung","Weihnachten"
            ]
    return random.choice(words)

def lifecycle_supply_type_random():
    words = ["Perennial","Year Round Replenishable","Seasonal Basic","Fashion"]
    return random.choice(words)

def fit_type_random():
    words = ["Moderne Passform","Reguläre Passform","Entspannte Passform","Halb tailliert","Skinny Passform","Maßgeschneiderte Passform","Klassische Passform", "Angepasst", "Lockere Passform", "Slim Passform"]
    return random.choice(words)

def theme_random():
    words = ["Abendmode","Business","Casual","Feierliche Anlässe","Arbeit","Mutterschaft","Stillen","Athletisch","Lässig","Themenorientiert","Kinder-Spielkleidung","Uniform","Kleid","Exotisch"]
    return random.choice(words)

def lining_description_random():
    words = ["Polyester","Nylon","Wolle","Baumwolle","Pelz","Mikrofaser","Rayon","Seide","Elastan","Kunstpelz"]
    return random.choice(words)

def neck_style_random():
    words = ["Crew-Hals",
    "V-Ausschnitt",
    "Tiefer Hals",
    "Mit Kapuze",
    "Trägerlos",
    "Halfterhals",
    "U-Boot-Ausschnitt",
    "Eckiger Ausschnitt",
    "Henley Ausschnitt",
    "Off Schulterhals",
    "Schlüssellochhals",
    "Schalkragen",
    "Mock-Ausschnitt",
    "Halber Reißverschluss",
    "Racerback",
    "Asymmetrischer Ausschnitt",
    "One Shoulder",
    "Bootshals",
    "Rollkragen",
    "Herzausschnitt",
    "Geteilter Hals",
    "Criss Cross Neck",
    "Henley Ausschnitt",
    "Schildkrötenhals"]
    return random.choice(words)

def sleeve_type_random():
    words = ["Langarm",
    "Kurzarm",
    "Ärmellos",
    "3/4 Ärmel",
    "Halbe Ärmel",
    "Rüschenärmel",
    "Fledermausärmel",
    "Glockenärmel",
    "Puffärmel",
    "Ballonärmel",
    "Kalte Schulterhülle",
    "Kimono-Ärmel",
    "Umhang-Ärmel",
    "Spitzenärmel",
    "Flügelärmel",
    "mit Weiten Ärmeln",
    "Schmetterlingärmel",
    "Raglanärmel",
    "Laternenhülle"]
    return random.choice(words)

def closure_type_random():
    words = ["Button","Pull On","Snap","Zipper","Buckle","Double Ring","Drawstring","Hook and Eye","Hook and Loop"]
    return random.choice(words)

def style_name_random():
    words = ["Asymmetrisch","Blusenbody","Bustier","Button-down","Empire","Neckholder","Rückenfrei","Schluppenbluse","Taillenband","Trägerlos","Tunika","Wickelbluse","Wickeltop","Beschnitten","Polo","T-Shirt","Camisole","Poncho","Ausschnitt","Bluse","Kleid","Henley","Longline","Rüschen","Umhang","Puffärmel","Mehrschichtig","Wickeln","A-Linie","Stillen","Trikots","Lässig","Schößchen","Tuxedo","Bodysuit","Schulterfrei","Bauer","Normal","Legere Geschäftskleidung","Tank","Zuknöpfen","Mit Kapuze","Kaftan","Geschnürt","Batwing"]
    return random.choice(words)

def seasons_random():
    words = ["Frühling-Sommer","Ganzjahresartikel","Herbst-Winter"]
    return random.choice(words)

def collection_name_random():
    words = ["Frühjahr-Sommer 12","Frühjahr-Sommer 13","Frühjahr-Sommer 14","Frühjahr-Sommer 15","Frühjahr-Sommer 16","Frühjahr-Sommer 17","Frühjahr-Sommer 18","Herbst-Winter 12","Herbst-Winter 13","Herbst-Winter 14","Herbst-Winter 15","Herbst-Winter 16","Herbst-Winter 17","Herbst-Winter 18"]
    return random.choice(words)

def lifestyle_random():
    words = ["Business", "Casual", "Feierliche Anlässe", "Arbeit", "Mutterschaft", "Athletisch", "Lässig", "Uniform", "Kleid", "Abendmode","Stillen","Themenorientiert","Kinder-Spielkleidung","Exotisch"]
    return random.choice(words)
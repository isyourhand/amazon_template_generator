import random

def fabric_type_random():
    words = ["Angora","Cachemire","Caoutchouc","Chanvre","Cotton","Cuir","Cuir lisse","Cuir vernis","Denim","Duvet","Fausse fourrure","Feutre","Fourrure","Laine","Lin","Merino","Mohair","Pailleté","Polaire","Satin","Soie","Suède","Synthétique","Velours","Velours côtelé","Lapin angora","Fur","Coton","Alpaga","Molleton"]
    return random.choice(words)

def outer_material_type_random():
    words = ["Angora","Cachemire","Caoutchouc","Chanvre","Cotton","Cuir","Cuir lisse","Cuir vernis","Denim","Duvet","Fausse fourrure","Feutre","Fourrure","Laine","Lin","Merino","Mohair","Pailleté","Polaire","Satin","Soie","Suède","Synthétique","Velours","Velours côtelé","Lapin angora","Fur","Coton","Alpaga","Molleton"]
    return random.choice(words)

def item_length_description_random():
    words = ["Au genou","Maxi","Midi","Mini","Longueur du plancher","Longueur genou","Sous le genou","Au-dessus du genou","Haut-bas","Mi-cuisse","Longueur de la mi-cuisse","Longueur du mollet","Longueur du genou","Longueur de la cheville"]
    return random.choice(words)

def inner_material_type_random():
    words = ["Angora","Cachemire","Caoutchouc","Chanvre","Cotton","Cuir","Cuir lisse","Cuir vernis","Denim","Duvet","Fausse fourrure","Feutre","Fourrure","Laine","Lin","Merino","Mohair","Pailleté","Polaire","Satin","Soie","Suède","Synthétique","Velours","Velours côtelé","Lapin angora","Fur","Coton","Alpaga","Molleton"]
    return random.choice(words)

def material_type_random():
    words = ["Acrylique","Cuir","Daim","Élasthanne","Fourrure","Laine","Lin","Néoprène","Nylon","Polyester","Soie","Viscose"]
    return random.choice(words)

def sport_type_random():
    words = ["American football","Course à pied","Rugby","Trekking","Tennis de table","Boxe","Course hippique","Badminton","T-Ball","Embarquement paddle","Tir à larc","Art martial mixte","Crosse","Ski nautique","Skateboard","Cricket","Surf","Cyclisme","Pêche","Ski neige","Art martial","Kitesurf","Course","Cheerleading","Course automobile","Plongeon","Yachting","Golf","Triathlon","Bowling","Hippique","Volleyball","Cyclocross","Alpinisme","Balle wiffle","Gymnastique","Roller Hockey","Baseball","Chasse","Randonnée","Varappe","Yoga","Softball","Natation","Haltérophilie","Voile","Airsoft","Basketball","Snowboard","Cyclisme sur route","Squash","Canoë","Marche","Paintball","Snorkeling","VTT","Water Polo","Raquetball","Billard","Multi-Sport","Motoneige","Tennis","Wakeboard","Kayak","Patinage sur glace","Hockey","Patinage à roulette","Navigation de plaisance","Planche à voile","BMX","Football","Danse","Ski de larrière-pays","Piste","Escalade","Activité extérieure","Lutte","Plongée sous glace","Entraînement et formation","Ski alpin","Rafting"]
    return random.choice(words)

# def pattern_name_random():
#     words = ["Animal Print","Argyle","Camouflage","Cartoon","Checkered","Chevron","Floral","Fruits","Geometric","Hearts","Herringbone","Houndstooth","Letter Print","Moire","Paisley","Plaid","Polka Dots","Solid","Stars","Striped"]
#     return random.choice(words)

def pocket_description_random():
    words = ["Poche à rabat","Poche cargo","Poche couture","Poche fendue","Poche inclinée","Poche kangourou","Poche monnaie","Poche passepoilée","Poche plaquée"]
    return random.choice(words)

def top_style_random():
    words = ["Bandeau","Dos nageur","Dos nu","Emboîtant","Push-up","Sans armature","Triangle","Bouton bas","Bralette","Palangre","Cami","Rashguard","Hors de lépaule","Tankini","Licou","Monokini","Bustier","T-Back","Évasée","Retour croisé","Une épaule","À armatures","Une pièce","Au dessus de lépaule","Col haut","Cravate devant","Volant","Racerback"]
    return random.choice(words)

def special_features_random():
    words = ["Adjustable","Built In Scale","Carry-On","Checkpoint Friendly","Elastic Band","Lightweight","Reversible","Sun Protection","Tsa Lock","Tsa Ready","Wrinkle-Free","Telescoping Handles","Expandable","Includes Card Holders","Includes Coin Pouch","Laptop Compartment","Waterproof","Stretch","Heavy Duty","elastic-band","fade resistant","hypoallergenic","super soft","scented","high color fastness","patterned","low linting","hanging loop","bleach resistant","super absorbent","zero twist","light weight","embroidered","quick dry"]
    return random.choice(words)

def front_style_random():
    words = ["Devant plat","Devant plissé"]
    return random.choice(words)

def rise_style_random():
    words = ["Taille haute","Taille normale","Taille basse"]
    return random.choice(words)

def weave_type_random():
    words = ["Tissé","Tissu tricoté"]
    return random.choice(words)

def collar_style_random():
    words = ["Col boutonné","Col cassé","Col chemise classique","Col chemise italien","Col chemise à patte boutonnée","Col mao","Col rond","Col tunisien","Patte","Straight point","Bouton caché","Club","Boutonné","Cutaway","Wingtip","Étalée","Camp","Bande"]
    return random.choice(words)

def fabric_wash_random():
    words = ["Moyen","Foncé","Léger"]
    return random.choice(words)

def bottom_style_random():
    words = ["Culotte","Jupette","Short","String","Hipster","G-String","Shorts de garçons","Skimpy","Jammer","Bas Bandes","Short de Board","Troncs","Briefs"]
    return random.choice(words)

def leg_style_random():
    words = ["Ankle","Boot Cut","Cropped","Flared","Skinny","Straight","Tapered","Trouser","Wide","Cuffed","Stirrup","Pencil"]
    return random.choice(words)

def strap_type_random():
    words = ["Dos nu","Spaghetti","Amovible","Réglable","Sans bretelles","Une manche"]
    return random.choice(words)

def waist_style_random():
    words = ["Taille basse","Taille haute","Taille normale","Taille très basse"]
    return random.choice(words)

def item_weight_random():
    return random.randint(100, 250)

def occasion_types_random():
    words = [
                "Action de Grâce","Anniversaire","Anniversary","Bal d’anciens élèves","Baptême","Diwali (fête des lumières hindoue)","Douche Nuptiale","Enterrement de Vie de Garçon","Enterrement de Vie de Jeune Fille","Fête de la Saint-Patrick","Fête des Mères","Fête des Pères","Fête Prénatale","Fiançailles","Funérailles","Halloween","Jour de l'Indépendance","Lune de miel","Mariage","Noël","Nouveau-né","Nouvel An","Pâques","Première communion","Quinceañera","Remise des Diplômes","Saint-Valentin"
            ]
    return random.choice(words)

def lifecycle_supply_type_random():
    words = ["Perennial","Year Round Replenishable","Seasonal Basic","Fashion"]
    return random.choice(words)

def fit_type_random():
    words = [ "Coupe athlétique",
  "Coupe régulière",
  "Coupe lâche",
  "Coupe slim", "Coupe classique","Ajustée","Coupe moderne","Coupe surdimensionnée","Coupe décontractée","Coupe semi","Coupe skinny","Coupe tailored"]
    return random.choice(words)

def theme_random():
    words = ["Aliens","Géographie","Personnages de dessins animés","Films","Comédie","Émissions de télévision","Animaux","Vacances","Steampunk","Humoristes","Politiciens","Sports"]
    return random.choice(words)

def lining_description_random():
    words = ["Polyester","Rayonne","Coton","Nylon","Fourrure","Microfibre","Laine","Fausse fourrure","Élasthanne","Soie"]
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
    words = [  "Manches longues",
  "Manches courtes",
  "Sans manche",
  "Manches 3/4",
  "Demi-manche",
  "Manche à volants",
  "Manches chauve-souris",
  "Manches cloche",
  "Manches bouffantes",
  "Manches ballons",
  "Manches à épaules dénudées",
  "Manche kimono",
  "Manches capes",
  "Manchon Transparent",
  "Manche Courte",
  "Manches bouffantes",
  "Manches papillon",
  "Manches raglan",
  "Manches lanterne"]
    return random.choice(words)

def closure_type_random():
    words = ["Button","Pull On","Snap","Zipper","Buckle","Double Ring","Drawstring","Hook and Eye","Hook and Loop"]
    return random.choice(words)

def style_name_random():
    words = ["Asymétrique","Avec boutons","Avec nœud","Avec taille nouée","Body chemise","Bustier","Cache-cœur","Dos nu","Dos ouvert","Empire","Sans bretelle","Tunique","Jerseys","Polo","T-Shirt","Camisole","Robe","Envelopper","Poncho","Paysan","Court","Henley","Longline","Débardeur","À capuche","Découpé","Décontracté","Allaitement","Body","Caftan","Daffaires décontractée","Attaches","Péplum","Blouse","A-Line","Cape","En couches","Boutonné","Batwing","Manches bouffantes","Coupe droite","Volants","Smoking"]
    return random.choice(words)

def seasons_random():
    words = ["automne-hiver","printemps-été"]
    return random.choice(words)

def collection_name_random():
    words = ["Automne-hiver 12","Automne-hiver 13","Automne-hiver 14","Automne-hiver 15","Automne-hiver 16","Automne-hiver 17","Automne-hiver 18","Printemps-été 12","Printemps-été 13","Printemps-été 14","Printemps-été 15","Printemps-été 16","Printemps-été 17","Printemps-été 18"]
    return random.choice(words)

def lifestyle_random():
    words = ["Casual",
  "Cérémonie",
  "Soirée",
  "Ville",
  "Décontracté",
  "Robe",
  "Utilité professionnelle",
  "Athlétique",
  "Uniforme", "Maternité","Allaitement","Survêtement enfant","Exotique","Thème"]
    return random.choice(words)

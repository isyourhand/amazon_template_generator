import random

def material_composition_random():
    words = ["Faux Leather","Polyester","Nylon","Spandex","Polycotton","Leather","Cotton","Suede","Cotton Blend","Silk","Wool Blend","Rayon Blend","Neoprene","Rayon","Polyester Blend","Linen","Rubber","Wool"]
    return random.choice(words)

def outer_material_type_random():
    words = ["Faux Fur","Faux Leather","Fur","Polyester","Nylon","Spandex","Leather","Cotton","Microfiber","Polyurethane","Wool","Acrylic"]
    return random.choice(words)

def item_length_description_random():
    words = ["Maxi","Knee Length","Mini","Above the Knee","Midi","Floor Length","High-Low","Below the Knee","Calf Length","Mid Thigh Length","Ankle Length"]
    return random.choice(words)

def inner_material_type_random():
    words = ["Faux Fur","Faux Leather","Fur","Polyester","Nylon","Spandex","Leather","Cotton","Microfiber","Polyurethane","Wool","Acrylic"]
    return random.choice(words)

def material_type_random():
    words = ["Acrylic","Fur","Latex","Leather","Linen","Neoprene","Nylon","Polyester","Rayon","Silk","Spandex","Suede","Wool"]
    return random.choice(words)

def sport_type_random():
    words = ["Rugby","Trekking","Road Cycling","Badminton","T-Ball","Table Tennis","Wrestling","Cricket","Horse Racing","Sailing","Archery","Swimming","Outdoor Lifestyle","Racing","Cheerleading","Yachting","Boxing","Golf","Triathlon","Bowling","Volleyball","Cyclocross","Ice Diving","Mountaineering","Backcountry Skiing","Kayaking","Ice Skating","Surfing","Walking","Weightlifting","Roller Hockey","Baseball","Canoeing","Running","Yoga","Wakeboarding","Softball","Kitesurfing","Paddle Boarding","Martial Arts","Billiards","Climbing","Airsoft","Basketball","Fishing","Squash","Boating","Workout & Training","Racquetball","Paintball","Snorkeling","Waterskiing","Mountain Biking","Snowboarding","Diving","Water Polo","Windsurfing","Auto Racing","Gymnastics","Multi-Sport","Tennis","Cycling","Hunting","Mixed Martial Arts","Hockey","Snow Skiing","Soccer","Roller Skating","Wiffle ball","BMX","Snowmobiling","Football","Hiking","Rock Climbing","Equestrian","Alpine Skiing","Dance","Lacrosse","Skateboarding","Rafting","Track"]
    return random.choice(words)

# def pattern_name_random():
#     words = ["Animal Print","Argyle","Camouflage","Cartoon","Checkered","Chevron","Floral","Fruits","Geometric","Hearts","Herringbone","Houndstooth","Letter Print","Moire","Paisley","Plaid","Polka Dots","Solid","Stars","Striped"]
#     return random.choice(words)

def pocket_description_random():
    words = ["Cargo Pocket","Coin Pocket","Flap Pocket","Jetted Pocket","Kangaroo Pocket","Patch Pocket","Seam Pocket","Slant Pocket","Slit Pocket","Straight Pocket","Welt Pocket"]
    return random.choice(words)

def top_style_random():
    words = ["Bandeaux","Button Down","Cami","Halter","One Shoulder","Racerback","Strapless/Tube","Tank","Triangle Tops"]
    return random.choice(words)

def belt_style_random():
    words = ["Chain","Medium","Sash/Woven","Skinny","Wide"]
    return random.choice(words)

def special_features_random():
    words = ["Adjustable","Built In Scale","Carry-On","Checkpoint Friendly","Elastic Band","Lightweight","Reversible","Sun Protection","Tsa Lock","Tsa Ready","Wrinkle-Free","Telescoping Handles","Expandable","Includes Card Holders","Includes Coin Pouch","Laptop Compartment","Waterproof","Stretch","Heavy Duty","elastic-band","fade resistant","hypoallergenic","super soft","scented","high color fastness","patterned","low linting","hanging loop","bleach resistant","super absorbent","zero twist","light weight","embroidered","quick dry"]
    return random.choice(words)

def control_type_random():
    words = ["Extra Firm","Firm","Light","Maximum","Medium","Moderate"]
    return random.choice(words)

def front_style_random():
    words = ["Flat Front","Pleated","Pleated Front"]
    return random.choice(words)

def rise_style_random():
    words = ["Ankle","High","Knee High","Low","Mid","Mid-Calf","No Show","Thigh High","Low Rise","Mid Rise","High Rise"]
    return random.choice(words)

def weave_type_random():
    words = ["Woven","Knit"]
    return random.choice(words)

def collar_style_random():
    words = ["Button-Down","Cutaway","Mandarin Collar","Point","Spread","Tab","Club","Hidden Button Down","Wingtip","Band","Straight Point","Camp"]
    return random.choice(words)

def fabric_wash_random():
    words = ["Dark","Light","Medium"]
    return random.choice(words)

def embellishment_feature1_random():
    words = ["Aluminum scales","Metal sheets","Decorative elements"]
    return random.choice(words)

def bottom_style_random():
    words = ["Bikini","Boy Short","Brief","G-String","Hipster","Pant","Short","Skirted","Thong"]
    return random.choice(words)

def leg_style_random():
    words = ["Ankle","Boot Cut","Cropped","Flared","Skinny","Straight","Tapered","Trouser","Wide","Cuffed","Stirrup","Pencil"]
    return random.choice(words)

def strap_type_random():
    words = ["Adjustable","Backless","Basic","Convertible","Halter","Invisible","Racerback","Strapless","compression","flannel-lined","heavyweight","lightweight","lined","midweight","non-breathable","seam-sealed","stretch","tearaway","water-resistant","waterproof","windproof","wrinkle-resistant"]
    return random.choice(words)

def waist_style_random():
    words = ["Medium Waist","High Waist","Low Waist"]
    return random.choice(words)

def item_weight_random():
    return random.randint(100, 250)

def occasion_types_random():
    words = [
                "Christmas", "Wedding", "Cocktail", "Birthday", "Halloween", "Baptism", 
                "Easter", "Graduation", "St.Patricks Day", "Thanksgiving", "Hanukkah", 
                "Memorial Day", "Kwanzaa", "Bachelorette", "Bridal Shower", "Engagement", 
                "Mothers Day", "New Year", "Independence Day", "Valentines Day", "Prom", 
                "Anniversary", "Housewarming", "Festival", "Party", "Mardi Gras", "Reception"
            ]
    return random.choice(words)

def lifecycle_supply_type_random():
    words = ["Perennial","Year Round Replenishable","Fashion"]
    return random.choice(words)

def fit_type_random():
    words = ["Classic Fit","Modern Fit","Oversized Fit","Regular Fit","Relaxed Fit","Semi Fit","Skinny Fit","Tailored Fit"]
    return random.choice(words)

def theme_random():
    words = ["Occupational/Professional","Mascots","Horror","Fairytale","Cartoon","TV & Movies","Famous People","Science Fiction","Western","Superhero","Insects","Sexy","Humorous","Animal","Food & Beverage","Religious","Scary","Classic Monster","Steampunk","Historical & Period","Sports","Geography","Holidays","Aliens","Animals","Cartoon-Characters","Tv Shows","Comedy","Politics","Movies","Comics"]
    return random.choice(words)

def lining_description_random():
    words = ["Faux Fur","Fur","Polyester","Silk","Microfiber","Nylon","Spandex","Rayon","Cotton","Wool"]
    return random.choice(words)

def style_keywords_random():
    words = ["animals","cartoon-characters","comedy","sci-fi","superheroes","steampunk","fairytale","movies-and-tv","pop-culture","anime","food-and-drink","1920s-style","1930s-style","1940s-style","1950s-style","1960s-style","1970s-style","1980s-style","renaissance","western","colonial","prehistoric","vikings","victorian-gothic","firefighters","police","astronauts","religious-themed","school-uniform-costumes","military","angels","clowns","ghosts","french-maid-style","monsters","pirates","vampires","witches","zombies","mummies","ninjas","skeletons","witches-and-wizards","fairies","elves","dragons","mermaids","princess-and-knights","witches-and-wizards","political-leaders","sports","memes","movie-stars"]
    return random.choice(words)

def occasion_random():
    words = ["Anniversary","Baby Shower","Bachelor Party","Bachelorette Party","Baptism","Birthday","Bridal Shower","Christmas","Easter","Engagement","Father's Day","Graduation","Halloween","Honeymoon","Independence Day","Mother's Day","New Baby","New Year","Prom Homecoming","St. Patrick's Day","Thanksgiving","Valentine's Day","Wedding"]
    return random.choice(words)

def neck_style_random():
    words = ["Boat Neck","Choker Neck","Collared Neck","Cowl Neck","Crew Neck","Criss Cross Neck","Halter Neck","Henley Neck","High Neck","Hooded Neck","Jewel Neck","Keyhole Neck","Mandarin Neck","Mock Neck","Notch Neck","Off Shoulder Neck","One Shoulder Neck","Sailor Collar Neck","Scoop Neck","Shawl Neck","Square Neck","Sweetheart Neck","Tie Neck","Turtle Neck","V Neck"]
    return random.choice(words)

def sleeve_type_random():
    words = ["Balloon Sleeve","Batwing Sleeve","Bell Sleeve","Bishop Sleeve","Butterfly Sleeve","Cap Sleeve","Cape Sleeve","Cold Shoulder Sleeve","Cuff Sleeve","Flutter Sleeve","Kimono Sleeve","Lantern Sleeve","Leg-of-Mutton Sleeve","Puff Sleeve","Raglan Sleeve","Ruffle Sleeve","Split Sleeve"]
    return random.choice(words)

def closure_type_random():
    words = ["Button","Pull On","Snap","Zipper","Buckle","Double Ring","Drawstring","Hook and Eye","Hook and Loop"]
    return random.choice(words)

def style_name_random():
    words = ["Balconette","Classic","Demi","Double-Breasted","Full Coverage","Modern/Fitted","Molded","Padded","Plunge","Push-Up","Seamless","Soft"]
    return random.choice(words)


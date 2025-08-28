import random

def material_composition_random():
    words = ["Faux Leather","Polyester","Nylon","Spandex","Polycotton","Leather","Cotton","Suede","Cotton Blend","Silk","Wool Blend","Rayon Blend","Neoprene","Rayon","Polyester Blend","Linen","Rubber","Wool"]
    return random.choice(words)

def outer_material_type_random():
    words = ["Alpaca","Angora","Cashmere","Corduroy","Cotton","Denim","Down","Faux Fur","Felt","Fleece","Fur","Hemp","Leather","Linen","Merino","Mohair","Patent Leather","Rubber","Satin","Sequined","Silk","Smooth Leather","Suede","Synthetic","Velvet","Wool","Sequinned"]
    return random.choice(words)

def item_length_description_random():
    words = ["Knee-Long","Maxi","Midi","Mini","Knee Length","Above the Knee","Floor Length","High-Low","Below the Knee","Calf Length","Mid Thigh Length","Ankle Length","Mid-Thigh"]
    return random.choice(words)

def inner_material_type_random():
    words = ["Alpaca","Angora","Cashmere","Corduroy","Cotton","Denim","Down","Faux Fur","Felt","Fleece","Fur","Hemp","Leather","Linen","Merino","Mohair","Patent Leather","Rubber","Satin","Sequined","Silk","Smooth Leather","Suede","Synthetic","Velvet","Wool","Sequinned"]
    return random.choice(words)

def material_type_random():
    words = ["Acrylic","Elastane","Fur","Leather","Linen","Neoprene","Nylon","Polyester","Raw Silk","Rubber","Silk","Suede","Viscose","Wool"]
    return random.choice(words)

def sport_type_random():
    words = ["Rugby","Trekking","Road Cycling","Badminton","T-Ball","Table Tennis","Wrestling","Cricket","Horse Racing","Sailing","Archery","Swimming","Outdoor Lifestyle","Racing","Cheerleading","Yachting","Boxing","Golf","Triathlon","Bowling","Volleyball","Cyclocross","Ice Diving","Mountaineering","Backcountry Skiing","Kayaking","Ice Skating","Surfing","Walking","Weightlifting","Roller Hockey","Baseball","Canoeing","Running","Yoga","Wakeboarding","Softball","Kitesurfing","Paddle Boarding","Martial Arts","Billiards","Climbing","Airsoft","American Football","Basketball","Fishing","Squash","Boating","Workout & Training","Racquetball","Paintball","Snorkeling","Waterskiing","Mountain Biking","Snowboarding","Diving","Water Polo","Windsurfing","Auto Racing","Gymnastics","Multi-Sport","Tennis","Cycling","Hunting","Mixed Martial Arts","Hockey","Snow Skiing","Soccer","Roller Skating","Wiffle ball","BMX","Snowmobiling","Hiking","Rock Climbing","Equestrian","Alpine Skiing","Dance","Lacrosse","Skateboarding","Rafting","Track"]
    return random.choice(words)

# def pattern_name_random():
#     words = ["Animal Print","Argyle","Camouflage","Cartoon","Checkered","Chevron","Floral","Fruits","Geometric","Hearts","Herringbone","Houndstooth","Letter Print","Moire","Paisley","Plaid","Polka Dots","Solid","Stars","Striped"]
#     return random.choice(words)

def pocket_description_random():
    words = ["Cargo Pocket","Flap Pocket","Jetted Pocket","Kangaroo Pocket","Patch Pocket","Seam Pocket","Slant Pocket","Slit Pocket","Straight Pocket","Welt Pocket"]
    return random.choice(words)

def top_style_random():
    words = ["Button Down","Cami","Halter","One Shoulder","Racerback","Strapless/Tube","Bralette","Off The Shoulder","High Neck","Flared","Crossback","Rashguard","Tankini","Monokini","Longline","Bandeau","Push Up"]
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
    words = ["Flat Front","Pleated Front"]
    return random.choice(words)

def rise_style_random():
    words = ["Low Rise","Mid Rise","High Rise"]
    return random.choice(words)

def weave_type_random():
    words = ["Woven","Knit"]
    return random.choice(words)

def collar_style_random():
    words = ["Button Down","Classic","Cutaway","Grandad","Mao","Round Collar","Tab Collar","Wing Collar","Spread","Tab","Club","Hidden Button Down","Wingtip","Band","Straight Point","Camp"]
    return random.choice(words)

def fabric_wash_random():
    words = ["Dark","Light","Medium"]
    return random.choice(words)

def embellishment_feature1_random():
    words = ["Aluminum scales","Metal sheets","Decorative elements"]
    return random.choice(words)

def bottom_style_random():
    words = ["Briefs","Shorts","Skirted","String","Hipster","Board Shorts","G-String","Trunk","Skimpy","Jammer","Banded Bottoms","Boy Shorts"]
    return random.choice(words)

def leg_style_random():
    words = ["Ankle","Boot Cut","Cropped","Flared","Skinny","Straight","Tapered","Trouser","Wide","Cuffed","Stirrup","Pencil"]
    return random.choice(words)

def strap_type_random():
    words = ["One shoulder","Removable","Spaghetti","Halter","Strapless","Adjustable"]
    return random.choice(words)

def waist_style_random():
    words = ["High","Low","Regular","Very Low"]
    return random.choice(words)

def item_weight_random():
    return random.randint(100, 250)

def occasion_types_random():
    words = [
                "Anniversary","Baby Shower","Bachelor Party","Bachelorette Party","Baptism","Birthday","Bridal Shower","Christmas","Communion","Diwali","Easter","Engagement","Father's Day","Funeral","Graduation","Halloween","Honeymoon","Independence Day","Mother's Day","New Baby","New Year","Prom Homecoming","Quinceanera","St. Patrick's Day","Thanksgiving","Valentine's Day","Wedding"
            ]
    return random.choice(words)

def lifecycle_supply_type_random():
    words = ["Perennial","Year Round Replenishable","Seasonal Basic","Fashion"]
    return random.choice(words)

def fit_type_random():
    words = ["Athletic Fit", "Fitted", "Loose Fit", "Slim Fit", "Classic Fit","Modern Fit","Oversized Fit","Regular Fit","Relaxed Fit","Semi Fit","Skinny Fit","Tailored Fit"]
    return random.choice(words)

def theme_random():
    words = ["Geography","Aliens","Films","TV Programmes","Holidays","Animals","Cartoon-Characters","Comedy","Politics","Steampunk","Comics","Sports"]
    return random.choice(words)

def lining_description_random():
    words = ["Faux Fur","Fur","Polyester","Silk","Nylon","Spandex","Microfibre","Rayon","Cotton","Wool"]
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
    words = ["Asymmetric","Backless","Body Blouse","Bow Front","Bustier","Button Down","Empire","Halterneck","Strapless","Tie-Waist","Tunic","Wrap","Jerseys","Tie- Ups","Polo","Cropped","T-Shirt","Camisole","Regular","Poncho","Henley","Longline","Peasant","Dress","Ruffles","Tuxedo","Blouse","Button Up","Layered","A-Line","Bodysuit","Casual","Cut Out","Cape","Puff Sleeve","Tank","Peplum","Kaftan","Nursing","Hooded","Business Casual","Batwing","Cold Shoulder"]
    return random.choice(words)

def collection_name_random():
    words = ["Autumn-Winter 12","Autumn-Winter 13","Autumn-Winter 14","Autumn-Winter 15","Autumn-Winter 16","Autumn-Winter 17","Autumn-Winter 18","Spring-Summer 12","Spring-Summer 13","Spring-Summer 14","Spring-Summer 15","Spring-Summer 16","Spring-Summer 17","Spring-Summer 18"]
    return random.choice(words)

def fabric_type_random():
    words = ["Polyester","Nylon","Spandex","Polycotton","Leather","Spandex Blend","Cashmere","Linen Blend","Cotton","Cotton Blend","Silk","Wool Blend","Rayon Blend","Rayon","Polyester Blend","Linen","Modal","Wool"]
    return random.choice(words)

def special_features5_random():
    words = ["Moisture Wicking","Sun Protection","Absorbant","Convertible","Reversible","Stretchable","Sustainable","Wrinkle Free"]
    return random.choice(words)
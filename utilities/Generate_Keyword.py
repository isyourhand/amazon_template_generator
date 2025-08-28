import random
from utilities.Calculate import format_fabric_string

def remove_duplicates(text):
    seen = set()
    result = []
    for word in text.split():
        if word not in seen:
            seen.add(word)
            result.append(word)
    return ' '.join(result)

def generate_Title(key_word_title1, key_word_title2, type, pattern, color, size, fabric, title_include_fields):
    _fabric_ = format_fabric_string(fabric)

    if not key_word_title1 and not key_word_title2:
        return ""
    
    title1 = random.choice(key_word_title1)

    title_detail = ""
    if title_include_fields.get("fabric", True):
        title_detail += " " + _fabric_
    if title_include_fields.get("color", True):
        title_detail += " " + color
    if title_include_fields.get("pattern", True):
        title_detail += " " + pattern
    if title_include_fields.get("type", True):
        title_detail += " " + type.title()

    # 构造 title2 - 改进部分
    title2 = ""
    remaining_keywords = key_word_title2.copy()  # 创建副本以避免修改原列表
    
    while remaining_keywords:
        # 随机选择一个关键词并从剩余列表中移除
        chosen_keyword = random.choice(remaining_keywords)
        remaining_keywords.remove(chosen_keyword)
        
        # 构建临时标题
        temp_title2 = f"{title2} {chosen_keyword}".strip() if title2 else chosen_keyword
        
        # 检查长度
        if len(f"{title1} {temp_title2} {size}") > 114:
            break
            
        title2 = temp_title2
    
    # 组合最终标题
    if title_include_fields.get("position", True):
        combined_title = f"{title1} - {title2}".strip()
    else:
        combined_title = f"{title1} - {title2}".strip()
    
    final_title = remove_duplicates(combined_title)

    return f"{final_title} - {color} {size}"

# Random bullet
def generate_Bullet(key_word_descri1, key_word_descri2):
        if not key_word_descri1 and not key_word_descri2:
             return ""
        
        descri1_part = random.choice(key_word_descri1)
        while len(descri1_part) < 300:
            next_descri = " " + random.choice(key_word_descri1)
            if len(descri1_part + next_descri) <= 300:
                descri1_part += next_descri
            else:
                break
        
        # Fill remaining up to 500 characters from key_word_descri2
        descri2_part = random.choice(key_word_descri2)
        while len(descri1_part + descri2_part) < 499:
            next_descri = " " + random.choice(key_word_descri2)
            if len(descri1_part + descri2_part + next_descri) <= 499:
                descri2_part += next_descri
            else:
                break
        
        combined_descri = (descri1_part + " " + descri2_part).strip()
        return combined_descri

# Random Generic
def generate_Generic(key_word_descri1, key_word_descri2):
        if not key_word_descri1 and not key_word_descri2:
             return ""

        descri1_part = random.choice(key_word_descri1)
        while len(descri1_part) < 150:
            next_descri = " " + random.choice(key_word_descri1)
            if len(descri1_part + next_descri) <= 150:
                descri1_part += next_descri
            else:
                break
        
        # Fill remaining up to 500 characters from key_word_descri2
        descri2_part = random.choice(key_word_descri2)
        while len(descri1_part + descri2_part) < 249:
            next_descri = " " + random.choice(key_word_descri2)
            if len(descri1_part + descri2_part + next_descri) <= 249:
                descri2_part += next_descri
            else:
                break
        
        combined_descri = (descri1_part + " " + descri2_part).strip()
        return combined_descri

def customize_Generation(key_word_title1, key_word_title2, length):
        if not key_word_title1 and not key_word_title2:
             return ""
        
        title1 = random.choice(key_word_title1)

        # 构造 title2
        title2 = ""
        while True:
            temp_title2 = title2 + " " + random.choice(key_word_title2) if title2 else random.choice(key_word_title2)
            if len(title1 + " " + temp_title2) > length:
                break
            title2 = temp_title2
        
        combined_title = f"{title1} {title2}"
        
        return combined_title
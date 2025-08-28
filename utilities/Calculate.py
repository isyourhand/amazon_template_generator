
import re
from datetime import datetime, timedelta
from openpyxl.styles import NamedStyle

def get_Price(data):
    # 去除所有英文字母
    data = re.sub(r'[A-Za-z]', '', data)

    # 初始化哈希表
    hash_map = {}

    # 匹配模式：国家名称、金额和货币单位
    pattern = r"([\u4e00-\u9fa5]+)：([\d\.]+)"

    # 查找所有匹配项
    matches = re.findall(pattern, data)

    # 填充哈希表
    for country, value in matches:
        hash_map[country] = value

    return hash_map

def calculate_Price(x, shipping_cost, profit):
    # 计算初步价格
    price = float(x) * 0.78 / (1 - float(profit)) - float(shipping_cost)
    
    # 将价格调整为以 .99 结尾
    price = round(price) - 1 + 0.99
    
    # 计算总价（价格 + 运费）
    total_price = price + float(shipping_cost)
    
    # 根据总价调整价格
    if total_price < 7.99:
        price += 2
    elif total_price < 8.99:
        price += 1

    if total_price > 19.97:
        price -= 3
    elif total_price > 17.97:
        price -= 2
    elif total_price > 16.97:
        price -= 1

    total_price = price + float(shipping_cost)
    if total_price > 15 and total_price < 15:
        price -= 1
    
    return price

def replace_Url(url,new_host):
    # 使用正则表达式替换 URL 中的主机部分
    new_url = re.sub(r'http://([\d.]+)/', f'http://{new_host}/', url)
    return new_url

def current_Time():
    now = datetime.now() - timedelta(days=1)
    return now.date()

def sale_End_Time():
    end_time = datetime.now() + timedelta(days=45)
    return end_time.date()


def format_fabric_string(input_string):
    # 1. 处理逗号和空格，确保逗号后有一个空格
    # input_string = re.sub(r'\s*[，,]\s*', ', ', input_string.strip())  # 统一逗号两边的空格

    # 2. 格式化每个材料成正确的形式
    def format_match(match):
        percentage = match.group(1)
        material = match.group(2).capitalize()
        return f"{percentage} {material}" if percentage else material

    formatted = re.sub(r'(\d+%)?\s*([a-zA-Z]+)', format_match, input_string)

    # 3. 再次检查逗号和空格
    formatted = re.sub(r'\s*[，,]\s*', ' and ', formatted)  # 确保逗号后有空格

    return formatted

def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)

def fabric_add_prefix(text):
    # 允许的标点符号集合
    allowed_punctuation = {'.', ',', '!', '?', ';', ':', '\'', '"', '-', '(', ')'}
    
    # 检查字符串是否只包含字母、标点符号和空格
    if all(char.isalpha() or char.isspace() or char in allowed_punctuation for char in text):
        return "100% " + text
    else:
        return text
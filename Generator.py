import os
import sys
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import messagebox, ttk
from utilities.excelDataProcess.ExcelDataProcess_us import copy_data
from utilities.excelDataProcess.ExcelDataProcess_de import copy_data_de
from utilities.excelDataProcess.ExcelDataProcess_fr import copy_data_fr
from utilities.excelDataProcess.ExcelDataProcess_ca import copy_data_ca
from utilities.excelDataProcess.ExcelDataProcess_uk import copy_data_uk

# Constants
DEFAULT_SITE = "美国"
DEFAULT_CATEGORY = "衬衫"
DEFAULT_TARGET_AUDIENCE = "女士"
DEFAULT_AGE_GROUP = "成人"
DEFAULT_GENDER = "女士"
DEFAULT_NECK_STYLE = "圆领"
DEFAULT_PATTERN_STYLE = "纯色"
DEFAULT_CLOSURE_TYPE = "穿上"
DEFAULT_SLEEVE_TYPE = "长袖"


# 获取资源文件路径
def resource_path(relative_path):
    """获取打包后资源文件的路径"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# 全局变量
target_file_path = None
source_file_path = None

def parse_textbox_content(textbox):
    content = textbox.get("1.0", tk.END).strip()
    return content.split("\n") if content else []

def on_drop_target(event):
    global target_file_path
    target_file_path = get_cleaned_path(event.data)
    label_target.config(text=f"目标文件已拖入: {os.path.basename(target_file_path)}")

def on_drop_source(event):
    global source_file_path
    source_file_path = get_cleaned_path(event.data)
    label_source.config(text=f"源文件已拖入: {os.path.basename(source_file_path)}")

def get_cleaned_path(file_path):
    return file_path[1:-1] if file_path.startswith('{') and file_path.endswith('}') else file_path

def handle_copy_data():
    global target_file_path, source_file_path

    if not target_file_path or not source_file_path:
        messagebox.showerror("错误", "请确保两个文件都已拖入")
        return

    prefix = prefix_entry.get().strip()
    url_prefix = url_prefix_entry.get().strip()
    shipping_cost = shipping_cost_entry.get().strip()
    brand = brand_entry.get().strip()
    profit = profit_entry.get().strip()
    gpsr = gpsr_entry.get().strip()

    if not all([prefix, url_prefix, shipping_cost, brand, profit]):
        messagebox.showerror("错误", "以下字段不能为空：\n" + 
                           (not prefix and "- 前缀\n" or "") +
                           (not url_prefix and "- 网址前缀\n" or "") +
                           (not shipping_cost and "- 运费模板\n" or "") +
                           (not brand and "- 品牌名\n" or "") +
                           (not profit and "- 利润率\n" or ""))
        return
    
    key_word_array1 = parse_textbox_content(textbox1)
    key_word_array2 = parse_textbox_content(textbox2)
    key_word_array3 = parse_textbox_content(textbox3)
    key_word_array4 = parse_textbox_content(textbox4)
    nodes_array = parse_textbox_content(nodes)

    if not all([key_word_array1, key_word_array2, key_word_array3, key_word_array4, nodes_array]):
        messagebox.showerror("错误", "以下文本框不能为空：\n" +
                           (not key_word_array1 and "- 子标题开头关键词\n" or "") +
                           (not key_word_array2 and "- 子标题身体关键词\n" or "") +
                           (not key_word_array3 and "- 五点介绍1（前半部分）\n" or "") +
                           (not key_word_array4 and "- 五点介绍2（后半部分）\n" or "") +
                           (not nodes_array and "- 节点\n" or ""))
        return

    product_Type = category_var.get()
    department_name = department_name_var.get()
    site = site_var.get()
    age_group = age_group_var.get()
    gender = gender_var.get()
    closure_type = closure_type_var.get()
    neck_style = neckStyle_var.get()
    
    seasons = [season for season, var in season_vars.items() if var.get()]
    patterns = [pattern for pattern, var in pattern_style_vars.items() if var.get()]
    
    # Validate checkbox selections
    empty_arrays = []
    if not seasons: empty_arrays.append("季节")
    if not patterns: empty_arrays.append("图案")
       
    if empty_arrays:
        messagebox.showerror("错误", "请至少选择一个选项：\n- " + "\n- ".join(empty_arrays))
        return

    title_include_fields = {key: var.get() for key, var in title_check_vars.items()}

    if site == "美国":
        copy_data(target_file_path, source_file_path, prefix, url_prefix,
                brand, site,
                key_word_array1, key_word_array2, key_word_array3, key_word_array4,
                product_Type, seasons, department_name, age_group, gender,
                patterns, nodes_array,
                shipping_cost, title_include_fields, profit)
    if site == "德国":
        copy_data_de(target_file_path, source_file_path, prefix, url_prefix,
                brand, site,
                key_word_array1, key_word_array2, key_word_array3, key_word_array4,
                product_Type, seasons, department_name, age_group, gender,
                patterns, nodes_array,
                shipping_cost, title_include_fields, closure_type, profit, gpsr, neck_style)
    if site == "法国":
        copy_data_fr(target_file_path, source_file_path, prefix, url_prefix,
                brand, site,
                key_word_array1, key_word_array2, key_word_array3, key_word_array4,
                product_Type, seasons, department_name, age_group, gender,
                patterns, nodes_array,
                shipping_cost, title_include_fields, closure_type, profit, gpsr, neck_style)
    if site == "英国":
        copy_data_uk(target_file_path, source_file_path, prefix, url_prefix,
                brand, site,
                key_word_array1, key_word_array2, key_word_array3, key_word_array4,
                product_Type, seasons, department_name, age_group, gender,
                patterns, nodes_array,
                shipping_cost, title_include_fields, profit, neck_style, closure_type)
    if site == "加拿大":
        copy_data_ca(target_file_path, source_file_path, prefix, url_prefix,
                brand, site,
                key_word_array1, key_word_array2, key_word_array3, key_word_array4,
                product_Type, seasons, department_name, age_group, gender,
                patterns, nodes_array,
                shipping_cost, title_include_fields, profit)


def create_label_and_combobox(frame, label_text, options, default_value):
    label = tk.Label(frame, text=label_text, pady=10)
    label.pack()
    var = tk.StringVar(value=default_value)
    combobox = ttk.Combobox(frame, textvariable=var, values=options, state="readonly")
    combobox.pack(pady=10)
    return var

# 创建主窗口
root = TkinterDnD.Tk()
root.title('模板生成')
root.geometry('500x600')

icon_path = resource_path("resources/catai_0BD_icon.ico")
root.iconbitmap(icon_path)

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(main_frame)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

def on_mouse_wheel(event):
    if sys.platform.startswith('win'):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")
    else:
        canvas.yview_scroll(-1 if event.delta > 0 else 1, "units")

root.bind_all("<MouseWheel>", on_mouse_wheel)

site_var = create_label_and_combobox(scrollable_frame, "选择站点:", ["美国", "德国", "法国", "英国", "加拿大"], DEFAULT_SITE)

label_target = tk.Label(scrollable_frame, text="拖拽目标 XLSX 文件到这里 (框 A)", pady=10)
label_target.pack()
frame_target = tk.Frame(scrollable_frame, width=400, height=50, bg="lightblue")
frame_target.pack(pady=10)
frame_target.drop_target_register(DND_FILES)
frame_target.dnd_bind('<<Drop>>', on_drop_target)

label_source = tk.Label(scrollable_frame, text="拖拽源 XLSX 文件到这里 (框 B)", pady=10)
label_source.pack()
frame_source = tk.Frame(scrollable_frame, width=400, height=50, bg="lightgreen")
frame_source.pack(pady=10)
frame_source.drop_target_register(DND_FILES)
frame_source.dnd_bind('<<Drop>>', on_drop_source)

prefix_label = tk.Label(scrollable_frame, text="输入前缀 (仅字母和数字):", pady=10)
prefix_label.pack()
prefix_entry = tk.Entry(scrollable_frame)
prefix_entry.pack()

url_prefix_label = tk.Label(scrollable_frame, text="输入网址前缀:", pady=10)
url_prefix_label.pack()
url_prefix_entry = tk.Entry(scrollable_frame)
url_prefix_entry.pack()

shipping_cost_label = tk.Label(scrollable_frame, text="输入运费模板:", pady=10)
shipping_cost_label.pack()
shipping_cost_entry = tk.Entry(scrollable_frame)
shipping_cost_entry.pack()
shipping_cost_entry.insert(0, "3.99")

brand_label = tk.Label(scrollable_frame, text="输入品牌名:", pady=10)
brand_label.pack()
brand_entry = tk.Entry(scrollable_frame)
brand_entry.pack()
brand_entry.insert(0, "Generic")

profit_label = tk.Label(scrollable_frame, text="输入利润率（8%=0.08）:", pady=10)
profit_label.pack()
profit_entry = tk.Entry(scrollable_frame)
profit_entry.pack()
profit_entry.insert(0, "0.08")

gpsr_label = tk.Label(scrollable_frame, text="输入GPSR图片地址（欧洲站点填写）:", pady=10)
gpsr_label.pack()
gpsr_entry = tk.Entry(scrollable_frame)
gpsr_entry.pack()


# Add textboxes
def create_textbox(frame, label_text):
    label = tk.Label(frame, text=label_text, pady=10)
    label.pack()
    textbox = tk.Text(frame, height=5, width=50)
    textbox.pack()
    return textbox

textbox1 = create_textbox(scrollable_frame, "粘贴关键词数据到此框（子标题开头）")
# 标题选项
fields = ["fabric", "color", "pattern", "type", "position"]
title_check_vars = {field: tk.BooleanVar(value=True) for field in fields}
tk.Checkbutton(scrollable_frame, text="材质", variable=title_check_vars["fabric"]).pack()
tk.Checkbutton(scrollable_frame, text="颜色", variable=title_check_vars["color"]).pack()
tk.Checkbutton(scrollable_frame, text="图案", variable=title_check_vars["pattern"]).pack()
tk.Checkbutton(scrollable_frame, text="产品类型", variable=title_check_vars["type"]).pack()
tk.Checkbutton(scrollable_frame, text="放置位置（勾选会放在子标题开头后否则放在最后面）", variable=title_check_vars["position"]).pack()
textbox2 = create_textbox(scrollable_frame, "粘贴关键词数据到此框（子标题身体）")
textbox3 = create_textbox(scrollable_frame, "粘贴关键词数据到此框（五点，介绍）1")
textbox4 = create_textbox(scrollable_frame, "粘贴关键词数据到此框（五点，介绍）2")
nodes = create_textbox(scrollable_frame, "粘贴节点到此框:")

category_var = create_label_and_combobox(scrollable_frame, "选择商品类别:", [
    "衬衫", "长款上衣", "运动衫", "背心", "连衣裙", "半身裙", "外套", 
    "罩衫", "夹克", "裤子", "短裤", "毛衣", "领带", "内裤", "泳装", 
    "袜子", "内衣", "睡袍", "睡衣两件套", "睡衣", "套装", "长袍", "胸罩", 
    "帽子", "围巾", "背包", "手提袋", "腰带", "手套", "配饰", "民族服装"
], DEFAULT_CATEGORY)

closure_type_var = create_label_and_combobox(scrollable_frame, "关闭类型:", [
    "穿上", "拉链", "按钮", "无关闭", "绑上", "系腰带", "扣上", "拉绳", "钩"
], DEFAULT_CLOSURE_TYPE)

department_name_var = create_label_and_combobox(scrollable_frame, "选择目标人群:", [
    "女士", "男士", "男女通用", "女孩", "男孩", "男女孩通用", "女婴", "男婴", "男女婴通用"
], DEFAULT_TARGET_AUDIENCE)

age_group_var = create_label_and_combobox(scrollable_frame, "适用年龄:", [
    "成人", "大孩子", "孩子", "小孩", "学步的儿童", "婴儿", "新生"
], DEFAULT_AGE_GROUP)

gender_var = create_label_and_combobox(scrollable_frame, "适用性别:", [
    "女士", "男士", "男女通用"
], DEFAULT_GENDER)

neckStyle_var = create_label_and_combobox(scrollable_frame, "领口类型:", [
    "圆领", "V领", "船领", "连帽", "露肩", "单肩领", "高领", "无肩带/抹胸", "挂脖露背（Halter）", "T形背",
    "U型领", "斜领", "不对称领口", "含孔领", "Polo领", "Henley领", "纽扣", "网孔领", "半拉链",
    "方领", "半高圆领", "心形颈", "开叉领", "披肩领", "无领领口"
], DEFAULT_NECK_STYLE)


# Add checkboxes
def create_checkboxes(frame, label_text, options):
    label = tk.Label(frame, text=label_text)
    label.pack(pady=(10, 0))
    vars = {}
    for option in options:
        vars[option] = tk.IntVar()
        tk.Checkbutton(frame, text=option, variable=vars[option]).pack()
    return vars

season_vars = create_checkboxes(scrollable_frame, "选择适用季节:", ["春天", "夏天", "秋天", "冬天"])
pattern_style_vars = create_checkboxes(scrollable_frame, "选择图案:", ["纯色", "简朴", "条纹", "有图案", "文字", "带花图案", "动物图案", "格子", "扎染", 
    "豹纹", "迷彩", "佩斯利纹", "波尔卡圆点", "几何", "星星图案", "水波纹",
    "锯齿纹", "植物图案", "菱形格", "水果", "水果和蔬菜", "拼色", "银河", "圣诞节", "卡通", "犬牙花纹", 
    "爱心", "鱼骨纹", "蛇皮图案", "钻石"])


copy_button = tk.Button(scrollable_frame, text="复制数据到目标文件", command=handle_copy_data)
copy_button.pack(pady=20)

root.mainloop()

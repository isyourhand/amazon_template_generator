import os
import sys
import tkinter as tk
from tkinter import messagebox
import subprocess

# 获取资源路径
def resource_path(relative_path, is_executable=False):
    """根据文件类型返回正确的路径
    - `relative_path`: 相对路径
    - `is_executable`: 是否为可执行文件
    """
    try:
        if getattr(sys, 'frozen', False):
            # 打包后的情况
            if hasattr(sys, '_MEIPASS'):
                # PyInstaller: 资源文件从 _MEIPASS 加载
                if not is_executable:
                    return os.path.join(sys._MEIPASS, relative_path)
            # 可执行文件与主程序在同一目录 (适用于所有打包工具)
            base_dir = os.path.dirname(sys.executable)
            return os.path.join(base_dir, relative_path)
        else:
            # 开发模式下的路径
            return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
    except Exception as e:
        messagebox.showerror("路径错误", f"获取路径失败: {e}")
        return None

# 运行子程序
def run_script_or_exe(script_name, exe_name):
    try:
        if getattr(sys, 'frozen', False):
            # 打包后运行 .exe
            exe_path = resource_path(exe_name, is_executable=True)
            if not exe_path or not os.path.exists(exe_path):
                raise FileNotFoundError(f"可执行文件未找到: {exe_name}")
            subprocess.Popen([exe_path], creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            # 未打包时运行 .py
            script_path = resource_path(script_name)
            if not script_path or not os.path.exists(script_path):
                raise FileNotFoundError(f"脚本文件未找到: {script_name}")
            subprocess.Popen([sys.executable, script_path])
    except FileNotFoundError as fnfe:
        messagebox.showerror("文件未找到", str(fnfe))
    except Exception as e:
        messagebox.showerror("运行错误", f"运行子程序时发生错误: {e}")

# 创建主窗口
def main():
    try:
        root = tk.Tk()
        root.title("选择模板生成")
        root.geometry("300x150")

        # 设置图标
        icon_path = resource_path("resources/catai_0BD_icon.ico")
        if icon_path and os.path.exists(icon_path):
            try:
                root.iconbitmap(icon_path)
            except Exception as e:
                print(f"设置窗口图标失败: {e}")  # 使用print而不是弹窗，避免循环弹窗
        else:
            print("图标文件不存在，程序将继续运行。")

        # 按钮配置
        buttons = [
            ("NEW", "Generator.py", "Generator.exe"),
            ("下装", "bottom.py", "bottom.exe")
        ]

        # 使用循环创建按钮
        for text, script, exe in buttons:
            btn = tk.Button(root, text=text, command=lambda s=script, e=exe: run_script_or_exe(s, e), width=20, height=2)
            btn.pack(pady=10)

        # 运行主窗口事件循环
        root.mainloop()
    except Exception as e:
        messagebox.showerror("主程序错误", f"程序运行时发生错误: {e}")

if __name__ == "__main__":
    main()
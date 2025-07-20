# 导入区

import time
import sys
import os
import requests


# 函数区

def run_software():
    """运行软件，显示进入提示和进度条"""
    # 显示欢迎信息
    print("欢迎使用本软件！")
    print("正在加载中...")
    time.sleep(0.5)
    
    # 模拟软件加载过程
    total_steps = 100
    for i in range(total_steps + 1):
        # 计算进度百分比
        percent = i / total_steps
        # 计算进度条填充长度
        bar_length = 50
        filled_length = int(bar_length * percent)
        # 生成进度条字符串
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        # 显示进度条（覆盖上一行）
        sys.stdout.write(f'\r[{bar}] {percent:.1%}')
        sys.stdout.flush()
        # 控制进度条更新速度
        time.sleep(0.02)
    print("\n加载完成！")
    time.sleep(0.5) 
    

# 运行区

run_software()

while True:
    try:
        # 软件主界面
        print("\n===================================")
        print("        软件主界面")
        print("===================================")
        print("1. 功能一")
        print("2. 功能二")
        print("3. 功能三")
        print("4.更新软件到最新版本")
        print("5. 退出软件")
        print("===================================")
        choice = input('请输入选项: ').strip()  # 增加strip()处理空白字符
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            print("正在更新软件到最新版本...")
            time.sleep(1.5)
            print("软件已更新到最新版本！")
            time.sleep(0.5)
        elif choice == "5":
            print("感谢使用，再见！")
            time.sleep(0.3)
            break
        else:
            print("无效的选择，请重新输入")
            continue
    except:
        print("软件发生错误，请重试，或与开发者联系。")
        print("\n===================================")
        time.sleep(1.5)
        print("\n\n\n\n===================================")
        continue
#!/usr/bin/env python3
"""
💖 爱心系列完整启动器
包含所有爱心动画和交互页面的启动菜单
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def clear_screen():
    """清屏函数"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    """显示主菜单"""
    print("=" * 60)
    print("💕 爱心系列完整启动器 💕")
    print("=" * 60)
    print("请选择要体验的内容：")
    print()
    print("🎮 动画类：")
    print("1. Pygame粒子爱心动画")
    print("2. Tkinter基础爱心动画")
    print("3. Tkinter增强版爱心动画 (推荐)")
    print()
    print("💌 交互类：")
    print("4. 趣味交互爱心页面 (HTML)")
    print()
    print("📚 其他：")
    print("5. 查看项目说明")
    print("6. 安装依赖")
    print("0. 退出")
    print("=" * 60)

def check_file_exists(filename):
    """检查文件是否存在"""
    return Path(filename).exists()

def run_python_script(script_name):
    """运行Python脚本"""
    try:
        print(f"正在启动 {script_name}...")
        result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"运行 {script_name} 时出错:")
            print(result.stderr)
            input("按回车键继续...")
    except Exception as e:
        print(f"运行 {script_name} 失败: {e}")
        input("按回车键继续...")

def open_html_file(filename):
    """打开HTML文件"""
    try:
        # 尝试启动本地服务器
        print(f"正在为 {filename} 启动本地服务器...")
        server_process = subprocess.Popen([sys.executable, "-m", "http.server", "8080"], 
                                        stdout=subprocess.DEVNULL, 
                                        stderr=subprocess.DEVNULL)
        
        # 等待服务器启动
        import time
        time.sleep(1)
        
        # 打开浏览器
        url = f"http://localhost:8080/{filename}"
        print(f"正在打开浏览器访问: {url}")
        webbrowser.open(url)
        
        print("网页已打开！按回车键返回主菜单（注意：服务器会继续运行）")
        input()
        
        # 注意：我们不关闭服务器，让用户可以继续使用
        return server_process
        
    except Exception as e:
        print(f"打开 {filename} 失败: {e}")
        print("尝试直接打开文件...")
        try:
            webbrowser.open(filename)
        except:
            print("无法打开文件，请手动打开文件或检查依赖")
        input("按回车键继续...")

def show_project_info():
    """显示项目信息"""
    clear_screen()
    print("=" * 60)
    print("📚 项目说明")
    print("=" * 60)
    print()
    print("💕 爱心系列项目包含以下内容：")
    print()
    print("1. 动画类（Python）：")
    print("   • particle_heart.py - Pygame粒子爱心")
    print("   • advanced_heart.py - Tkinter基础爱心")
    print("   • enhanced_heart.py - Tkinter增强版")
    print()
    print("2. 交互类（HTML）：")
    print("   • interactive_love.html - 趣味交互页面")
    print()
    print("3. 文档类：")
    print("   • README_ADVANCED.md - 动画项目说明")
    print("   • README_INTERACTIVE.md - 交互页面说明")
    print()
    print("4. 工具类：")
    print("   • requirements.txt - 依赖列表")
    print("   • complete_launcher.py - 本启动器")
    print()
    print("🎯 使用建议：")
    print("   • 新手推荐：先体验交互页面，再看增强版动画")
    print("   • 技术学习：对比不同版本的实现方式")
    print("   • 表白用途：交互页面 + 增强版动画组合使用")
    print()
    input("按回车键返回主菜单...")

def install_dependencies():
    """安装依赖"""
    print("正在安装依赖...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ 依赖安装完成！")
    except subprocess.CalledProcessError:
        print("❌ 依赖安装失败，请手动安装：")
        print("pip install -r requirements.txt")
    input("按回车键继续...")

def main():
    """主函数"""
    # 检查文件完整性
    files_to_check = [
        "particle_heart.py",
        "advanced_heart.py", 
        "enhanced_heart.py",
        "interactive_love.html",
        "requirements.txt"
    ]
    
    missing_files = []
    for file in files_to_check:
        if not check_file_exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("⚠️  发现缺失的文件：")
        for file in missing_files:
            print(f"   - {file}")
        print()
    
    while True:
        clear_screen()
        show_main_menu()
        
        if missing_files:
            print(f"⚠️  缺失文件: {', '.join(missing_files)}")
        
        choice = input("\n请输入选择 (0-6): ").strip()
        
        if choice == '0':
            print("💕 感谢使用爱心系列启动器！")
            print("愿爱与美好永远伴随你！✨")
            break
        elif choice == '1':
            if check_file_exists("particle_heart.py"):
                run_python_script("particle_heart.py")
            else:
                print("❌ 文件 particle_heart.py 不存在")
                input("按回车键继续...")
        elif choice == '2':
            if check_file_exists("advanced_heart.py"):
                run_python_script("advanced_heart.py")
            else:
                print("❌ 文件 advanced_heart.py 不存在")
                input("按回车键继续...")
        elif choice == '3':
            if check_file_exists("enhanced_heart.py"):
                run_python_script("enhanced_heart.py")
            else:
                print("❌ 文件 enhanced_heart.py 不存在")
                input("按回车键继续...")
        elif choice == '4':
            if check_file_exists("interactive_love.html"):
                open_html_file("interactive_love.html")
            else:
                print("❌ 文件 interactive_love.html 不存在")
                input("按回车键继续...")
        elif choice == '5':
            show_project_info()
        elif choice == '6':
            install_dependencies()
        else:
            print("❌ 无效选择，请输入 0-6")
            input("按回车键继续...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 程序被用户中断，再见！")
    except Exception as e:
        print(f"❌ 程序运行出错: {e}")
    
    print("\n💕 愿爱与美好永远伴随你！✨")
    print("感谢使用爱心系列启动器！")
import os
import time
import json
import random
import requests
import urllib.parse
import os
import sys
from colorama import Fore, Style
import threading
from concurrent.futures import ThreadPoolExecutor
from pyfiglet import Figlet
from colorama import Fore
from datetime import datetime, timedelta
from requests.auth import HTTPProxyAuth
from colorama import Fore, Style
requests.urllib3.disable_warnings()

def art():
    print("\033[1;34m" + r"""     

MENUTOOL 
""" + "\033[0m" + "\033[1;96m" + r"""                                    
 
         By Tấn Tài tham gia telegram:@airdroptoolchannel
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mCân nhắc khi sử dụng,tool nguy cơ bị ban\033[0m\n\033[1;96mLoi tren 500: \nThi bo qua do sever\033[0m\n\033[1;34mMenu tool và code tool by tele: @tai_2302  \nThanks\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m[THAM GIA: @airdroptoolchannel]\033[0m\n\033[1;96m\033[0m")

def print_gradient_text(text, colors):
    banner = text.splitlines()
    total_lines = len(banner)
    section_size = total_lines // len(colors)
    for i, line in enumerate(banner):
        color = colors[i // section_size] if i // section_size < len(colors) else colors[-1]
        print(color + line + Style.RESET_ALL)

def create_gradient_banner(text):
    custom_fig = Figlet(font='slant')
    if os.name == "nt":
        custom_fig = Figlet(font='Stforek')
    
    os.system("title MeNuTool" if os.name == "nt" else "clear")
    os.system("cls" if os.name == "nt" else "clear")
    
    gradient_colors = [Fore.CYAN + Style.BRIGHT, Fore.RED + Style.BRIGHT, Fore.YELLOW + Style.BRIGHT]
    banner_text = custom_fig.renderText(text)
    
    print_gradient_text(banner_text, gradient_colors)

    print(f"{Fore.WHITE}[Tool tự động lấy token chỉ cần bỏ queryid $${Fore.RESET}")
    print(f"{Fore.YELLOW} Ban không chịu trách nhiệm,cân nhắc khi dùng !{Fore.RESET}")
        # Gọi hàm để hiển thị banner
create_gradient_banner('MENUTOOL BY @TAI_2302')

def update_script():
    repo_url = "https://raw.githubusercontent.com/lttai2302/capnhattool/main/menutool.py"  # Cập nhật đường dẫn URL chính xác của bạn
    local_file = "menutool.py"

    try:
        response = requests.get(repo_url)
        response.raise_for_status()

        # Đọc nội dung tệp hiện tại
        with open(local_file, "r", encoding="utf-8") as file:
            local_code = file.read()

        # So sánh nội dung tệp từ GitHub với tệp hiện tại
        if response.text != local_code:
            with open(local_file, "w", encoding="utf-8") as file:
                file.write(response.text)
            print("Đã cập nhật tệp, vui lòng chạy lại tool.")
            os._exit(0)  # Thoát để tránh chạy mã cũ
        else:
            print("Bạn đang sử dụng phiên bản mới nhất.")
    except Exception as e:
        print("Đã xảy ra lỗi khi cập nhật tệp:", str(e))

def delete_self_if_renamed():
    # Lấy tên tệp hiện tại đang chạy
    current_filename = os.path.basename(__file__)

    # Kiểm tra nếu tên tệp hiện tại không phải là "Vertus-Proxy2.py" hoặc "vertus-proxy2.py"
    if current_filename not in ["menutool.py", "MENUTOOL.PY", "Menutool.py"]:
        print(Fore.MAGENTA + Style.BRIGHT + "Tên tệp đã bị đổi, tệp sẽ tự xóa.")
        try:
            os.remove(__file__)
            print(Fore.MAGENTA + Style.BRIGHT + "Đã xóa tệp thành công.")
        except Exception as e:
            print("Không thể xóa tệp:", str(e))
        sys.exit()
    else:
        print(Fore.WHITE + Style.BRIGHT + "Tệp đang chạy đúng tên, không cần xóa.")

def run_script_from_github(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            script_content = response.text
            print(f"{Fore.LIGHTCYAN_EX}Chạy tool từ sever")
            exec(script_content)
        else:
            print(f"{Fore.RED}Lỗi: Không thể tải script từ tool")
    except Exception as e:
        print(f"{Fore.RED}Lỗi: {e}")

def main_tonghop():
    while True:
        print("\033[1m\033[38;2;255;165;0m" + Style.BRIGHT + "\nVui lòng chọn một trong các lựa chọn sau:")
        print(Fore.GREEN + Style.BRIGHT + "1. Tool storychainal")
        print(Fore.BLUE + Style.BRIGHT + "2. Tool vertus")
        print(Fore.WHITE + Style.BRIGHT + "3. Tool memewar")
        print(Fore.CYAN + Style.BRIGHT + "4. Tool moonhub")
        print(Fore.YELLOW + Style.BRIGHT + "5. Thoát chương trình")
        
        choice = input(Fore.YELLOW + Style.BRIGHT + "\nNhập số lựa chọn tool: ")

        if choice == '1':
            url = input(Fore.LIGHTCYAN_EX + "https://raw.githubusercontent.com/lttai2302/capnhattool/main/story-proxy2.py")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Đang chạy Tool storychainal...")
            run_script_from_github(url)
        elif choice == '2':
            url = input(Fore.LIGHTCYAN_EX + "https://raw.githubusercontent.com/lttai2302/capnhattool/main/Vertus-Proxy2.py")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Đang chạy Tool vertus...")
            run_script_from_github(url)
      
        elif choice == '3':
            url = input(Fore.LIGHTCYAN_EX + "https://raw.githubusercontent.com/lttai2302/capnhattool/main/meme-war.py")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Đang chạy Tool memewar...")
            run_script_from_github(url)
        elif choice == '4':
            url = input(Fore.LIGHTCYAN_EX + "https://raw.githubusercontent.com/lttai2302/capnhattool/main/moonhub-tool.py")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Đang chạy Tool moonhub...")
            run_script_from_github(url)
        elif choice == '5':
            print(Fore.RED + Style.BRIGHT + "Thoát chương trình.")
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    print(Fore.WHITE + Style.BRIGHT + "Đang kiểm tra cập nhật và kiểm tra tệp có bị đổi tên hay thiết bị khác sử dụng.")
    time.sleep(4)
    delete_self_if_renamed()
    update_script()
    main_tonghop()

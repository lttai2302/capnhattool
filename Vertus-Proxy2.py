import time
import requests
import random
import urllib.parse
import os
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor




def update_script():
    repo_url = "https://raw.githubusercontent.com/lttai2302/capnhattool/main/Vertus-Proxy2.py"  # Cập nhật đường dẫn URL chính xác của bạn
    local_file = "Vertus-Proxy2.py"

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
 
if __name__ == "__main__":
    print(Fore.WHITE + Style.BRIGHT + "Đi ngủ rồi mai chạy tool sao,mai nào tỉnh tag @tai_2302 bật tool")
    update_script()
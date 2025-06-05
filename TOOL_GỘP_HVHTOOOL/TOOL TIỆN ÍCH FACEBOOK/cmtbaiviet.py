import requests
import json
import time
import sys
import os

# Màu sắc cho giao diện
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
purple = "\033[35m"
hong = "\033[1;95m"
xam = "\033[1;37;90m"
cam = "\033[1;38;2;255;165;0m"
xanhngoc = "\033[1;38;2;0;255;255m"
nau = "\033[1;38;2;139;69;19m"
vangnhat = "\033[1;38;2;255;255;224m"
hongdam = "\033[1;38;2;199;21;133m"
xanhlacay = "\033[1;38;2;34;139;34m"
xanhbienda = "\033[1;38;2;70;130;180m"

def clear():
    if(sys.platform.startswith('win')):
        os.system('cls')
    else:
        os.system('clear')

def banner():
    print(f''' 
{tim}                                     ¶¶           
{hong}                                ¶1¶1111111¶       
{vang}        ¶¶111¶               ¶¶¶¶111111111¶¶¶1    
{xam}     ¶1¶¶¶¶¶111111¶         ¶¶¶1¶¶¶11111111¶1¶¶   
{xanhbienda}   ¶¶¶1¶1111111111¶¶1      ¶¶1¶¶¶1111111111111¶¶  
{cam}  ¶¶1¶¶1111111111111¶¶     ¶¶¶1¶¶¶¶1111111111111¶ 
{lam}  ¶¶ ¶1111111111111111¶¶   ¶¶¶¶¶¶11¶111111111111¶ 
{lamd} 11 ¶11111111111111111¶¶     ¶¶¶¶  ¶111111111111¶¶
{vangnhat}¶¶¶¶1111111111111111¶¶¶¶     1¶¶  11111111111111¶¶
{xanhlacay}¶¶¶¶11111111111¶¶¶¶¶¶¶      1¶1¶¶1111111111111111¶
{hongdam}¶¶1¶1111111111111¶¶¶¶¶¶     ¶¶¶¶¶¶11111111111111¶¶
{cam}¶¶11111111111111111111111¶¶   ¶¶¶¶¶¶1111111111¶¶¶ 
{tim} 1¶111111111111111111¶¶¶¶¶¶    ¶¶¶¶11111111111¶1  
{red}  ¶¶11111111111111111¶¶¶     ¶¶¶1111111111111¶1   
{trang}   ¶¶¶111111111111¶1¶¶¶    1¶¶111¶1111111¶11¶1    
{nau}    1¶¶¶11111111111¶¶¶¶111¶¶¶¶111111111¶11¶¶¶     
{purple}      ¶¶¶¶1111111111111¶¶¶¶1¶¶¶¶¶¶¶¶11¶11¶¶       
{luc}       ¶¶¶¶¶11111111111¶111¶   ¶¶¶111¶1¶¶¶        
{vang}         ¶¶¶¶¶¶111111111111¶  ¶¶¶111¶¶¶1          
{xam}            1¶¶¶¶¶11111111¶¶ ¶¶¶¶111¶¶            
{xanhbienda}              ¶¶¶¶¶¶1111111 ¶¶¶11¶¶1             
{tim}                 1¶¶¶¶¶¶1111¶¶¶1¶¶¶¶              
{xanhbienda}                    ¶¶¶¶¶¶1¶¶¶¶¶1¶                
{xanhlacay}                       ¶1¶¶¶1¶¶¶                  
{xanhngoc}                           11¶       
                        
{tim}                ██╗░░██╗██╗░░░██╗██╗░░██╗
{xanhbienda}                ██║░░██║██║░░░██║██║░░██║
{tim}                ███████║╚██╗░██╔╝███████║
{cam}                ██╔══██║░╚████╔╝░██╔══██║
{xanhlacay}                ██║░░██║░░╚██╔╝░░██║░░██║   LIKE VIP!!!!!!!!!!!!!!!!
{xanhngoc}                ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝    LIKE VIP!!!!!!!!!!!!!!!!
    ''')
print('')
clear()
banner()

def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        colors = [
            "\033[1;37mH\033[1;36mO\033[1;35mA\033[1;32mnN\033[1;31mG \033[1;34mH\033[1;33mU\033[1;36mY\033[1;36m🍉 - Tool\033[1;36m Yip \033[1;31m\033[1;32m",
            "\033[1;34mH\033[1;31mO\033[1;37mA\033[1;36mnN\033[1;32mG \033[1;35mH\033[1;37mU\033[1;33mY\033[1;32m🍉 - Tool\033[1;34m Yip \033[1;31m\033[1;32m",
            "\033[1;31mH\033[1;37mO\033[1;36mA\033[1;33mnN\033[1;35mG \033[1;32mH\033[1;34mU\033[1;35mY\033[1;37m🍉 - Tool\033[1;33m Yip \033[1;31m\033[1;32m",
            "\033[1;32mH\033[1;33mO\033[1;34mA\033[1;35mnN\033[1;36mG \033[1;37mH\033[1;36mU\033[1;31mY\033[1;34m🍉 - Tool\033[1;31m Yip \033[1;31m\033[1;32m",
            "\033[1;37mH\033[1;34mO\033[1;35mA\033[1;36mnN\033[1;32mG \033[1;33mH\033[1;31mU\033[1;37mY\033[1;34m🍉 - Tool\033[1;37m Yip \033[1;31m\033[1;32m",
            "\033[1;34mH\033[1;33mO\033[1;37mA\033[1;35mnN\033[1;31mG \033[1;36mH\033[1;36mU\033[1;32mY\033[1;37m🍉 - Tool\033[1;36m Yip \033[1;31m\033[1;32m",
            "\033[1;36mH\033[1;35mO\033[1;31mA\033[1;34mnN\033[1;37mG \033[1;35mH\033[1;32mU\033[1;36mY\033[1;33m🍉 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
        ]
        for color in colors:
            print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
            time.sleep(0.12)
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ", end="\r")

# Cấu hình
USER_ACCESS_TOKEN = input('NHẬP ACCESS_TOKEN : ') 
cookie = input('NHẬP COOKIE : ') 
POST_ID = input('NHẬP ID BÀI VIẾT (đảm bảo là ID bài viết, không phải ID ảnh): ')  
time_sec = int(input('Nhập Delay: '))
comment_text = input('NHẬP NỘI DUNG BÌNH LUẬN: ')
API_VERSION = "v12.0"
HEADERS = {
    'cookie': cookie,
}

def validate_user_token():
    try:
        url = f"https://graph.facebook.com/{API_VERSION}/me"
        params = {"access_token": USER_ACCESS_TOKEN}
        response = requests.get(url, params=params, headers=HEADERS)
        response.raise_for_status()
        print("User access token is valid. User ID:", response.json().get("id"))
        return True
    except requests.exceptions.HTTPError as http_err:
        print(f"Invalid user token: {http_err}")
        print(f"Response: {response.text}")
        return False

def validate_page_token(page_token, page_name):
    try:
        url = f"https://graph.facebook.com/{API_VERSION}/me"
        params = {"access_token": page_token}
        response = requests.get(url, params=params, headers=HEADERS)
        response.raise_for_status()
        print(f"Page access '{page_name}' Hợp Lệ. Page ID:", response.json().get("id"))
        return True
    except requests.exceptions.HTTPError as http_err:
        print(f"Invalid Page token for '{page_name}': {http_err}")
        print(f"Response: {response.text}")
        return False

def validate_post_id(page_token, page_name):
    try:
        url = f"https://graph.facebook.com/{API_VERSION}/{POST_ID}"
        params = {"access_token": page_token}
        response = requests.get(url, params=params, headers=HEADERS)
        response.raise_for_status()
        print(f"Post {POST_ID} bài viết hợp lệ . đang truy cập --->>>'{page_name}'.")
        return True, None, None
    except requests.exceptions.HTTPError as http_err:
        error_response = response.json()
        error_code = error_response.get("error", {}).get("code")
        error_message = error_response.get("error", {}).get("message")
        print(f"Post {POST_ID} is invalid or inaccessible to '{page_name}': {http_err}")
        print(f"Response: {response.text}")
        return False, error_code, error_message

def comment_on_facebook_post(page_token, page_name, comment_text):
    if not validate_page_token(page_token, page_name):
        print(f"Skipping comment for '{page_name}': Invalid Page token.")
        return False

    is_valid, error_code, error_message = validate_post_id(page_token, page_name)
    if not is_valid and error_code != 12:
        print(f"Skipping comment for '{page_name}': Post ID is invalid or inaccessible.")
        return False

    try:
        url = f"https://graph.facebook.com/{API_VERSION}/{POST_ID}/comments"
        params = {
            "access_token": page_token,
            "message": comment_text
        }
        response = requests.post(url, params=params, headers=HEADERS)
        response.raise_for_status()
        response_json = response.json()

        if "id" in response_json:
            print(f"BÌNH LUẬN THÀNH CÔNG {POST_ID} with '{page_name}'.")
            return True
        else:
            print(f"BÌNH LUẬN THẤT BẠI {POST_ID} with '{page_name}'. Response: {response_json}")
            return False

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error while commenting with '{page_name}': {http_err}")
        print(f"Response: {response.text}")
        return False
    except Exception as err:
        print(f"Error while commenting with '{page_name}': {err}")
        return False

def get_all_page_tokens_and_ids():
    if not validate_user_token():
        print("Aborting: Fix the user access token and try again.")
        return []

    pages_data = []
    try:
        url = f"https://graph.facebook.com/{API_VERSION}/me/accounts"
        params = {
            "access_token": USER_ACCESS_TOKEN,
            "fields": "id,name,access_token",
            "limit": 100
        }

        while url:
            response = requests.get(url, params=params, headers=HEADERS)
            response.raise_for_status()
            data = response.json()

            pages = data.get("data", [])
            if not pages and not pages_data:
                print("No Pages found for this user.")
                return []

            for page in pages:
                pages_data.append({
                    "page_name": page["name"],
                    "page_id": page["id"],
                    "access_token": page["access_token"]
                })

            url = data.get("paging", {}).get("next")
            params = {}

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response: {response.text}")
        return []
    except Exception as err:
        print(f"An error occurred: {err}")
        return []

    return pages_data

def save_to_file(pages_data, filename="page_tokens.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(pages_data, f, indent=4, ensure_ascii=False)
        print(f"Saved Page data to {filename}")
    except Exception as err:
        print(f"Error saving to file: {err}")

def print_page_names(pages_data):
    print("\nDANH SÁCH ATIF KHOẢN:")
    for index, page in enumerate(pages_data):
        print(f"page[{index}][{page['page_name']}]")

if __name__ == "__main__":
    pages = get_all_page_tokens_and_ids()

    if pages:
        print_page_names(pages)
        save_to_file(pages)
        print(f"\nBẮT ĐẦU BÌNH LUẬN:{POST_ID}........ ")
        time.sleep(5)
        successful_comments = 0
        for page in pages:
            print(f'{luc}---------------------------------------------------------------')
            print(f"{hongdam}TÀI KHOẢN PAGE' --->>{page['page_name']}' (ID: {page['page_id']})")
            if comment_on_facebook_post(page["access_token"], page["page_name"], comment_text):
                successful_comments += 1
            countdown(time_sec)
        print(f" BÌNH LUẬN THÀNH CÔNG {POST_ID} VỚI {successful_comments}/{len(pages)} Pages.")
        print(f'{luc}---------------------------------------------------------------')
    else:
        print("Không có trang nào có sẵn để bình luận bài viết.")
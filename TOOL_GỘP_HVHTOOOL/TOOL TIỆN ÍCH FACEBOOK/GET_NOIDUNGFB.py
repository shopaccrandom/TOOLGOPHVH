import requests
import json
import time
import sys
import os
import re

# Màu sắc giao diện
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

# Xóa màn hình
def clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

# In banner
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
{xanhlacay}                ██║░░██║░░╚██╔╝░░██║░░██║   GET POST VIP!!!!!!!!!!!!!!!!
{xanhngoc}                ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝   GET POST VIP!!!!!!!!!!!!!!!!
    ''')

# Đếm ngược với hiệu ứng màu
def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        colors = [
            "\033[1;37mH\033[1;36mO\033[1;35mA\033[1;32mnN\033[1;31mG \033[1;34mH\033[1;33mU\033[1;36mY\033[1;36m🍉 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
            "\033[1;34mH\033[1;31mO\033[1;37mA\033[1;36mnN\033[1;32mG \033[1;35mH\033[1;37mU\033[1;33mY\033[1;32m🍉 - Tool\033[1;34m Vip \033[1;31m\033[1;32m",
            "\033[1;31mH\033[1;37mO\033[1;36mA\033[1;33mnN\033[1;35mG \033[1;32mH\033[1;34mU\033[1;35mY\033[1;37m🍉 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
            "\033[1;32mH\033[1;33mO\033[1;34mA\033[1;35mnN\033[1;36mG \033[1;37mH\033[1;36mU\033[1;31mY\033[1;34m🍉 - Tool\033[1;31m Vip \033[1;31m\033[1;32m",
            "\033[1;37mH\033[1;34mO\033[1;35mA\033[1;36mnN\033[1;32mG \033[1;33mH\033[1;31mU\033[1;37mY\033[1;34m🍉 - Tool\033[1;37m Vip \033[1;31m\033[1;32m",
            "\033[1;34mH\033[1;33mO\033[1;37mA\033[1;35mnN\033[1;31mG \033[1;36mH\033[1;36mU\033[1;32mY\033[1;37m🍉 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
            "\033[1;36mH\033[1;35mO\033[1;31mA\033[1;34mnN\033[1;37mG \033[1;35mH\033[1;32mU\033[1;36mY\033[1;33m🍉 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
        ]
        for color in colors:
            print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
            time.sleep(0.12)
    print("\r                          \r", end="")
    print("\033[1;35mĐANG XỬ LÝ DỮ LIỆU         ", end="\r")

# Cấu hình
API_VERSION = "v20.0"

# Nhập thông tin
clear()
banner()
USER_ACCESS_TOKEN = input(f'{vang}NHẬP ACCESS_TOKEN: ')
COOKIE = input(f'{hong}NHẬP COOKIE: ')
POST_ID = input(f'{luc}NHẬP ID BÀI VIẾT: ')
#DELAY = int(input(f'{xanhbienda}NHẬP DELAY (GIÂY): '))

# Tiêu đề yêu cầu
HEADERS = {
    'cookie': COOKIE,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Kiểm tra token hợp lệ
def validate_user_token():
    try:
        url = f"https://graph.facebook.com/{API_VERSION}/me?fields=id,name,permissions"
        params = {"access_token": USER_ACCESS_TOKEN}
        response = requests.get(url, params=params, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        print(f"{luc}TOKEN HỢP LỆ. USER ID: {data.get('id')} ({data.get('name')})")
        permissions = data.get('permissions', {}).get('data', [])
        #print(f"{vang}QUYỀN: {', '.join([perm['permission'] for perm in permissions if perm['status'] == 'granted'])}")
        return True
    except requests.exceptions.HTTPError as http_err:
        print(f"{red}TOKEN KHÔNG HỢP LỆ: {http_err}")
        print(f"{red}PHẢN HỒI: {response.text}")
        return False

# Kiểm tra ID bài viết
def validate_post_id():
    try:
        url = f"https://graph.facebook.com/{API_VERSION}/{POST_ID}?fields=id"
        params = {"access_token": USER_ACCESS_TOKEN}
        response = requests.get(url, params=params, headers=HEADERS)
        response.raise_for_status()
        print(f"{luc}ID BÀI VIẾT {POST_ID} HỢP LỆ.")
        return True
    except requests.exceptions.HTTPError as http_err:
        print(f"{red}ID BÀI VIẾT {POST_ID} KHÔNG HỢP LỆ HOẶC KHÔNG TRUY CẬP ĐƯỢC: {http_err}")
        print(f"{red}PHẢN HỒI: {response.text}")
        return False

# Lấy nội dung bài viết
def get_facebook_post():
    if not validate_user_token():
        print(f"{red}VUI LÒNG KIỂM TRA TOKEN VÀ THỬ LẠI.")
        return None

    if not validate_post_id():
        print(f"{red}VUI LÒNG KIỂM TRA ID BÀI VIẾT VÀ THỬ LẠI.")
        return None

    try:
        # Yêu cầu cơ bản: message, created_time, from, permalink_url
        url = f"https://graph.facebook.com/{API_VERSION}/{POST_ID}?fields=message,created_time,from,permalink_url"
        params = {"access_token": USER_ACCESS_TOKEN}
        response = requests.get(url, params=params, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            print(f"{red}LỖI: {data['error']['message']}")
            return None

        # Lấy số lượt thích qua /reactions
        likes_count = 0
        try:
            url_likes = f"https://graph.facebook.com/{API_VERSION}/{POST_ID}/reactions?summary=total_count"
            response_likes = requests.get(url_likes, params=params, headers=HEADERS)
            response_likes.raise_for_status()
            likes_count = response_likes.json().get("summary", {}).get("total_count", 0)
        except:
            print(f"{vang}KHÔNG LẤY ĐƯỢC SỐ LƯỢT THÍCH.")

        # Lấy số bình luận qua /comments
        comments_count = 0
        try:
            url_comments = f"https://graph.facebook.com/{API_VERSION}/{POST_ID}/comments?summary=total_count"
            response_comments = requests.get(url_comments, params=params, headers=HEADERS)
            response_comments.raise_for_status()
            comments_count = response_comments.json().get("summary", {}).get("total_count", 0)
        except:
            print(f"{vang}KHÔNG LẤY ĐƯỢC SỐ BÌNH LUẬN.")

        # Lấy số chia sẻ (nếu có)
        shares_count = data.get("shares", {}).get("count", 0)

        post_data = {
            "post_id": POST_ID,
            "message": data.get("message", "Không có nội dung"),
            "created_time": data.get("created_time", "Không xác định"),
            "from": data.get("from", {}).get("name", "Không xác định"),
            "permalink_url": data.get("permalink_url", "Không có link"),
            "likes": likes_count,
            "comments": comments_count,
            "shares": shares_count
        }
        print(f"{luc}---------------------------------------------------------------")
        print(f"{hongdam}LẤY NỘI DUNG BÀI VIẾT {POST_ID} THÀNH CÔNG!")
        print(f"{vang}NGƯỜI ĐĂNG: {post_data['from']}")
        print(f"{vang}NỘI DUNG: {post_data['message']}")
        print(f"{vang}THỜI GIAN: {post_data['created_time']}")
        print(f"{vang}LINK: {post_data['permalink_url']}")
        print(f"{vang}LƯỢT THÍCH: {post_data['likes']}")
        print(f"{vang}BÌNH LUẬN: {post_data['comments']}")
        print(f"{vang}CHIA SẺ: {post_data['shares']}")
        print(f"{luc}---------------------------------------------------------------")
        return post_data

    except requests.exceptions.HTTPError as http_err:
        print(f"{red}LỖI HTTP: {http_err}")
        print(f"{red}PHẢN HỒI: {response.text}")
        return None
    except Exception as err:
        print(f"{red}LỖI: {err}")
        return None

# Lưu dữ liệu vào file JSON
def save_to_file(post_data, filename="post_data.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(post_data, f, indent=4, ensure_ascii=False)
        print(f"{luc}LƯU DỮ LIỆU VÀO {filename} THÀNH CÔNG!")
    except Exception as err:
        print(f"{red}LỖI LƯU FILE: {err}")

# Hàm chính
if __name__ == "__main__":
    print(f"\n{xanhbienda}BẮT ĐẦU LẤY NỘI DUNG BÀI VIẾT: {POST_ID}...")
    time.sleep(3)
    post_data = get_facebook_post()
    if post_data:
        save_to_file(post_data)
    else:
        print(f"{red}KHÔNG LẤY ĐƯỢC NỘI DUNG BÀI VIẾT.")
    print(f"{luc}HOÀN TẤT!")
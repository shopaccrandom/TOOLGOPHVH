import requests
import json
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

# Cấu hình
USER_ACCESS_TOKEN = input('NHẬP ACCESS_TOKEN : ') 
cookie = input('NHẬP COOKIE : ') 
POST_ID = input('NHẬP ID BÀI VIẾT: ')  
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

def validate_post_id(user_token, post_id):
    try:
        url = f"https://graph.facebook.com/{API_VERSION}/{post_id}"
        params = {"access_token": user_token}
        response = requests.get(url, params=params, headers=HEADERS)
        response.raise_for_status()
        print(f"Post {post_id} is accessible.")
        return True, None, None
    except requests.exceptions.HTTPError as http_err:
        response = http_err.response
        error_response = response.json()
        error_code = error_response.get("error", {}).get("code")
        error_message = error_response.get("error", {}).get("message")
        print(f"Post {post_id} is invalid or inaccessible: {http_err}")
        print(f"Response: {response.text}")
        return False, error_code, error_message

def comment_on_post(user_token, post_id, comment_text):
    try:
        url = f"https://graph.facebook.com/{API_VERSION}/{post_id}/comments"
        params = {
            "access_token": user_token,
            "message": comment_text
        }
        response = requests.post(url, params=params, headers=HEADERS)
        response.raise_for_status()
        response_json = response.json()
        if "id" in response_json:
            print(f"Commented successfully on post {post_id}.")
            return True
        else:
            print(f"Failed to comment on post {post_id}. Response: {response_json}")
            return False
    except requests.exceptions.HTTPError as http_err:
        response = http_err.response
        print(f"HTTP error while commenting: {http_err}")
        print(f"Response: {response.text}")
        return False
    except Exception as err:
        print(f"Error while commenting: {err}")
        return False

if __name__ == "__main__":
    if validate_user_token():
        is_valid, error_code, error_message = validate_post_id(USER_ACCESS_TOKEN, POST_ID)
        if is_valid or error_code == 12:
            if comment_on_post(USER_ACCESS_TOKEN, POST_ID, comment_text):
                print("Comment posted successfully.")
            else:
                print("Failed to post comment.")
        else:
            print(f"Cannot comment on post {POST_ID} due to error: {error_message}")
    else:
        print("Invalid user access token. Please check and try again.")
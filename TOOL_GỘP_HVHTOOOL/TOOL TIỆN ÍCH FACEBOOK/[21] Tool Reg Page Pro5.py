#TOOL BY HVHTOOÔOL
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
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

ndp_tool = trang + "" + do + "[" + trang + "<+>" + do + "] " + trang + "=> "
ndp = trang + "" + do + "[" + trang + "<+>" + do + "] " + trang + "=> "
# Config

dem = 0
# import lib
import requests, os, sys,re
from time import sleep
from datetime import datetime
try:
    import requests
except:
    print(luc+"Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải... ")
    os.system("pip install requests")
# ====================== [ FUNCTION ] ====================== 
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def banner():
    banner = f"""
                        
{tim}                ██╗░░██╗██╗░░░██╗██╗░░██╗
{xanhbienda}                ██║░░██║██║░░░██║██║░░██║
{tim}                ███████║╚██╗░██╔╝███████║
{cam}                ██╔══██║░╚████╔╝░██╔══██║
{xanhlacay}                ██║░░██║░░╚██╔╝░░██║░░██║   REGPRO5 VIP!!!!!!!!!!!!!!!!!!!!!!
{xanhngoc}                ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝    REGPRO5 VIP!!!!!!!!!!!!!!!!!!!!!!         
                        
\033[1;37m-----------------------------------------------------------------"""
    echo(banner)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
def ndp_delay(o):
    while(o>1):
        o=o-1
        print(f'{trang}[\033[1;31mH\033[1;33mV \033[1;36mH\033[1;37m[\033[1;36m|\033[1;37m]\033[1;37m[.....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mH\033[1;32mV \033[1;34mH\033[1;37m[\033[1;31m/\033[1;37m]\033[1;37m[\033[1;32m>\033[1;37m....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33mV \033[1;36mH\033[1;37m[\033[1;32m-\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;37m...]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mH\033[1;32mV \033[1;34mH\033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;37m..]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33mV \033[1;36mH\033[1;37m[\033[1;34m\{trang}]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;37m.]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mH\033[1;32mV \033[1;34mH\033[1;37m[\033[1;35m|\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;35m>\033[1;37m]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
# =================[ START TOOL ]===========================
clear()
banner()
access_token = input('Nhập Token:')
cookie = input(ndp_tool+luc+'Vui Lòng Nhập Cookie Facebook'+trang+': '+vang)
headers = {
        'authority': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://mbasic.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://mbasic.facebook.com/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie
}
    
try:
    url = 'https://www.facebook.com/'
    response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
    response.raise_for_status()  # Ném lỗi nếu mã trạng thái không phải 200
    home = response.text
    # Phần còn lại của mã (trích xuất fb_dtsg, jazoest, tên, v.v.)
    # Extract fb_dtsg
    fb_dtsg_match = None
    fb_dtsg_patterns = [
        r'<input type="hidden" name="fb_dtsg" value="(.*?)"',
        r'"name":"fb_dtsg","value":"(.*?)"',
        r'"fb_dtsg":"(.*?)"',
        r'fb_dtsg:"(.*?)"',
        r'"async_get_token":"(.*?)"'
    ]
    for pattern in fb_dtsg_patterns:
        fb_dtsg_match = re.search(pattern, home)
        if fb_dtsg_match:
            print(f"fb_dtsg found with pattern: {pattern}")
            break
    fb_dtsg = fb_dtsg_match.group(1) if fb_dtsg_match else None
    if not fb_dtsg:
        raise ValueError("Could not find fb_dtsg in the response")
    # Extract jazoest
    jazoest_match = re.search(r'<input type="hidden" name="jazoest" value="(.*?)"', home)
    if not jazoest_match:
        jazoest_match = re.search(r'"name":"jazoest","value":"(.*?)"', home)
    jazoest = jazoest_match.group(1) if jazoest_match else None
    if not jazoest:
        raise ValueError("Could not find jazoest in the response")
    # Extract name (ten)
    uid = cookie.split('c_user=')[1].split(';')[0]
except:
    print(ndp+do+"Cookie Die Vui Lòng Kiểm Tra Lại!!!")
# =================[ NHẬP DELAY ]===========================
clear()
banner()
delay = int(input(ndp_tool+luc+'Vui Lòng Nhập Delay Reg Page'+trang+': '+vang))
# GET INFO
result = {}
try:
    api_url = "https://graph.facebook.com/me"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Cookie": cookie  # Thêm cookie vào header của API
    }
    params = {
        "fields": "id,name",
        "access_token": access_token
    }
    api_response = requests.get(api_url, params=params, headers=headers)
    api_response.raise_for_status()
    api_data = api_response.json()

    if "error" in api_data:
        result["api_error"] = api_data["error"]["message"]
    else:
        id = api_data.get("id", "Không tìm thấy ID")
        name_fb = api_data.get("name", "Không tìm thấy tên")
        print(f"id: {id}")
        print(f"name: {name_fb}")
except requests.RequestException as e:
    result["api_error"] = f"Lỗi khi gửi yêu cầu API: {str(e)}"
except Exception as e:
    result["api_error"] = f"Lỗi API: {str(e)}"

# In lỗi nếu API thất bại



while True: 
    name = requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/male?count=2').json()['data'][0]['name']
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/pages/creation/?ref_type=launch_point',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1221',
        'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
        'x-fb-lsd': 'wPd4PRo0e2MNyiZJhrq96a',
        'cookie': cookie,
    }

    data = {
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': 'wPd4PRo0e2MNyiZJhrq96a',
        '__spin_r': '1006614608',
        '__spin_b': 'trunk',
        '__spin_t': '1668582022',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
        'variables': '{"input":{"bio":"test tool auto reg page pro5 by NguyenDucPhat","categories":["660696964377118"],"creation_source":"comet","name":"'+str(name)+'","page_referrer":"launch_point","actor_id":"'+str(uid)+'","client_mutation_id":"1"}}',
        'server_timestamps': 'true',
        'doc_id': '5903223909690825',
    }

    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    if 'id' in response.text:
        dem=dem+1
        id = response.json()['data']['additional_profile_plus_create']['additional_profile']['id']
        print(f''+do+'['+trang+'Bé Tập Code'+do+'] | '+do+'['+vang+str(dem)+do+'] | '+do+'['+trang+str(name)+do+'] | '+do+'['+trang+id+do+']')
        ndp_delay(delay)
    else:
        exit(ndp_tool+do+'Clone Đã Bị Block Reg Page!!!')
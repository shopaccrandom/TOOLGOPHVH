import requests, json, os, sys
from threading import Thread
import threading, re
import urllib.parse
from datetime import datetime
from time import strftime
from time import sleep
den = '\x1b[1;90m'
luc = '\x1b[1;32m'
trang = '\x1b[1;37m'
red = '\x1b[1;31m'
vang = '\x1b[1;33m'
tim = '\x1b[1;35m'
lamd = '\x1b[1;34m'
lam = '\x1b[1;36m'
purple = '\\e[35m'
hong = '\x1b[1;95m'
thanh_xau="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  \033[1;32m"
thanh_dep="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  \033[1;32m"
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
dem = 0

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
{xanhbienda}              ¶¶¶¶¶¶¶1111111 ¶¶¶11¶¶1             
{tim}                 1¶¶¶¶¶¶1111¶¶¶1¶¶¶¶              
{xanhbienda}                    ¶¶¶¶¶¶1¶¶¶¶¶1¶                
{xanhlacay}                       ¶1¶¶¶1¶¶¶                  
{xanhngoc}                           11¶       
                        
{tim}                ██╗░░██╗██╗░░░██╗██╗░░██╗
{xanhbienda}                ██║░░██║██║░░░██║██║░░██║
{tim}                ███████║╚██╗░██╔╝███████║
{cam}                ██╔══██║░╚████╔╝░██╔══██║
{xanhlacay}                ██║░░██║░░╚██╔╝░░██║░░██║   FOLLOW VIP!!!!!!!!!!!!!!!!
{xanhngoc}                ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝    FOLLOW VIP!!!!!!!!!!!!!!!!         
                            
     ''')
print('')

def nghingoi(delay):
    for x in range(delay, 0, -1):
        print("\r\033[1;93m   Bé Tập Code \033[1;91m ~>       \033[1;92m LO      \033[1;91m | "+str(x)+" | \r ", end='')
        sleep(0.14)
        print("\r\033[1;91m   Bé Tập Code \033[1;91m   ~>     \033[1;92m LOA     \033[0;31m | "+str(x)+" | \r ", end='')
        sleep(0.14)
        print("\r\033[1;92m   Bé Tập Code \033[1;91m     ~>   \033[1;92m LOAD    \033[0;31m | "+str(x)+" | \r", end='')
        sleep(0.14)
        print("\r\033[1;94m   Bé Tập Code \033[1;91m       ~> \033[1;92m LOADI   \033[0;31m | "+str(x)+" | \r", end='')
        sleep(0.14)
        print("\r\033[1;95m   Bé Tập Code \033[1;91m        ~>\033[1;92m LOADIN  \033[0;31m | "+str(x)+" | \r", end='')
        sleep(0.14)
        print("\r\033[1;96m   Bé Tập Code \033[1;91m        ~>\033[1;92m LOADING \033[0;31m | "+str(x)+" | \r", end='')
        sleep(0.14)
        print("\r\033[1;93m  Bé Tập Code \033[1;91m        ~>\033[1;92m LOADING.\033[0;31m | "+str(x)+" | \r", end='')
        sleep(0.14)
    print("\r\r\033[1;95m    ⚡Bé Tập Code⚡                         \r", end='')
    sleep(0.1)

def bongoc(so):
    a = "\033[1;31m" + "────" * so
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.003)
    print()

class Facebook:
    def __init__(self, cookie):
        self.cookie = cookie
        self.headers = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }

    def get_thongtin(self):
        try:
            url = 'https://www.facebook.com/'
            response = requests.get(url, headers=self.headers, timeout=10, allow_redirects=True)
            response.raise_for_status()
            home = response.text
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
            self.fb_dtsg = fb_dtsg_match.group(1) if fb_dtsg_match else None
            if not self.fb_dtsg:
                raise ValueError("Could not find fb_dtsg in the response")
            jazoest_match = re.search(r'<input type="hidden" name="jazoest" value="(.*?)"', home)
            if not jazoest_match:
                jazoest_match = re.search(r'"name":"jazoest","value":"(.*?)"', home)
            self.jazoest = jazoest_match.group(1) if jazoest_match else None
            if not self.jazoest:
                raise ValueError("Could not find jazoest in the response")
            name_match = re.search(r'"profile_owner":{"__typename":"User","name":"(.*?)"', home)
            ten = name_match.group(1) if name_match else None
            if not ten:
                name_match = re.search(r'<a aria-label="Dòng thời gian của (.*?)"', home)
                ten = name_match.group(1) if name_match else None
            if not ten:
                url_name_match = re.search(r'people/([^/]+)/', response.url)
                if url_name_match:
                    ten = urllib.parse.unquote(url_name_match.group(1)).replace('-', ' ')
            if not ten:
                raise ValueError("Could not find name in the response")
            self.user_id = self.cookie.split('c_user=')[1].split(';')[0]
            return ten, self.user_id
        except Exception as e:
            return 0

    def get_pro5(self):
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'cookie': self.cookie,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
        }
        data = {
            'av': self.user_id,
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometSettingsDropdownListQuery',
            'variables': '{"fetchTestUserProfileListCell":false,"includeHorizBadging":false,"inProfileSwitcherEntry":false,"inSimpleHeaderEntry":true,"scale":2}',
            'server_timestamps': 'true',
            'doc_id': '8179507702122101',
        }
        try:
            a = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
            get = a['data']['viewer']['actor']['profile_switcher_eligible_profiles']
            tong = get['count']
            data_pro5 = get['nodes']
            print(f'{red}| {vang}{tong} {luc}Page Profile')
            return data_pro5
        except:
            print(red + '\nKhông Get Được Page Profile ')
            return 0

    def follow(self, id, id_page, name):
        cookie = self.cookie
        ck_pro5 = cookie + '; i_user=' + id_page + ';'
        headers = {
            'Host': 'www.facebook.com',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '980',
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-lsd': 'ozBHo3fICOG_bXpKqo1J1C',
            'x-fb-friendly-name': 'CometUserFollowMutation',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua-platform': '"Linux"',
            'accept': '*/*',
            'origin': 'https://www.facebook.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.facebook.com/',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': ck_pro5
        }
        data = {
            'av': id_page,
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1669330367418,219724,250100865708545,","subscribe_location":"PROFILE","subscribee_id":"'+id+'","actor_id":"'+id_page+'","client_mutation_id":"1"},"scale":2}',
            'server_timestamps': 'true',
            'doc_id': '5032256523527306'
        }
        try:
            fl = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
            check = fl.json()['data']['actor_subscribe']['subscribee']['subscribe_status']
            if check == 'IS_SUBSCRIBED':
                print(f'{vang}[{trang}{dem}{vang}] {luc}[{lam}{name} {red}| {trang}{id_page}{luc}] {red}=> {vang}FOLLOW {red}=> {luc}[{trang}{id}{luc}] {red}=> {luc}SUCCESS ')
            else:
                print(f'{vang}[{trang}{dem}{vang}] {luc}[{lam}{name} {red}| {trang}{id_page}{luc}] {red}=> {vang}FOLLOW {red}=> {luc}[{trang}{id}{luc}] {red}=> {red}ERROR ')
        except:
            print(f'{vang}[{trang}{dem}{vang}] {luc}[{lam}{name} {red}| {trang}{id_page}{luc}] {red}=> {vang}FOLLOW {red}=> {luc}[{trang}{id}{luc}] {red}=> {red}ERROR ')

banner()
while True:
    while True:
        cookie = input(thanh_xau + luc + 'Nhập Cookie Nick Cầm Page Profile: ' + vang)
        fb = Facebook(cookie)
        bongoc(14)
        a = fb.get_thongtin()
        if a == 0:
            continue
        data_pro5 = fb.get_pro5()
        bongoc(14)
        if data_pro5 == 0:
            continue
        else:
            # Liệt kê tất cả page profile
            print(f"{luc}Danh sách Page Profile:")
            for i, page in enumerate(data_pro5, start=1):
                name = page['profile']['name']
                print(f"{vang}[{i}] | [{name}]")
            break
    id = input(thanh_xau + luc + 'Nhập ID Nick Cần Buff Follow: ' + vang)
    dl = int(input(thanh_xau + luc + 'Nhập Delay: ' + vang))
    for x in data_pro5:
        id_page = x['profile']['id']
        name = x['profile']['name']
        dem += 1
        fb.follow(id, id_page, name)
        nghingoi(dl)
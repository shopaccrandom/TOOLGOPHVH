import json
from curl_cffi import requests
import os
import sys
import re
from time import sleep
from datetime import datetime
import random

# Load User-Agent strings from user-agent.txt
def load_user_agents(file_path="user-agent.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            user_agents = [line.strip() for line in file if line.strip()]
        if not user_agents:
            raise ValueError("không có User-Agent")
        return user_agents
    except FileNotFoundError:
        print(f"Error: {file_path} không có file")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        sys.exit(1)

USER_AGENTS = load_user_agents()

def get_random_user_agent(used_user_agents):
    available_agents = [ua for ua in USER_AGENTS if ua not in used_user_agents]
    if not available_agents:
        used_user_agents.clear()  # Reset if all User-Agents are used
        available_agents = USER_AGENTS
    chosen_agent = random.choice(available_agents)
    used_user_agents.add(chosen_agent)
    return chosen_agent

def banner():
    print("\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗")
    print("\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║")
    print("\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║")
    print("\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║")
    print("\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗")
    print("\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n")
    print("\033[97m════════════════════════════════════════════════")

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
thanh_xau = "\033[1;97m[\033[1;91m✨\033[1;97m] \033[1;36m☄️  \033[1;32m"
thanh_dep = "\033[1;97m[\033[1;91m✨\033[1;97m] \033[1;36m☄️  \033[1;32m"

dem = 0
list_cookie = []
os.system("cls" if os.name == "nt" else "clear")
banner()

def coin(ckvp):
    try:
        h_xu = {'user-agent': get_random_user_agent(set()), 'cookie': ckvp}
        x = requests.post('https://vipig.net/home.php', headers=h_xu, timeout=10).text
        xu = x.split('"soduchinh">')[1].split('<')[0]
        return xu
    except Exception as e:
        print(f"Error fetching coin balance: {e}")
        return "0"

def cookie(token):
    try:
        ck = requests.post('https://vipig.net/logintoken.php', headers={'Content-type': 'application/x-www-form-urlencoded'}, data={'access_token': token}, timeout=10)
        cookie = 'PHPSESSID=' + ck.cookies['PHPSESSID']
        return cookie
    except Exception as e:
        print(f"Error fetching cookie: {e}")
        return None

def get_nv(type, ckvp):
    headers = {
        'content-type': 'text/html; charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'referer': 'https://vipig.net/kiemtien/',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?1',
        'user-agent': get_random_user_agent(set()),
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'cookie': ckvp
    }
    try:
        a = requests.post(f'https://vipig.net/kiemtien{type}/getpost.php', headers=headers, timeout=10).json()
        return a
    except Exception as e:
        print(f"Error fetching tasks: {e}")
        return []

def nhan_tien(list, ckvp, type):
    data_xu = 'id=' + str(list)
    data_nhan = str(len(data_xu))
    headers = {
        'content-length': data_nhan,
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': '*/*',
        'user-agent': get_random_user_agent(set()),
        'sec-ch-ua-mobile': '?1',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'origin': 'https://vipig.net',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://vipig.net/kiemtien' + type + '/',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cookie': ckvp
    }
    try:
        a = requests.post(f'https://vipig.net/kiemtien{type}/nhantien.php', headers=headers, data=data_xu, timeout=10).text
        return a
    except Exception as e:
        print(f"Error claiming reward: {e}")
        return ""

def nhan_sub(list, ckvp):
    data_xu = 'id=' + str(list[0:len(list)-1])
    data_nhan = str(len(data_xu))
    headers = {
        'content-length': data_nhan,
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': '*/*',
        'user-agent': get_random_user_agent(set()),
        'sec-ch-ua-mobile': '?1',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'origin': 'https://vipig.net',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://vipig.net/kiemtien/subcheo',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cookie': ckvp
    }
    try:
        a = requests.post('https://vipig.net/kiemtien/subcheo/nhantien2.php', headers=headers, data=data_xu, timeout=10).json()
        return a
    except Exception as e:
        print(f"Error claiming follow reward: {e}")
        return {}

def delay(dl):
    try:
        for i in range(dl, -1, -1):
            print(f'[Bé Tập Code][{i} Giây]           ', end='\r')
            sleep(1)
    except:
        sleep(dl)
        print(dl, end='\r')

def name(cookie, user_agent):
    try:
        headers = {
            'Host': 'www.instagram.com',
            'cache-control': 'max-age=0',
            'viewport-width': '980',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': cookie
        }
        a = requests.get('https://www.instagram.com/', headers=headers, timeout=10).text
        match = re.search(r'"username":"(.*?)"', a)
        if match:
            user = match.group(1)
            id_match = re.search(r'ds_user_id=(\d+);', cookie)
            if id_match:
                return user, id_match.group(1)
        return 'die', 'die'
    except Exception as e:
        print(f"Error fetching Instagram username: {e}")
        return 'die', 'die'

def bongoc(so):
    a = "────" * so
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.003)
    print()

def like(id, cookie, user_agent):
    headers = {
        "x-ig-app-id": "1217981644879628",
        "x-asbd-id": "198387",
        "x-instagram-ajax": "c161aac700f",
        "accept": "*/*",
        "content-length": "0",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": user_agent,
        "x-csrftoken": cookie.split('csrftoken=')[1].split(';')[0],
        "x-requested-with": "XMLHttpRequest",
        "cookie": cookie
    }
    try:
        like = requests.post(f'https://www.instagram.com/web/likes/{id}/like/', headers=headers, timeout=10).text
        return '2' if 'ok' in like else '1'
    except Exception as e:
        print(f"Error liking post: {e}")
        return '1'

def get_id(link, cookie, user_agent):
    headers = {
        "x-ig-app-id": "1217981644879628",
        "x-asbd-id": "198387",
        "x-instagram-ajax": "c161aac700f",
        "accept": "*/*",
        "content-length": "0",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": user_agent,
        "x-csrftoken": cookie.split('csrftoken=')[1].split(';')[0],
        "x-requested-with": "XMLHttpRequest",
        "cookie": cookie
    }
    try:
        response = requests.get(link, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Invalid response status: {response.status_code}")
            return False
        a = response.text
        match = re.search(r'("id":".*?")', a)
        if not match:
            print(f"Post ID not found in response")
            return False
        id_str = match.group(1)  # e.g., "id":"1234567890"
        id = id_str.split('"id":"')[1].rstrip('"')  # Extract 1234567890
        if not id.isdigit():  # Validate that ID is numeric
            print(f"Invalid post ID format: {id}")
            return False
        return id
    except Exception as e:
        print(f"Error fetching post ID: {e}")
        return False

def follow(id, cookie, user_agent):
    headers = {
        "x-ig-app-id": "1217981644879628",
        "x-asbd-id": "198387",
        "x-instagram-ajax": "c161aac700f",
        "accept": "*/*",
        "content-length": "0",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": user_agent,
        "x-csrftoken": cookie.split('csrftoken=')[1].split(';')[0],
        "x-requested-with": "XMLHttpRequest",
        "cookie": cookie
    }
    try:
        fl = requests.post(f"https://i.instagram.com/web/friendships/{id}/follow/", headers=headers, timeout=10).text
        return fl if 'ok' in fl else '1'
    except Exception as e:
        print(f"Error following user: {e}")
        return '1'

def cmt(msg, id, cookie, user_agent):
    headers = {
        "x-ig-app-id": "1217981644879628",
        "x-asbd-id": "198387",
        "x-instagram-ajax": "c161aac700f",
        "accept": "*/*",
        "content-length": "0",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": user_agent,
        "x-csrftoken": cookie.split('csrftoken=')[1].split(';')[0],
        "x-requested-with": "XMLHttpRequest",
        "cookie": cookie
    }
    try:
        cmt = requests.post(f'https://i.instagram.com/api/v1/web/comments/{id}/add/', headers=headers, data={'comment_text': msg}, timeout=10).json()
        return 'ok' if cmt.get('status') == 'ok' else cmt
    except Exception as e:
        print(f"Error commenting: {e}")
        return '1'

def cau_hinh(id_ig, ckvp, user_agent):
    headers = {
        'content-length': '23',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?1',
        'user-agent': user_agent,
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://vipig.net/cauhinh/datnick.php',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cookie': ckvp
    }
    try:
        a = requests.post('https://vipig.net/cauhinh/datnick.php', headers=headers, data={'iddat[]': id_ig}, timeout=10).text
        return a
    except Exception as e:
        print(f"Error configuring account: {e}")
        return '0'

while True:
    token = input(f'{thanh_dep}Nhập Access_Token Vipig: {vang}')
    log = requests.post('https://vipig.net/logintoken.php', headers={'Content-type': 'application/x-www-form-urlencoded'}, data={'access_token': token}, timeout=10).json()
    if log.get('status') == 'success':
        user = log['data']['user']
        xu = log['data']['sodu']
        ckvp = cookie(token)
        if ckvp:
            print(f'{thanh_dep}Đăng Nhập Thành Công')
            break
    else:
        print(f"{red}{log.get('mess', 'Đăng nhập thất bại')}")
bongoc(14)
x = 0
print('[LƯU Ý] Muốn Dừng Thì Nhấn Enter')
while True:
    x += 1
    cookie = input(f'{thanh_dep}Nhập Cookie Instagram Thứ {x}: {vang}')
    if cookie == '' and x > 1:
        break
    ten = name(cookie, get_random_user_agent(set()))
    if ten[0] != 'die':
        print(f'User Instagram: {ten[0]} ')
        list_cookie.append(cookie)
        bongoc(14)
    else:
        print(f'{red}Cookie Instagram Sai ! Vui Lòng Nhập Lại !!! ')
        x -= 1
        bongoc(14)

os.system("cls" if os.name == "nt" else "clear")
banner()
print(f"""{thanh_dep}Tên Tài Khoản: {vang}{user}
{thanh_dep}Xu Hiện Tại: {vang}{xu}
{thanh_dep}Số Cookie: {vang}{len(list_cookie)}""")
bongoc(14)
print(f"""{thanh_dep}Nhập [1] Để Chạy Nhiệm Vụ Like
{thanh_dep}Nhập [2] Để Chạy Nhiệm Vụ Follow
{thanh_dep}Nhập [3] Để Chạy Nhiệm Vụ Comment
{thanh_dep}Có Thể Chọn Nhiều Nhiệm Vụ {vang}(Ví Dụ 123)""")
chon = input(f'{thanh_dep}Nhập Số Để Chạy Nhiệm Vụ: {vang}')
bongoc(14)
dl = int(input(f'{thanh_dep}Nhập Delay: {vang}'))
print('Sau ____ Nhiệm Vụ Thì Kích Hoạt Chống Block.', end='\r')
chong_block = int(input('Sau '))
print(f'Sau {chong_block} Nhiệm Vụ Nghỉ Ngơi ____ Giây       ', end='\r')
delay_block = int(input(f'Sau {chong_block} Nhiệm Vụ Nghỉ Ngơi '))
doi_acc = int(input(f'{thanh_dep}Sau Bao Nhiêu Nhiệm Vụ Thì Đổi Nick: {vang}'))

while True:
    x = 0
    hvh = 0
    used_user_agents = set()  # Track used User-Agents
    if len(list_cookie) == 0:
        print(f'{red}Toàn Bộ Cookie Đã Out Vui Lòng Nhập Lại !!')
        while True:
            x += 1
            cookie = input(f'{thanh_dep}Nhập Cookie Instagram Thứ {x}: {vang}')
            if cookie == '' and x > 1:
                break
            ten = name(cookie, get_random_user_agent(used_user_agents))
            if ten[0] != 'die':
                print(f'User Instagram: {ten[0]} ')
                list_cookie.append(cookie)
                bongoc(14)
            else:
                print(f'{red}Cookie Instagram Sai ! Vui Lòng Nhập Lại !!! ')
                x -= 1
                bongoc(14)
    for i in range(len(list_cookie)):
        if hvh == 2:
            break
        loi_like = 0
        loi_cmt = 0
        loi_get_id = 0  # Counter for get_id failures
        cookie = list_cookie[i]
        current_user_agent = get_random_user_agent(used_user_agents)  # Select new User-Agent for this cookie
        #print(f"Using User-Agent: {current_user_agent}")  # Debug print to confirm User-Agent
        user = name(cookie, current_user_agent)
        id_ig = user[1]
        if user[0] == 'die':
            print(f'{red}Cookie Instagram Die !!!! ')
            list_cookie.remove(cookie)
            continue
        ngoc = cau_hinh(id_ig, ckvp, current_user_agent)
        if ngoc == '1':
            bongoc(14)
            print(f'Đang Cấu Hình ID: {id_ig} | User: {user[0]} | user_agent: {current_user_agent}')
            bongoc(14)
        else:
            print(f'Cấu Hình Thất Bại ID: {id_ig} | User: {user[0]} ')
            delay(3)
            list_cookie.remove(cookie)
            continue
        hvh = 0
        while True:
            if hvh in (1, 2):
                break
            if '1' in chon:
                get_like = get_nv('', ckvp)
                if len(get_like) == 0:
                    print('Tạm Thời Hết Nhiệm Vụ Like', '     ', end='\r')
                if len(get_like) != 0:
                    print(f'Tìm Thấy {len(get_like)} Nhiệm Vụ Like', '     ', end='\r')
                for x in get_like:
                    link = x['link']
                    uid = x['idpost']
                    id = get_id(link, cookie, current_user_agent)
                    if id is False:
                        loi_get_id += 1
                        if loi_get_id >= 5:  # Switch cookie after 5 consecutive get_id failures
                            print(f'{red}Tài Khoản {user[0]} Gặp Quá Nhiều Lỗi Lấy Post ID, Chuyển Cookie')
                            list_cookie.remove(cookie)
                            hvh = 2
                            break
                        continue
                    loi_get_id = 0  # Reset counter on success
                    lam = like(id, cookie, current_user_agent)
                    if lam == '1':
                        user = name(cookie, current_user_agent)
                        if user[0] == 'die':
                            print('Cookie Instagram Die !!!! ')
                            list_cookie.remove(cookie)
                            hvh = 2
                            break
                        else:
                            print(f'Tài Khoản {user[0]} Đã Bị Chặn Tương Tác {lam}')
                            list_cookie.remove(cookie)
                            hvh = 2
                            break
                    elif loi_like >= 4:
                        print(f'Tài Khoản {user[0]} Đã Bị Chặn Tương Tác')
                        list_cookie.remove(cookie)
                        hvh = 2
                        break
                    elif lam == '2':
                        nhan = nhan_tien(uid, ckvp, '')
                        if 'mess' in nhan:
                            xu = coin(ckvp)
                            dem += 1
                            tg = datetime.now().strftime('%H:%M')
                            print(f'[{dem}] | {tg} | LIKE | {id} | +300 | {xu}')
                            loi_like = 0
                            if dem % chong_block == 0:
                                delay(delay_block)
                            else:
                                delay(dl)
                            if dem % doi_acc == 0:
                                hvh = 1
                                break
                        else:
                            tg = datetime.now().strftime('%H:%M')
                            print(f'[X] | {tg} | LIKE | {id} | ERROR ')
                            loi_like += 1
                            delay(dl)
            if hvh in (1, 2):
                break
            if '2' in chon:
                get_sub = get_nv('/subcheo', ckvp)
                if len(get_sub) == 0:
                    print('Tạm Thời Hết Nhiệm Vụ Follow', '     ', end='\r')
                if len(get_sub) != 0:
                    print(f'Tìm Thấy {len(get_sub)} Nhiệm Vụ Follow', '     ', end='\r')
                for x in get_sub:
                    id = x['soID']
                    lam = follow(id, cookie, current_user_agent)
                    if lam == '1':
                        if user[0] == 'die':
                            print(f'Cookie Instagram Die !!!!  ')
                            list_cookie.remove(cookie)
                        else:
                            print(f'Tài Khoản {user[0]} Đã Bị Chặn Tương Tác {lam}')
                            list_cookie.remove(cookie)
                        hvh = 2
                        break
                    try:
                        with open(f"{id_ig}.txt", "a+", encoding='utf-8') as data_id:
                            data_id.write(str(id) + ',')
                    except IOError as e:
                        print(f"Error writing to file: {e}")
                        continue
                    dem += 1
                    tg = datetime.now().strftime('%H:%M')
                    print(f'[{dem}] | {tg} | FOLLOW | {id} | SUCCESS')
                    try:
                        with open(f"{id_ig}.txt", "r", encoding='utf-8') as data_id:
                            list = data_id.read()
                    except IOError as e:
                        print(f"Error reading file: {e}")
                        list = ""
                    dem_sub = len(list.split(',')) - 1
                    if dem % chong_block == 0:
                        delay(delay_block)
                    else:
                        delay(dl)
                    if dem_sub >= 6:
                        nhan = nhan_sub(list, ckvp)
                        try:
                            xu_them = nhan['sodu']
                            job = xu_them // 600
                            xu = coin(ckvp)
                            print(f'Nhận Thành Công {job} Nhiệm Vụ Follow | +{xu_them} | {xu}')
                            if os.path.exists(f"{id_ig}.txt"):
                                os.remove(f"{id_ig}.txt")
                            dem_sub = 0
                        except Exception as e:
                            print(f"Error processing follow reward: {nhan} | {e}")
                    if dem % doi_acc == 0:
                        hvh = 1
                        break
            if hvh in (1, 2):
                break
            if '3' in chon:
                get_cmt = get_nv('/cmtcheo', ckvp)
                if len(get_cmt) == 0:
                    print('Tạm Thời Hết Nhiệm Vụ Comment', '     ', end='\r')
                if len(get_cmt) != 0:
                    print(f'Tìm Thấy {len(get_cmt)} Nhiệm Vụ Comment', '     ', end='\r')
                for x in get_cmt:
                    link = x['link']
                    uid = x['idpost']
                    msg = random.choice(json.loads(x['nd']))
                    id = get_id(link, cookie, current_user_agent)
                    if id is False:
                        loi_get_id += 1
                        if loi_get_id >= 5:  # Switch cookie after 5 consecutive get_id failures
                            print(f'{red}Tài Khoản {user[0]} Gặp Quá Nhiều Lỗi Lấy Post ID, Chuyển Cookie')
                            list_cookie.remove(cookie)
                            hvh = 2
                            break
                        continue
                    loi_get_id = 0  # Reset counter on success
                    lam = cmt(msg, id, cookie, current_user_agent)
                    if lam == '1':
                        user = name(cookie, current_user_agent)
                        if user[0] == 'die':
                            print('Cookie Instagram Die !!!! ')
                            list_cookie.remove(cookie)
                            hvh = 2
                            break
                        else:
                            print(f'Tài Khoản {user[0]} Đã Bị Chặn Tương Tác ')
                            list_cookie.remove(cookie)
                            hvh = 2
                            break
                    elif loi_cmt >= 4:
                        print(f'Tài Khoản {user[0]} Đã Bị Chặn Tương Tác')
                        list_cookie.remove(cookie)
                        hvh = 2
                        break
                    elif lam == 'ok':
                        nhan = nhan_tien(uid, ckvp, '/cmtcheo')
                        if 'mess' in nhan:
                            xu = coin(ckvp)
                            dem += 1
                            tg = datetime.now().strftime('%H:%M')
                            print(f'[{dem}] | {tg} | COMMENT | {id} | {msg} | +600 | {xu}')
                            loi_cmt = 0
                            if dem % chong_block == 0:
                                delay(delay_block)
                            else:
                                delay(dl)
                            if dem % doi_acc == 0:
                                hvh = 1
                                break
                        else:
                            tg = datetime.now().strftime('%H:%M')
                            print(f'[X] | {tg} | COMMENT | {id} | ERROR')
                            loi_cmt += 1
                            delay(dl)
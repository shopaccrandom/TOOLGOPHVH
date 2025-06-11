try:
    from curl_cffi import requests
    from curl_cffi.requests.exceptions import TooManyRedirects
    import time
    import os 
    from art import *
    from colorama import Fore
    import json, re
    import random
    from time import sleep
    import sys
    from tabulate import tabulate
    import tempfile
except ImportError:
    import os, sys
    os.system("pip install curl_cffi")
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
    os.system("pip install random2")

# Hardcoded list of User-Agent strings
USER_AGENTS = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1 (iPhone 16)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1 (iPhone 16 Pro)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1 (iPhone 16 Pro Max)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1 (iPhone 16 Plus)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1 (iPhone 15)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1 (iPhone 15 Pro)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1 (iPhone 15 Pro Max)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1 (iPhone 17)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1 (iPhone 17 Pro)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1 (iPhone 17 Pro Max)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1 (iPhone 14)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1 (iPhone 14 Pro)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1 (iPhone SE 4)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1 (iPhone 15 Plus)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1 (iPhone 17 Plus)",
    "Mozilla/5.0 (Linux; Android 14; CPH2573) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 (OPPO Find X7 Pro)",
    "Mozilla/5.0 (Linux; Android 14; CPH2551) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 (OPPO Find X7)",
    "Mozilla/5.0 (Linux; Android 14; CPH2591) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 (OPPO Reno 11 Pro)",
    "Mozilla/5.0 (Linux; Android 14; CPH2577) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 (OPPO Reno 11)",
    "Mozilla/5.0 (Linux; Android 14; CPH2603) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 (OPPO Find X8)",
    "Mozilla/5.0 (Linux; Android 14; CPH2611) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 (OPPO Find X8 Pro)",
    "Mozilla/5.0 (Linux; Android 14; CPH2621) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 (OPPO Reno 12)",
    "Mozilla/5.0 (Linux; Android 14; CPH2631) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 (OPPO Reno 12 Pro)",
    "Mozilla/5.0 (Linux; Android 14; CPH2581) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 (OPPO A79)",
    "Mozilla/5.0 (Linux; Android 14; CPH2599) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 (OPPO A99)",
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 (Galaxy S24 Ultra)",
    "Mozilla/5.0 (Linux; Android 14; SM-S926B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 (Galaxy S24)",
    "Mozilla/5.0 (Linux; Android 14; SM-S921B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 (Galaxy S24 FE)",
    "Mozilla/5.0 (Linux; Android 14; SM-F956B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 (Galaxy Z Fold 6)",
    "Mozilla/5.0 (Linux; Android 14; SM-F946B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 (Galaxy Z Flip 6)",
    "Mozilla/5.0 (Linux; Android 14; SM-A556B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 (Galaxy A55)",
    "Mozilla/5.0 (Linux; Android 14; SM-A356B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 (Galaxy A35)",
    "Mozilla/5.0 (Linux; Android 14; SM-S938B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 (Galaxy S25 Ultra)",
    "Mozilla/5.0 (Linux; Android 14; SM-S936B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 (Galaxy S25)",
    "Mozilla/5.0 (Linux; Android 14; SM-M556B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 (Galaxy M55)",
    "Mozilla/5.0 (Linux; Android 14; SM-F966B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 (Galaxy Z Fold 7)",
    "Mozilla/5.0 (Linux; Android 14; SM-F976B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 (Galaxy Z Flip 7)",
    "Mozilla/5.0 (Linux; Android 14; SM-A566B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 (Galaxy A56)",
    "Mozilla/5.0 (Linux; Android 14; SM-A366B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 (Galaxy A36)",
    "Mozilla/5.0 (Linux; Android 14; SM-S948B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 (Galaxy S25 Plus)"
]

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

def INSTAGRAN(file_name, DELAY, choose):
    if not os.path.exists(file_name):
        print(Fore.RED + "File không tồn tại." + Fore.RESET)
        return

    with open(file_name, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]

    for idx, line in enumerate(lines, 1):
        User_Agent = random.choice(USER_AGENTS)  # Randomly select from hardcoded User-Agent list
        if '|' in line:
            parts = line.split('|', 1)
            if len(parts) == 2:
                NAMEIG, cookie = parts
                NAMEIG = NAMEIG.strip()
                cookie = cookie.strip()
            else:
                print(Fore.RED + f"Dòng {idx} không hợp lệ: {line}" + Fore.RESET)
                continue
        else:
            cookie = line.strip()
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'cache-control': 'max-age=0',
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://www.instagram.com/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': User_Agent,
                'viewport-width': '382',
                'cookie': cookie,
            }
            
            url = 'https://www.instagram.com/'
            try:
                response = requests.get(url, headers=headers, impersonate="chrome", max_redirects=10)
                response.raise_for_status()
                getnameig = response.text
                chuoiname = re.findall(r'"username":"(.*?)"', getnameig)
                jazoest = re.findall(r'jazoest=(.*?)"', getnameig)
                if chuoiname:
                    NAMEIG = chuoiname[0]
                else:
                    print(Fore.RED + f"Không thể lấy username từ cookie tại dòng {idx}." + Fore.RESET)
                    continue
            except TooManyRedirects:
                print(Fore.RED + f"Quá nhiều chuyển hướng tại dòng {idx}. Cookie có thể không hợp lệ." + Fore.RESET)
                continue
            except requests.RequestException as e:
                print(Fore.RED + f"Lỗi khi lấy username tại dòng {idx}: {e}" + Fore.RESET)
                continue

        if not NAMEIG or NAMEIG == 'Instagram User':
            print(Fore.RED + f"Username không hợp lệ hoặc tài khoản có thể đã die tại dòng {idx}: {NAMEIG}" + Fore.RESET)
            continue

        print(f"\n\033[1;33m=== Bắt đầu xử lý cookie với: {NAMEIG} (dòng {idx}) | User_Agent : {User_Agent} ===\033[0m")

        xcsrftoken_match = re.search(r'csrftoken=([^;]+)', cookie)
        if xcsrftoken_match:
            xcsrftoken = xcsrftoken_match.group(1)
        else:
            print(Fore.RED + f"Không tìm thấy csrftoken trong cookie tại dòng {idx}." + Fore.RESET)
            continue

        dem = 0
        tong = 0
        DIE = 0

        headersig = {
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'priority': 'u=1, i',
            'referer': 'https://www.instagram.com/notifications/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.115", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.115"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"SM-G955U"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"8.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': User_Agent,
            'x-asbd-id': '359341',
            'x-csrftoken': xcsrftoken,
            'x-ig-app-id': '1217981644879628',
            'x-ig-www-claim': 'hmac.AR112mGyzPzTzPsiBGMvCn4ykuNiS_amD4aK1jWRQjuRst8C',
            'x-instagram-ajax': '1022547763',
            'x-requested-with': 'XMLHttpRequest',
            'x-web-session-id': 'wy7l3p:3aqprq:sieysj',
            'cookie': cookie,
        }
        headersigcomment = {
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'priority': 'u=1, i',
            'referer': 'https://www.instagram.com/by.maianh_order/p/DJ_Gf8MxIoQ/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': User_Agent,
            'x-asbd-id': '359341',
            'x-csrftoken': xcsrftoken,
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR112mGyzPzTzPsiBGMvCn4ykuNiS_amD4aK1jWRQjuRsvDm',
            'x-instagram-ajax': '1023119282',
            'x-requested-with': 'XMLHttpRequest',
            'x-web-session-id': 'owxwii:2566l1:95ulws',
            'cookie': cookie,
        }

        headersgl = {
            'authorization': authorization,
            't': T,
            'user-agent': User_Agent,
        }

        try:
            thongtinig = requests.get('https://gateway.golike.net/api/instagram-account', headers=headersgl, impersonate="chrome").json()
            if 'status' not in thongtinig:
                print(Fore.RED + f"Lỗi khi lấy thông tin tài khoản Instagram tại dòng {idx}." + Fore.RESET)
                continue

            ID = [i['id'] for i in thongtinig['data']]
            NAMEGI = [i['instagram_username'] for i in thongtinig['data']]
            try:
                index = NAMEGI.index(NAMEIG)
                ID = ID[index]
            except ValueError:
                print(Fore.RED + f"Không tìm thấy username {NAMEIG} trong Golike tại dòng {idx}." + Fore.RESET)
                continue
        except requests.RequestException as e:
            print(Fore.RED + f"Lỗi khi lấy thông tin từ Golike tại dòng {idx}: {e}. Bỏ qua." + Fore.RESET)
            continue

        while dem < choose and DIE == 0:
            try:
                paramsgetjop = {
                    'instagram_account_id': ID,
                    'data': '',
                }
                getjop = requests.get('https://gateway.golike.net/api/advertising/publishers/instagram/jobs', params=paramsgetjop, headers=headersgl, impersonate="chrome").json()
                if getjop['status'] == 200:
                    ads_id = getjop['data']['id']
                    object_id = getjop['data']['object_id']
                    job_type = getjop['data']['type']
                    print(job_type)
                    if job_type == 'follow':
                        url = f'https://www.instagram.com/api/v1/friendships/create/{object_id}/'
                        data = {
                            'container_module': 'profile',
                            'nav_chain': 'PolarisFeedRoot:feedPage:8:topnav-link',
                            'user_id': object_id,
                        }
                        response = requests.post(url, headers=headersig, data=data).text
                        countdown(DELAY)

                        if '"status":"ok"' in response:
                            url = 'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs'
                            json_data = {
                                'instagram_account_id': ID,
                                'instagram_users_advertising_id': ads_id,
                                'async': True,
                                'data': '',
                            }
                            time.sleep(3)
                            response = requests.post(url, headers=headersgl, json=json_data, impersonate="chrome").json()
                            if response.get('success') == True:
                                dem += 1
                                local_time = time.localtime()
                                h, m, s = [f"{t:02d}" for t in (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)]
                                prices = response['data']['prices']
                                tong += prices
                                chuoi = (
                                    f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                    f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                    f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                    f"\033[1;31mfollow\033[1;31m\033[1;32m\033[1;97m | "
                                    f"\033[1;32mẨn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                    f"\033[1;33m{tong} vnđ"
                                )
                                print(chuoi)
                            else:
                                json_data = {
                                    'ads_id': ads_id,
                                    'object_id': object_id,
                                    'account_id': ID,
                                    'type': job_type,
                                }
                                checkskipjob = requests.post(
                                    'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',
                                    headers=headersgl,
                                    json=json_data,
                                    impersonate="chrome"
                                ).json()
                                if checkskipjob['status'] == 200:
                                    print(Fore.RED + str(checkskipjob['message']) + Fore.RESET)
                        elif '"message":"checkpoint_required"' in response:
                            print(Fore.RED + f"Tài khoản bị checkpoint tại dòng {idx}." + Fore.RESET)
                            DIE = 1
                        elif '"status":"fail"' in response and '"spam":true' in response:
                            print(Fore.RED + f"Tài khoản bị chặn follow tại dòng {idx}." + Fore.RESET)
                            DIE = 1
                        elif '"status":"fail"' in response and '"require_login":true' in response:
                            print(Fore.RED + f"Cookie die tại dòng {idx}." + Fore.RESET)
                            DIE = 1
                        else:
                            json_data = {
                                'ads_id': ads_id,
                                'object_id': object_id,
                                'account_id': ID,
                                'type': job_type,
                            }
                            checkskipjob = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',
                                headers=headersgl,
                                json=json_data,
                                impersonate="chrome"
                            ).json()
                            if checkskipjob['status'] == 200:
                                print(Fore.RED + str(checkskipjob['message']) + Fore.RESET)

                    elif job_type == 'like':
                        like_id1 = getjop['data']['description']
                        like_id = like_id1.split('_')[0]
                        url = f'https://www.instagram.com/api/v1/web/likes/{like_id}/like/'
                        response = requests.post(url, headers=headersig).text
                        print(response)
                        countdown(DELAY)

                        if '"status":"ok"' in response:
                            url = 'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs'
                            json_data = {
                                'instagram_account_id': ID,
                                'instagram_users_advertising_id': ads_id,
                                'async': True,
                                'data': '',
                            }
                            time.sleep(3)
                            response = requests.post(url, headers=headersgl, json=json_data, impersonate="chrome").json()
                            if response['success'] == True:
                                dem += 1
                                local_time = time.localtime()
                                h, m, s = [f"{t:02d}" for t in (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)]
                                prices = response['data']['prices']
                                tong += prices
                                chuoi = (
                                    f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                    f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                    f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                    f"\033[1;31mlike\033[1;31m\033[1;32m\033[1;97m | "
                                    f"\033[1;32mẨn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                    f"\033[1;33m{tong} vnđ"
                                )
                                print(chuoi)
                            else:
                                json_data = {
                                    'ads_id': ads_id,
                                    'object_id': object_id,
                                    'account_id': ID,
                                    'type': 'like',
                                }
                                checkskipjob = requests.post(
                                    'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',
                                    headers=headersgl,
                                    json=json_data,
                                    impersonate="chrome"
                                ).json()
                                if checkskipjob['status'] == 200:
                                    print(Fore.RED + str(checkskipjob['message']) + Fore.RESET)
                        elif '"message":"checkpoint_required"' in response:
                            print(Fore.RED + f"Tài khoản bị checkpoint tại dòng {idx}." + Fore.RESET)
                            DIE = 1
                        elif '"status":"fail"' in response and '"spam":true' in response:
                            print(Fore.RED + f"Tài khoản bị chặn like tại dòng {idx}." + Fore.RESET)
                            DIE = 1
                        elif '"status":"fail"' in response and '"require_login":true' in response:
                            print(Fore.RED + f"Cookie die tại dòng {idx}." + Fore.RESET)
                            DIE = 1
                        else:
                            json_data = {
                                'ads_id': ads_id,
                                'object_id': object_id,
                                'account_id': ID,
                                'type': job_type,
                            }
                            checkskipjob = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',
                                headers=headersgl,
                                json=json_data,
                                impersonate="chrome"
                            ).json()
                            if checkskipjob['status'] == 200:
                                print(Fore.RED + str(checkskipjob['message']) + Fore.RESET)
                                    
                    elif job_type == 'comment':
                        comment_id = getjop['lock']['comment_id']
                        instagram_account_id = getjop['lock']['instagram_account_id']
                        instagram_users_advertising_id = getjop['lock']['instagram_users_advertising_id']
                        messagecomment = getjop['lock']['message']
                        idcomment = getjop['data']['description']
                        link = getjop['data']['link']
                        ID_COMMENT = idcomment.split('_')[0]

                        data = {
                            'comment_text': messagecomment,
                            'jazoest': jazoest,
                        }
                        response = requests.post(f'https://www.instagram.com/api/v1/web/comments/{ID_COMMENT}/add/', headers=headersigcomment, data=data).text
                        countdown(20)
                        if '"status":"ok"' in response:
                            json_data = {
                                'instagram_users_advertising_id': instagram_users_advertising_id,
                                'instagram_account_id': instagram_account_id,
                                'async': True,
                                'data': None,
                                'comment_id': comment_id,
                                'message': messagecomment,
                            }
                            response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
                                headers=headersgl,
                                json=json_data,
                                impersonate="chrome"
                            ).json()
                            if response['success'] == True:
                                dem += 1
                                local_time = time.localtime()
                                h, m, s = [f"{t:02d}" for t in (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)]
                                prices = response['data']['prices']
                                tong += prices
                                chuoi = (
                                    f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                    f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                    f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                    f"\033[1;31mcomment\033[1;31m\033[1;32m\033[1;97m | "
                                    f"\033[1;31mlink\033[1;31m[{link}] \033[1;32m\033[1;97m "
                                    f"\033[1;32mẨn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                    f"\033[1;33m{tong} vnđ"
                                )
                                print(chuoi)
                            else:
                                print('Trang không tồn tại hoặc bài đăng chưa bật công khai comment')
                                json_data = {
                                    'ads_id': ads_id,
                                    'object_id': object_id,
                                    'account_id': ID,
                                    'type': job_type,
                                }
                                checkskipjob = requests.post(
                                    'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',
                                    headers=headersgl,
                                    json=json_data,
                                    impersonate="chrome"
                                ).json()
                                if checkskipjob['status'] == 200:
                                    print(Fore.RED + str(checkskipjob['message']) + Fore.RESET)
                        else:
                            json_data = {
                                'ads_id': ads_id,
                                'object_id': object_id,
                                'account_id': ID,
                                'type': job_type,
                            }
                            checkskipjob = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',
                                headers=headersgl,
                                json=json_data,
                                impersonate="chrome"
                            ).json()
                            if checkskipjob['status'] == 200:
                                print(Fore.RED + str(checkskipjob['message']) + Fore.RESET)
                else:
                    print(Fore.RED + f"{getjop['message']} tại dòng {idx}." + Fore.RESET)
                    if 'Vui lòng bấm lại load job' in getjop['message']:
                        pass
                    else:
                        break

            except Exception as e:
                print(Fore.RED + f"Lỗi tại dòng cookie {idx}: KHOẢN ĐÃ BỊ KHÓA. Bỏ qua job." + Fore.RESET)
                break

        print(f"\033[1;32mHoàn thành {dem} job cho cookie tại dòng {idx}. Tổng tiền: {tong} vnđ\033[0m")
        if DIE == 1:
            print(Fore.RED + f"COOKIE DIE tại dòng {idx}, chuyển sang cookie tiếp theo..." + Fore.RESET)

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush() 
        sleep(0.00125)

if __name__ == "__main__":
    banner()
    authorization = input('NHẬP authorization:')
    T = input('NHẬP T :')
    print(Fore.CYAN + "Chọn chức năng:")
    print(Fore.GREEN + "1. Chạy xử lý job Instagram (định dạng file : cookie)")
    print(Fore.GREEN + "2. Instagram (định dạng file : name|cookie)")
    print(Fore.GREEN + "3. Nhập cookie thủ công")
    choice = input(Fore.YELLOW + "Nhập lựa chọn (1, 2 hoặc 3): " + Fore.RESET)

    if choice == '1':
        DELAY = int(input(Fore.RED + '\033[1;97m[\033[1;91m✨\033[1;97m] \033[1;36m☄️  Nhập Delay : '))
        choose = int(input(Fore.RED + '\033[1;97m[\033[1;91m✨\033[1;97m] \033[1;36m☄️  Nhập Số Lượng Job : '))
        file_name = input(Fore.YELLOW + "Nhập tên file chứa các cookie: " + Fore.RESET)
        banner()
        INSTAGRAN(file_name, DELAY, choose)
    elif choice == '2':
        while True:
            file_name = input(Fore.YELLOW + "Nhập tên file chứa các name|cookie: " + Fore.RESET)
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as f:
                    lines = [line.strip() for line in f.readlines() if line.strip()]
                if os.path.exists('cookiepass.txt'):
                    with open('cookiepass.txt', 'r', encoding='utf-8') as f:
                        existing_entries = {line.strip().split('|')[1].strip() for line in f if line.strip() and '|' in line}
                else:
                    existing_entries = set()

                valid_entries = []
                duplicate_count = 0
                invalid_count = 0

                for line in lines:
                    if line.count('|') == 1:
                        name, cookie = [part.strip() for part in line.split('|', 1)]
                        if name and cookie:
                            if cookie not in existing_entries:
                                valid_entries.append(f"{name}|{cookie}")
                                existing_entries.add(cookie)
                            else:
                                duplicate_count += 1
                        else:
                            invalid_count += 1
                    else:
                        invalid_count += 1

                if valid_entries:
                    with open('cookiepass.txt', 'a', encoding='utf-8') as f:
                        for entry in valid_entries:
                            f.write(entry + '\n')
                    print(Fore.GREEN + f"Đã thêm {len(valid_entries)} entry hợp lệ." + Fore.RESET)

                if duplicate_count > 0:
                    print(Fore.YELLOW + f"Có {duplicate_count} entry trùng lặp đã bị bỏ qua." + Fore.RESET)

                if invalid_count > 0:
                    print(Fore.RED + f"Có {invalid_count} entry không hợp lệ đã bị bỏ qua." + Fore.RESET)
                break
            else:
                print(Fore.RED + "File không tồn tại. Vui lòng nhập lại." + Fore.RESET)

        run_jobs = input(Fore.YELLOW + "Bạn có muốn chạy xử lý job bây giờ không? (y/n): " + Fore.RESET)
        if run_jobs.lower() == 'y':
            DELAY = int(input(Fore.RED + '\033[1;97m[\033[1;91m✨\033[1;97m] \033[1;36m☄️  Nhập Delay : '))
            choose = int(input(Fore.RED + '\033[1;97m[\033[1;91m✨\033[1;97m] \033[1;36m☄️  Nhập Số Lượng Job : '))
            banner()
            INSTAGRAN(file_name, DELAY, choose)
        else:
            print(Fore.CYAN + "Kết thúc chương trình." + Fore.RESET)
    elif choice == '3':
        print(Fore.CYAN + "Nhập cookie hoặc name|cookie, nhấn Enter để kết thúc." + Fore.RESET)
        cookie_lines = []
        count = 1  # Biến đếm để hiển thị thứ tự
        while True:
            input_line = input(Fore.YELLOW + f"Nhập cookie hoặc name|cookie thứ {count}: " + Fore.RESET).strip()
            if not input_line:
                break
            cookie_lines.append(input_line)
            count += 1
        if cookie_lines:
            DELAY = int(input(Fore.RED + '\033[1;97m[\033[1;91m✨\033[1;97m] \033[1;36m☄️  Nhập Delay : '))
            choose = int(input(Fore.RED + '\033[1;97m[\033[1;91m✨\033[1;97m] \033[1;36m☄️  Nhập Số Lượng Job : '))
            with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
                for line in cookie_lines:
                    temp_file.write(line + '\n')
                temp_file.flush()
                file_name = temp_file.name
            try:
                banner()
                INSTAGRAN(file_name, DELAY, choose)
            finally:
                os.remove(file_name)
        else:
            print(Fore.YELLOW + "Không có cookie nào được nhập." + Fore.RESET)
    else:
        print(Fore.RED + "Lựa chọn không hợp lệ." + Fore.RESET)
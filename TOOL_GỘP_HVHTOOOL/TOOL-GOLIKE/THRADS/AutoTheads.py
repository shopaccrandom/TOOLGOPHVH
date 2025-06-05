try:
    from curl_cffi import requests
    import time
    import os
    from art import *
    from colorama import Fore
    import json
    import random
    from tabulate import tabulate
    import re
    from time import sleep
    import sys
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem
except ImportError:
    os.system("pip install curl_cffi")  # Install curl_cffi instead of requests
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
    os.system("pip install random_user_agent")

# Define software names and operating systems for user agent rotation
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
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

def THREADS():
    checkaccount = requests.get('https://gateway.golike.net/api/threads-account',headers=headers,impersonate="chrome").json()
    user_THREADS = []
    account_id1 = []
    STT = []
    STATUS =[]
    tong = 0
    dem = 0
    i=1
    for data in checkaccount['data'] :
            usernametk = data['name']
            # print(str(i)+'.'+usernametk)
            user_THREADS.append(data['name'])
            account_id1.append(data['id'])
            STT.append(i)
            STATUS.append(Fore.GREEN+"Hoạt Động"+Fore.RED)
        # create header
            print(f'\033[1;36m[{i}] \033[1;36m✈ \033[1;97mTài Khoản┊\033[1;32m㊪ :\033[1;93m {usernametk} \033[1;97m|\033[1;32m㊪ :\033[1;93m {STATUS[-1]}')
            i += 1
    
    print('\033[97m════════════════════════════════════════════════')
    choose = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Tài Khoản : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_THREADS) :
        user_THREADS = user_THREADS[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_THREADS[0] 
        account_id = account_id1[0]
        checkfile2 = os.path.isfile('COOKIETHR'+str(account_id)+'.txt')
        if checkfile2 == False:
            banner()
            cookieX = input(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Cookie Threads : ')
            createfile = open('COOKIETHR'+str(account_id)+'.txt','w')
            createfile.write(cookieX)
            createfile.close()
            readfile = open('COOKIETHR'+str(account_id)+'.txt','r')
            cookieTHR = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIETHR'+str(account_id)+'.txt','r')
            cookieTHR = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        banner()
        print(Fore.RED+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập 1 Để Sử Dụng Cookie Cữ : ')
        print(Fore.RED+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập 2 Để Xóa Cookie : ')
        URchoose = int(input(Fore.WHITE+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Lựa Chọn : '))
        if URchoose == 2:
             os.remove('COOKIETHR'+str(account_id)+'.txt')
             return 0
        os.system('cls' if os.name== 'nt' else 'clear')
        banner()
        choose = int(input(Fore.RED+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Số Lượng Job : '))
        
        param = {
             'account_id':str(account_id)
        }
        DELAY = int(input(Fore.RED+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Delay : '))
        print("\033[97m════════════════════════════════════════════════")
        print(f'\033[1;36m|STT\033[1;97m| \033[1;33mThời gian ┊ \033[1;32mStatus | \033[1;31mType Job | \033[1;32mID Acc | \033[1;32mXu |\033[1;33m Tổng')
        for i in range(choose):
            try:
                headerscheck = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'dpr': '1',
                    'priority': 'u=0, i',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
                    'sec-ch-ua-full-version-list': '"Chromium";v="136.0.7103.114", "Google Chrome";v="136.0.7103.114", "Not.A/Brand";v="99.0.0.0"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-model': '"Nexus 5"',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"6.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
                    'viewport-width': '595',
                    'cookie': cookieTHR,
                    # 'cookie': 'ig_did=5B9698C1-D2E9-4F5E-98D7-F3D43E4C934B; mid=aCl0GgALAAHMOhpHcmgFRAH6ZH6o; csrftoken=vuP2NiwnGVtLyxVZznTsh294obRuDBUX; ds_user_id=74704726894; dpr=2; sessionid=74704726894%3A2FmXAs79r0oZek%3A26%3AAYdnPjDcQqKJYd4LQdYWzdwoU_qZT5nt4re6ayGbaA',
                }
                headersTHR = {
                    'accept': '*/*',
                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': cookieTHR,
                    'origin': 'https://www.threads.net',
                    'priority': 'u=1, i',
                    'referer': 'https://www.threads.net/@dreyt041',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.182", "Google Chrome";v="126.0.6478.182"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-model': '"Pixel 5"',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"13"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'user_agent',
                    'x-asbd-id': '129477',
                    'x-csrftoken': cookieTHR.split('csrftoken=')[1].split(';')[0],
                    'x-fb-friendly-name': 'useBarcelonaFollowMutationFollowMutation',
                    'x-fb-lsd': '6Z5u6bYBj-kOXPD0nbgSGu',
                    'x-ig-app-id': '238260118697367',
                }
                job = 'https://gateway.golike.net/api/advertising/publishers/threads/jobs?account_id='+str(account_id)
                nos = ses.get(job,headers=headers,params=param,impersonate="chrome").json()
                #print(cookieTHR)
                #print(nos)
                if nos['status'] ==200:
                    ads_id = nos['data']['id']
                    object_id = nos['data']['object_id']
                    type = nos['data']['type']
                    #user_id=nos['lock']['user_id']
                    link = nos['data']['link']
                    print(type)
                    #print(link)
                    if type == 'follow':
                        try :
                            url = link
                            try:
                                check1 = requests.get('https://www.threads.com/',headers=headerscheck).text
                                fb_dtsg = check1.split('"f":"')[1].split('",')[0]
                            except:
                                print('cookie die!!!!')

                            check = requests.get(link,headers=headerscheck).text
                            match = re.search(r'"userID":\s*"(\d+)"',check)
                            user_id = match.group(1)
                            print(user_id)
                            #print(fb_dtsg)
# Check if the token was found and extract i
                 
         # Output: QdCIlxrxZvC931peM9WzINm1A4jpqKAt
                            data = {
                            'av': '17841461328267610',
                            '__user': '0',
                            '__a': '1',
                            '__req': 'c',
                            '__hs': '19925.HYP:barcelona_web_pkg.2.1..0.1',
                            'dpr': '1',
                            '__ccg': 'UNKNOWN',
                            '__rev': '1015041514',
                            '__s': '4oqz5z:tfv4jd:iv92im',
                            '__hsi': '7394241910778378470',
                            '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0om782Cw8G11wBz81s8hwGwQw9m1YwBgao6C0Mo2swlo5qfK0EUjwGzE2ZwNwmE2eUlwhE2Lx-0iS2S3qazo7u0zE2ZwrUdUbGw4mwr86C2q1iwiQ1mwLwHxW17y9UjgdE-19w',
                            '__csr': 'gV2QPfHkGNcIQZFAjlqvap8lbc9qyBByp99O96y9o01J73a4A5hlwQSaxshDk9a4Ujgakph3DS7o6K0_A0hvc2p1afwk41jx7OhM1SmEiglwqcM4d01vhx22t0FhYg0QFA',
                            '__comet_req': '29',
                            'fb_dtsg': fb_dtsg,
                            'jazoest': '26086',
                            'lsd': '6Z5u6bYBj-kOXPD0nbgSGu',
                            '__spin_r': '1015041514',
                            '__spin_b': 'trunk',
                            '__spin_t': '1721606103',
                            'fb_api_caller_class': 'RelayModern',
                            'fb_api_req_friendly_name': 'useBarcelonaFollowMutationFollowMutation',
                            'variables': '{"target_user_id":'+str(user_id)+',"media_id_attribution":null,"container_module":"ig_text_feed_profile"}',
                            'server_timestamps': 'true',
                            'doc_id': '7812622502155806',
                        }
                            response = requests.post('https://www.threads.net/api/graphql', headers=headersTHR, data=data).text
                            print(response)
                            countdown(DELAY)
                            if '"following":true' in response:
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/threads/complete-jobs',
                                headers=headers,
                                json=json_data,
                                impersonate="chrome"
                                ).json()
                                #print(response)
                                if response['success']==True:
                                    dem += 1
                                    local_time = time.localtime()
                                    hour = local_time.tm_hour
                                    minute = local_time.tm_min
                                    second = local_time.tm_sec

                                    # Định dạng giờ, phút, giây
                                    h = f"{hour:02d}"
                                    m = f"{minute:02d}"
                                    s = f"{second:02d}"
                                    prices =response['data']['prices']


                                    # Cộng dồn giá trị prices vào tổng tiền
                                    tong += prices

                                    chuoi = (
                                        f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                        f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                        f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                        f"\033[1;31mfollow\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                        f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                        f"\033[1;33m{tong} vnđ"
                                    )
                                    print(chuoi)
                                else:
                                    print(response['message'])
                                    json_data = {
                                        'account_id': account_id,
                                        'ads_id': ads_id,
                                        'object_id': object_id,
                                    }
                                    checkskipjob = ses.post(
                                        'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs',
                                        headers=headers,
                                        json=json_data,
                                        impersonate="chrome"
                                    ).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                            elif "A server error critical occured. Check server logs for details" in response:
                                if response['success']==True:
                                    dem += 1
                                    local_time = time.localtime()
                                    hour = local_time.tm_hour
                                    minute = local_time.tm_min
                                    second = local_time.tm_sec

                                    # Định dạng giờ, phút, giây
                                    h = f"{hour:02d}"
                                    m = f"{minute:02d}"
                                    s = f"{second:02d}"
                                    prices =response['data']['prices']


                                    # Cộng dồn giá trị prices vào tổng tiền
                                    tong += prices

                                    chuoi = (
                                        f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                        f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                        f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                        f"\033[1;31mlike  \033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                        f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                        f"\033[1;33m{tong} vnđ"
                                    )
                                    print(chuoi)
                                else:
                                    json_data = {
                                        'account_id': account_id,
                                        'ads_id': ads_id,
                                        'object_id': object_id,
                                    }
                                    checkskipjob = ses.post(
                                        'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs',
                                        headers=headers,
                                        json=json_data,
                                        impersonate="chrome"
                                    ).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                            else:
                                print('có thể là bị block follow')
                                json_data = {
                                        'account_id': account_id,
                                        'ads_id': ads_id,
                                        'object_id': object_id,
                                    }
                                checkskipjob = ses.post(
                                        'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs',
                                        headers=headers,
                                        json=json_data,
                                        impersonate="chrome"
                                    ).json()
                                if checkskipjob['status'] == 200:
                                    message = checkskipjob['message']
                                    print(Fore.RED+str(message))
                        except :
                            json_data = {
                                        'account_id': account_id,
                                        'ads_id': ads_id,
                                        'object_id': object_id,
                                    }
                            checkskipjob = ses.post(
                                        'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs',
                                        headers=headers,
                                        json=json_data,
                                        impersonate="chrome"
                                    ).json()
                            if checkskipjob['status'] == 200:
                                message = checkskipjob['message']
                                print(Fore.RED+str(message))
                    elif type == 'like':
                        try :
                            try:
                                check1 = requests.get('https://www.threads.com/',headers=headerscheck).text
                                fb_dtsg = check1.split('"f":"')[1].split('",')[0]
                            except:
                                print('cookie die!!!!')
                            check = requests.get(link,headers=headerscheck).text
                            match = re.search(r'"postID":\s*"(\d+)"', check)
                            post_id = match.group(1)
                            print(post_id)
                            
                            data = {
                                'av': '17841465195438651',
                                '__user': '0',
                                '__a': '1',
                                '__req': '13',
                                '__hs': '19926.HYP:barcelona_web_pkg.2.1..0.1',
                                'dpr': '1',
                                '__ccg': 'UNKNOWN',
                                '__rev': '1015041902',
                                '__s': 'gmmbni:g1innv:0tm2do',
                                '__hsi': '7394261959223963838',
                                '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0om782Cw8G11wBz81s8hwGwQw9m1YwBgao6C0Mo2swlo5qfK0EUjwGzE2ZwNwmE2eUlwhE2Lx-0iS2S3qazo7u0zE2ZwrUdUbGw4mwr86C2q6oe84J0lEbUaUuwhUyu4Q3qfwio',
                                '__csr': 'gV2QP9mJiHkTYQZFAjlqvap8lbc9qKpqG9AAD8Cm8Bw06QscEigl5m3joG5N6tgAEjxd0FhB4evotwqU3-g15YM9A4E-1gg5e4v9706Gy89mEiglwqcM4d01vhx22t0FhYg0QFA58',
                                '__comet_req': '29',
                                'fb_dtsg': fb_dtsg,
                                'jazoest': '26398',
                                'lsd': 'cQ5UmUjtTg4rd7wo5B_3qv',
                                '__spin_r': '1015041902',
                                '__spin_b': 'trunk',
                                '__spin_t': '1721610771',
                                'fb_api_caller_class': 'RelayModern',
                                'fb_api_req_friendly_name': 'useBarcelonaLikeMutationLikeMutation',
                                'variables': '{"mediaID":'+str(post_id)+'}',
                                'server_timestamps': 'true',
                                'doc_id': '24068295876148027',
                            }
                            response = requests.post('https://www.threads.net/api/graphql', headers=headersTHR, data=data).text
                            print(response)
                            countdown(DELAY)
                            if '"is_final":true' in response or '"has_liked":true' in response:
                                json_data = {
                                'account_id': account_id,
                                'ads_id': ads_id,
                                }
                                time.sleep(3)
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/threads/complete-jobs',
                                headers=headers,
                                json=json_data,
                                impersonate="chrome"
                                ).json()
                                #print(response)
                                if response['success']==True:
                                    dem += 1
                                    local_time = time.localtime()
                                    hour = local_time.tm_hour
                                    minute = local_time.tm_min
                                    second = local_time.tm_sec

                                    # Định dạng giờ, phút, giây
                                    h = f"{hour:02d}"
                                    m = f"{minute:02d}"
                                    s = f"{second:02d}"
                                    prices =response['data']['prices']


                                    # Cộng dồn giá trị prices vào tổng tiền
                                    tong += prices

                                    chuoi = (
                                        f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                                        f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                                        f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                        f"\033[1;31mlike  \033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                        f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                        f"\033[1;33m{tong} vnđ"
                                    )
                                    print(chuoi)

                                else:
                                    print(response['message'])
                                    json_data = {
                                        'account_id': account_id,
                                        'ads_id': ads_id,
                                        'object_id': object_id,
                                    }
                                    checkskipjob = ses.post(
                                        'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs',
                                        headers=headers,
                                        json=json_data,
                                        impersonate="chrome"
                                    ).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                            else:
                                print('có thể là bị block follow')
                                json_data = {
                                        'account_id': account_id,
                                        'ads_id': ads_id,
                                        'object_id': object_id,
                                    }
                                checkskipjob = ses.post(
                                        'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs',
                                        headers=headers,
                                        json=json_data,
                                        impersonate="chrome"
                                    ).json()
                                if checkskipjob['status'] == 200:
                                    message = checkskipjob['message']
                                    print(Fore.RED+str(message))
                    
                        except :
                            print('lỗi trong lúc chạy có thể là ko có trang')
                            json_data = {
                                'account_id': account_id,
                                'ads_id': ads_id,
                                'object_id': object_id,
                            }
                            checkskipjob = ses.post(
                                'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs',
                                headers=headers,
                                json=json_data,
                                impersonate="chrome"
                            ).json()
                            if checkskipjob['status'] == 200:
                                message = checkskipjob['message']
                                print(Fore.RED+str(message))
                    elif type =='comment':
                        print('bỏ quả comment')
                        json_data = {
                            'account_id': account_id,
                            'ads_id': ads_id,
                            'object_id': object_id,
                        }
                        checkskipjob = ses.post(
                            'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs',
                            headers=headers,
                            json=json_data,
                            impersonate="chrome"
                        ).json()
                        if checkskipjob['status'] == 200:
                            message = checkskipjob['message']
                            print(Fore.RED+str(message))
                
                else:
                    print(nos['message'])
                    sleep(5)
            except TypeError :
                print('die die [kiểm tra xem đã thên tài khoản vaofgolike chưa]')
def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f"""
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)

def LIST():
    banner()
    
os.system('cls' if os.name== 'nt' else 'clear')
banner()
checkfile = os.path.isfile('user.txt')
if checkfile == False:
    AUTHUR = input(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNHẬP Authorization Golike : ')
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
ses = requests.Session()
User_Agent = random.choice([
    "android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9100 Build/KTU84P) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/50.0.3755.367 Mobile Safari/600.8",
    "android|Mozilla/5.0 (Linux; Android 5.0; SM-N910V Build/LRX22C) AppleWebKit/601.33 (KHTML, like Gecko) Chrome/54.0.1548.302 Mobile Safari/537.0",
])
headers = {'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
            'Referer':'https://app.golike.net/',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-site',
            'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
            'User-Agent':User_Agent,
            "Authorization" : file,
            'Content-Type':'application/json;charset=utf-8'            
}

url1 = 'https://gateway.golike.net/api/users/me'
checkurl1 = ses.get(url1,headers=headers,impersonate="chrome").json()
    #user
if checkurl1['status']== 200 :
        print('DANG NHAP THANH CONG')
        time.sleep(3)
        os.system('cls' if os.name== 'nt' else 'clear')
        username = checkurl1['data']['username']
        coin = checkurl1['data']['coin']
        user_id = checkurl1['data']['id']
        print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTài Khoản : '+Fore.YELLOW+username)
        print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTổng Tiền : '+Fore.YELLOW+str(coin))
        print(Fore.RED+'\033[97m════════════════════════════════════════════════')
        print("\033[1;32mNhập \033[1;31m1 \033[1;33mđể vào \033[1;34mTool Threads\033[1;33m")
        print(Fore.RED+'Nhập 2 Để Xóa Authorization Hiện Tại')
        choose = int(input(Fore.WHITE+'Nhập Lựa Chọn : '))
        if choose == 1:
            os.system('cls' if os.name== 'nt' else 'clear')
            banner()
            username = checkurl1['data']['username']
            coin = checkurl1['data']['coin']
            user_id = checkurl1['data']['id']
            print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTài Khoản : '+Fore.YELLOW+username)
            print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTổng Tiền : '+Fore.YELLOW+str(coin))
            print(Fore.RED+'\033[97m════════════════════════════════════════════════')
            THREADS()
        elif choose == 2:
                os.remove('user.txt')
else:
    print(Fore.RED+'DANG NHAP THAT BAI')
    os.remove('user.txt')
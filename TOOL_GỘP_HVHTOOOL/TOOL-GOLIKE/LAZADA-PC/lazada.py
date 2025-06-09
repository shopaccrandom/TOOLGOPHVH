try :
    from curl_cffi import requests
    import time
    import os 
    from art import *
    from colorama import Fore
    import time
    import json
    import random
    from time import sleep
    import sys
    from tabulate import tabulate
except ImportError:
    import os,sys
    os.system("pip install random2")
    os.system("pip install curl-cffi")
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")

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
banner()
time_sec = int(input('Nhập Delay làm Jop:'))  
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
def LAZADA():
    authorization=input('Nhập authorization:')
    T = input('Nhập T:')
    dem=0
    tong=0
    prices =0
    headersgl = {
    'authorization': authorization,
    't': T,
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    }

    acclazada = requests.get('https://gateway.golike.net/api/lazada-account', headers=headersgl,impersonate="chrome").json()
    if 'status' in acclazada :
        ID = acclazada['data'][0]['id']
        for i in range(100):
            try:
            #==========================GET JOP=====================================
                params = {
                    'account_id': ID,
                }
                Getjop = requests.get('https://gateway.golike.net/api/advertising/publishers/lazada/jobs', params=params, headers=headersgl,impersonate="chrome").json()
                #print(Getjop)
                if 'status' in Getjop and Getjop['status'] == 200:
                    adsid=Getjop['lock']['ads_id']
                    type=Getjop['data']['package_name']
                    odjecid=Getjop['data']['package_name']
                else:
                    m=Getjop['message']
                    print(m)
                    countdown(10)
                    continue

                countdown(time_sec)
                #============================hoàn thành jop
                json_data = {
                    'ads_id': adsid,
                    'account_id': ID,
                    'async': True,
                    'data': None,
                    #'captcha_token': '03AFcWeA6acCZJPFQa2fgfuJc8WB88GtF_vFsWIrHT7LHny4ZDQpaVWca0P7d8NuEgzNJKvoNlzns3obO-cSiJ2e8p2_6oH6Xrq4Y9ts2u6Vgnuj3wXEkseW4EPjkpIW_ljPwL3nLP7QK2KYpP65nbG7vIE-ZITabeYcbBPxtdMo-C5GFF4G10RlGdfDWD-tVQP9LpHW1R-yhLGrQhWKhSGJ2UjYFMFmfgvSHFoj5sAYSptJgEKX2yCScMi8FrRRjuCAkpmzk3gFmx6hre7Z1ZvlJb8P0F4cRxr3G7OAjqQDlsv7ZY3Wk2zFcXcWC7VrxhdFiNYf2hVLRsUjFhlICiAXLc3uPR6yDXHr_O8-xBML44pZhkUDTaerjgaC4nZ-wDepxqu3pPwKvZXw_M5254pao0XhKMMasNd_jkEwPvEKI7xkk3Tmm8szC66qxz5-YKjD1zq6Q9aGLjwA8WJ6sStn2xA6Ln0AR-uubc5hTe9RmgOnM0K9w1lGh0BemDOaBNTwPtSYHtP4xeFx5kOtNtrviu5TlAjwC8LWl2n6WzO--r2inOveHkmbcUReDZVqTE5FL700kdrfwm4FaAmXoZlSWWkqJnR1qjlwBKBsfVvShWamAqIr5kz80irmrMIZd16wVFK4vaqCkI3QXWHpjJSLVW6IeRkKU3GEOsjhDu85ZYt5XPNFvIA97G4iZpuhFU7W8tECGWWbHaOvUyByqJyptRtrUgZNTbTP45PgDy8N9h2lAt_Gpr-_rVy9X26nRnhPGeNQRL7q9Dzi0dV8JspHv6-ekr-VahCDlbMDJaGXY4VmzodX9h19SYvqASMg1srfbCD1cl3-mnCfoNdDJN8HRlp24TCW1O2fyT1vGJFtOyqrI-ghSbyen6ZdSU2dxAmzvjtogEakg_MuaAMR0617H9hR4jlsSmW7I6cHC9eBv3ylel9BvFwOuexOZxFiB7LQG19EVE91e1UUafYTGDBsf97pjCV_VlRo5nUFY0IoC2LbrO51eLbgIKzgzMFn0NeZMEkIpP_Ebm',
                    #'captcha': 'recaptcha',
                }
                hoanthanh = requests.post(
                    'https://gateway.golike.net/api/advertising/publishers/lazada/complete-jobs',
                    headers=headersgl,
                    json=json_data,
                    impersonate="chrome"
                ).json()
                #print(hoanthanh)
                hoanthanh['message']
                if 'Báo cáo thành công' in hoanthanh['message']:
                    dem += 1
                    local_time = time.localtime()
                    hour = local_time.tm_hour
                    minute = local_time.tm_min
                    second = local_time.tm_sec
                    # Định dạng giờ, phút, giây
                    h = f"{hour:02d}"
                    m = f"{minute:02d}"
                    s = f"{second:02d}"
                    prices = hoanthanh['data']['prices']
                    # Cộng dồn giá trị prices vào tổng tiền
                    tong += prices

                    chuoi = (
                        f"\033[1;31m\033[1;36m{dem}\033[1;31m\033[1;97m | "
                        f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                        f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                        f"\033[1;31mfollow\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                        f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                        f"\033[1;33m{tong} vnđ"
                    )
                    print(chuoi) 
                else:
                    json_data = {
                    'ads_id': adsid,
                    'object_id': odjecid,
                    'account_id': ID,
                    'type': type,
                }

                    response = requests.post(
                        'https://gateway.golike.net/api/advertising/publishers/lazada/skip-jobs',
                        headers=headersgl,
                        json=json_data,
                        impersonate="chrome"
                    ).json()
                    print(response['message'])
            except:
                json_data = {
                    'ads_id': adsid,
                    'object_id': odjecid,
                    'account_id': ID,
                    'type': type,
                }

                response = requests.post(
                    'https://gateway.golike.net/api/advertising/publishers/lazada/skip-jobs',
                    headers=headersgl,
                    json=json_data,
                    impersonate="chrome"
                )
                print(response['message'])

    else:
        print('CHƯA THÊM acc lazada đi')
LAZADA()
        
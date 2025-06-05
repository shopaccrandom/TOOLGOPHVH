try:
    from curl_cffi import requests
    from curl_cffi.requests.exceptions import TooManyRedirects  # Import the exception
    import time
    import os 
    from art import *
    from colorama import Fore
    import json, re
    import random
    from time import sleep
    import sys
    from tabulate import tabulate
except ImportError:
    import os,sys
    os.system("pip install curl_cffi")
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
    os.system("pip install random2")

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

def getthongtin():

    headers = {
        f'authorization':Authorizationgolike,
        f'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    }
    getthongtin = requests.get('https://gateway.golike.net/api/users/me', headers=headers, impersonate="chrome").json()
    thongtin=[]
    #print(getthongtin)
    if 'status' in getthongtin:
        thongtin.append(getthongtin['data']['id'])
        thongtin.append(getthongtin['data']['name'])
        thongtin.append(getthongtin['data']['coin'])
        return thongtin
        
    else:
        print("lỗi get thông tin")# Trả về None để chỉ ra lỗi
        return None
def X_accout():
    headers = {
        f'authorization':Authorizationgolike,
        f'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
        f't':T,
    }

    Xaccout= requests.get('https://gateway.golike.net/api/twitter-account', headers=headers, impersonate="chrome").json()
    if 'status' in Xaccout:
        ID = [i['id'] for i in Xaccout['data']]
        NAMEX =[i['screen_name'] for i in Xaccout['data']]
        #print(ID)
        #print(NAMEX)
        return ID,NAMEX
    else:
        print('lỗi requests Xaccout')
        return None

'''
def getjop():
    global package_name,object_id,adsid,mess,messcomment,comment_id
    headers = {
        f'authorization':Authorizationgolike,
        f'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
        f't':T,
    }

    params = {
        'account_id': ID,
    }
    #getjopX= requests.get('https://mocki.io/v1/911a4f9f-ed05-4fc7-8e39-72463efa2d9b', params=params, headers=headers,impersonate="chrome").json()
    getjopX = requests.get('https://gateway.golike.net/api/advertising/publishers/twitter/jobs', params=params, headers=headers,impersonate="chrome").json()
    #print(getjopX)
    if 'status' in getjopX and getjopX['status'] == 200:
        package_name=getjopX['data']['package_name']
        #print(package_name,'lllllll')
        if package_name in['like','follow']:
            object_id=getjopX['data']['object_id']
            adsid=getjopX['lock']['ads_id']
            return package_name,object_id,adsid
        elif package_name in ['comment']:
            #print('8888888888888888888')
            object_id=getjopX['data']['object_id']
            messcomment=getjopX['data']['comment_run']['message']
            comment_id=getjopX['lock']['comment_id']
            adsid=getjopX['lock']['ads_id']
            return object_id,messcomment,comment_id,adsid
        else:
            print('loi gẹtp')
            #print(messcomment
        #print(ID)
        #print(NAMEX)
    elif getjopX['status'] == 400:
            #print('ppppppppp')
            mess = getjopX['message'] # Dùng get để tránh lỗi nếu 'message' không tồn tại
            return None
    else:
            mess = getjopX.get('message', f"Unexpected status: {getjopX.get('status', 'unknown')}")
            return None
    '''
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
            sleep(0.12)
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ", end="\r")
'''
def hoanthanh():
    global messhoanthanh
    headers = {
        f'authorization':Authorizationgolike,
        f'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
        f't':T,
    }
    if package_name in ['follow','like']: 
        json_data = {
        'ads_id': adsid,
        'account_id': ID,
        'async': True,
        #'captcha_token': '03AFcWeA73UiZDfMSvb2lpy4xcbo6PDmHGTukzWDZKFDIuKFZwfQWxFTc874Xl0pOm3SapT-aUJ2gsn-ukiALA5Ho5zzuHu772kLXXEpP8XjUEupreu6eD90_sHUoRyKbFCkG8pJebSpNDX2Ca3y1zTHmHbyVSYx0INAuf8ZLXeZW9mn_KZ22nMmwdWIC6PWJUodIdWaXUAuTpvF7_c2OthXcV9jcjfk4aDrrI_F3ZuQ86ZjGytjHC_2BxT4oJI1OugHR6QXSDpofL-WxZNOFKO3zMdt-1ZyO6ujQmifZtaRNdHsXB_Tbkxqow6FQAYR9IRj77jLOZzsfbkpbduJEVV7VhkgiZdpAmCQIhL0BnvGf_id51oIZ5CIiWbH1EYXCwRbPVFg1K9yWr4c-yXEAeo-j6TwGOZwdMurhLjLIuSfWx6CZRQlOXxa3zvqqkPx3qTdLL-r7dRa1RtMTEm6kKyWsbTTdXCuT__bX72T-R8VUBdPNC3OCPR7rdMfYBsjcxPxAs4exzR2u_I9wNX6yxR4g1lw1tUNcovfu5nwj9FNJpN4PnTQJNPiGVHNkA_rOFPFHtI_hUj3BNMp1Pq9uH2SkLoe0H9GIaaLRmm3QMkxytPhTmlG3-3b9vAKUpbAiLDqNhPFEhZXnGnd61-ZuP2LnvCiQ8KX6bO38VI2J9OOezM6HPiwIL7i1bHKIi9Wo0ODDfGbi2YefuYJKo-S8skPwyLPSGceSMPK9SCJDXYj-hM2u1lxR9mnpI5_jv2DAgRLtbLVE2RAmHiup6RbPWBg5XOo6CU0IhnStphCKFQ3CK9gyBAGaQ9_Z7BUkmwqqv1TMHAAbP2vd6prLecjJMD3dljwZIyav6M9wtdPiCXN5RLyz7D0d3GD63SDw4xJm03bV0r9af8G-sTPsoaFZLMSklr6boUNpTTOAVtHCNmWJPwoKWWIn4iagdSa1Q1qyCQK3l_dZ9xRuvLuVs9cbz2X1gkMY0yTVRjvXuPfxia69znc2XFVSLIja6wVtWRoY5jZrM64lfo8sVqNW4ahzhYbrFCyXKqrPFxVc88J5PdikAXCyPz9S0tir8a-edW9k2Ezw5L7_TB9B-',
        #'captcha': 'recaptcha',
        }
        hoanthanh = requests.post(
            'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
            headers=headers,
            json=json_data,
            impersonate="chrome").json()
    elif package_name in ['comment'] :
        json_datacomment = {
        'ads_id': adsid,
        'account_id': ID,
        'async': True,
        #'captcha_token': '03AFcWeA7083t3eCPUk_CtvNCM-Cm1eCdNPY6KXWWGvygMvWBA94fot3S6oqtxul5O4OFSbhAkuKRhMC5kcOgx1_5QpxTnmsMrEhbG6SRPiwzG-qu_LNURtVnnjuOKXMShKv4YvsHTxyWA28gUAcg7MqQqstBheAYUD3OMnhMspsKdRZgOF4LtUvwPz87Ec3rS_aX4zoDYT_cyGYXV_O9eHMuVXlrbuGENqIis3845PibQbmFwBTiozYz2p4bimyNFcCezjP3l2SKD69Gw7eePHTuaAN3OXNvbzkIAqS5jz42cV3ZChZxSEOvo2dfiI2iesmzBPPzTDuQTsF4SQ0K7OrMidoDaKfnapbtfQPiUVMgQohudmW22XtCbZ_clR_48xw5rkU8JA_aqdhxNT2wriF9wjlU9akMLTAdnLJPkKSe3ua_6ClqlpeJ6dy2YE6472I4QUzmGKKR1Hvwv38QE0DbEgIO4O2d7MTq-l1y-OvjePTgnhm9x-YMm72L0P3DGxCb-QWwU475RxrCC6Toz2jZqblJdrzGsHChdHJcd5MpCmVv-xhhvxCVJMUu_8xSq3fHzL0w-z6HOY7i0f0idrMU0RbbhMJ9dfBekqXoeVQ1_xWBT2ug63-QjwXNwh6d9p-pWeLdaVGKDH1yBAE_HwSFRyRjEeeEc9OW5ecKjQKccP-A6Ev3h8vctNZ2Q2y5GF0SjebyH1xyCzneG1on3KowwNESO5J6Xj0nKSA3ttd_ALU-jZtSSPgcMEingC511Ydk9Z9hX3cA5QcrqaeCC9uo0nwAiT-N7yujGuyUaLkbiDUqxd8OOdkWB8N6iM8PgCFkMB43RTmWRMl_2QOGKU1BsjUtvUVv0I4-_jBR3YW0Wn7QAovQBng9PY6w6zcMq-Kb7b_NV7IpdVwsdjvlWmE2j4SvFCNEEbyDXdKhgwtVq1yAFvz7yhMW1ofXVaH6_oNAdFUO0rPlCKIQL-YDTM1ZP3ZfSFvA4tz4TAwP62-RGzVgPC8Tj7elkTgn8eMosGXZZZvbw6d8vGT8fF7sqpVjoPjXYEbUTDg',
        #'captcha': 'recaptcha',
        'comment_id': comment_id,
        'message': messcomment,
        }
        hoanthanh = requests.post(
            'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
            headers=headers,
            json=json_datacomment,
            impersonate="chrome").json()
    else:
        print('lpoi hoanthanh')
    if 'status' in hoanthanh:
        messhoanthanh=hoanthanh['message']
    else:
         print('lỗi hoan thanh')
'''
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
def start():
   
    global authorizationx,cookie,xcsrftoken,Authorizationgolike,T,ID,NAMEX
    banner()
    Authorizationgolike = input('Nhập Authorization golike:')
    T =input('Nhập T golike:')
    authorizationx=input('Nhập authorization X:')
    cookie=input('Nhập cookie X:')
    xcsrftoken=cookie.split('ct0=')[1].split(';')[0]
    os.system('cls')
    banner()
    thongtintaikhoan = getthongtin()
    print(f'-------------------------------------------------------------------------------------')
    print(f'✨TÊN TÀI KHOẢN:{thongtintaikhoan[1]} ')
    print(f'✨TỔNG TIỀN:{thongtintaikhoan[2]} VNĐ')
    print(f'✨ID TÀI KHOẢN:{thongtintaikhoan[0]} ')
    print(f'-------------------------------------------------------------------------------------')
    ID=X_accout()[0]
    NAMEX=X_accout()[1]
    for i in range(len(ID)):
        print(f'{vang}✨---------------------------------------✨')
        print(f'🌟{tim}{i}  |  {ID[i]} |   {NAMEX[i]}         ')
        print(f'{vang}✨---------------------------------------✨')
    chontaikhoanX=int(input('CHỌN TÀI KHOẢN MUỐN CHẠY : '))
    ID=ID[chontaikhoanX]
    solanchay=int(input('NHẬP SỐ LẦN CHẠY:'))
    time_sec = int(input('Nhaapj  Thowif Gian Dellay Jop:'))
    dem = 0  # Đếm số job đã hoàn thành cho cookie hiện tại
    tong = 0 
    for chay in range(1,solanchay+1):
        headersgl = {
            f'authorization':Authorizationgolike,
            f'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
            f't':T,
        }

        params = {
            'account_id': ID,
        }
        #getjopX= requests.get('https://mocki.io/v1/911a4f9f-ed05-4fc7-8e39-72463efa2d9b', params=params, headers=headers,impersonate="chrome").json()
        getjopX = requests.get('https://gateway.golike.net/api/advertising/publishers/twitter/jobs', params=params, headers=headersgl,impersonate="chrome").json()
        if 'status' in getjopX and getjopX['status'] == 200:
            package_name=getjopX['data']['package_name']

        #print(getjopX
            try:
                #print(adsid)
                if package_name in ['like']:
                    package_name=getjopX['data']['package_name']
                    object_id=getjopX['data']['object_id']
                    adsid=getjopX['lock']['ads_id']

                    print(package_name)
                    headers = {
                        'accept': '*/*',
                        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                        'authorization': authorizationx,
                        'content-type': 'application/json',
                        'origin': 'https://x.com',
                        'priority': 'u=1, i',
                        'referer': 'https://x.com/huuduong2000/status/1918710974837624896',
                        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                        'sec-ch-ua-arch': '"x86"',
                        'sec-ch-ua-bitness': '"64"',
                        'sec-ch-ua-full-version': '"135.0.7049.115"',
                        'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.115", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.115"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-model': '""',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"10.0.0"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
                        'x-client-transaction-id': 'Cx92uBpTjiU+FU/KmH71SzTznwer5RzTOxVNROjKqOXh0KnGbzfNSbFR/4JpAhIYYwiazAiJk6yZi1NlPacyL7m1Wgf4CA',
                        'x-csrf-token': xcsrftoken,
                        'x-twitter-active-user': 'yes',
                        'x-twitter-auth-type': 'OAuth2Session',
                        'x-twitter-client-language': 'en',
                        'cookie': cookie,
                    }
                    json_data = {
                        'variables': {
                            'tweet_id': object_id,
                        },
                        'queryId': 'lI07N6Otwv1PhnEgXILM7A',
                    }
                    
                    likex = requests.post(
                        'https://x.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet',
                        headers=headers,
                        json=json_data,
                        
                    ).text
                    countdown(time_sec)
                    if '"data"' in likex:
                        json_data = {
                        'ads_id': adsid,
                        'account_id': ID,
                        'async': True,
                        #'captcha_token': '03AFcWeA73UiZDfMSvb2lpy4xcbo6PDmHGTukzWDZKFDIuKFZwfQWxFTc874Xl0pOm3SapT-aUJ2gsn-ukiALA5Ho5zzuHu772kLXXEpP8XjUEupreu6eD90_sHUoRyKbFCkG8pJebSpNDX2Ca3y1zTHmHbyVSYx0INAuf8ZLXeZW9mn_KZ22nMmwdWIC6PWJUodIdWaXUAuTpvF7_c2OthXcV9jcjfk4aDrrI_F3ZuQ86ZjGytjHC_2BxT4oJI1OugHR6QXSDpofL-WxZNOFKO3zMdt-1ZyO6ujQmifZtaRNdHsXB_Tbkxqow6FQAYR9IRj77jLOZzsfbkpbduJEVV7VhkgiZdpAmCQIhL0BnvGf_id51oIZ5CIiWbH1EYXCwRbPVFg1K9yWr4c-yXEAeo-j6TwGOZwdMurhLjLIuSfWx6CZRQlOXxa3zvqqkPx3qTdLL-r7dRa1RtMTEm6kKyWsbTTdXCuT__bX72T-R8VUBdPNC3OCPR7rdMfYBsjcxPxAs4exzR2u_I9wNX6yxR4g1lw1tUNcovfu5nwj9FNJpN4PnTQJNPiGVHNkA_rOFPFHtI_hUj3BNMp1Pq9uH2SkLoe0H9GIaaLRmm3QMkxytPhTmlG3-3b9vAKUpbAiLDqNhPFEhZXnGnd61-ZuP2LnvCiQ8KX6bO38VI2J9OOezM6HPiwIL7i1bHKIi9Wo0ODDfGbi2YefuYJKo-S8skPwyLPSGceSMPK9SCJDXYj-hM2u1lxR9mnpI5_jv2DAgRLtbLVE2RAmHiup6RbPWBg5XOo6CU0IhnStphCKFQ3CK9gyBAGaQ9_Z7BUkmwqqv1TMHAAbP2vd6prLecjJMD3dljwZIyav6M9wtdPiCXN5RLyz7D0d3GD63SDw4xJm03bV0r9af8G-sTPsoaFZLMSklr6boUNpTTOAVtHCNmWJPwoKWWIn4iagdSa1Q1qyCQK3l_dZ9xRuvLuVs9cbz2X1gkMY0yTVRjvXuPfxia69znc2XFVSLIja6wVtWRoY5jZrM64lfo8sVqNW4ahzhYbrFCyXKqrPFxVc88J5PdikAXCyPz9S0tir8a-edW9k2Ezw5L7_TB9B-',
                        #'captcha': 'recaptcha',
                        }
                        hoanthanh = requests.post(
                            'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                            headers=headersgl,
                            json=json_data,
                            impersonate="chrome").json()
                        dem += 1
                        local_time = time.localtime()
                        h, m, s = [f"{t:02d}" for t in (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)]
                        prices = hoanthanh['data']['prices']
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
                        'ads_id': adsid,
                        'account_id': ID,
                        'object_id': object_id,
                        }
                        boqua = requests.post(
                            'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs',
                            headers=headersgl,
                            json=json_data,
                            impersonate="chrome"
                        ).json()
            
                    
                    
                elif package_name in ['follow']:
                    package_name=getjopX['data']['package_name']
                    object_id=getjopX['data']['object_id']
                    adsid=getjopX['lock']['ads_id']
                    print(package_name)
                    headers = {
                        'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.115", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.115"',
                        'sec-ch-ua-platform': '"Windows"',
                        'authorization': authorizationx,
                        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                        'sec-ch-ua-bitness': '"64"',
                        'sec-ch-ua-model': '""',
                        'sec-ch-ua-mobile': '?0',
                        'x-twitter-active-user': 'yes',
                        'sec-ch-ua-arch': '"x86"',
                        'sec-ch-ua-full-version': '"135.0.7049.115"',
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-csrf-token': xcsrftoken,
                        'Referer': 'https://x.com/CharlesCamilleS',
                        'x-twitter-client-language': 'en',
                        #'x-client-transaction-id': '63U9IdhdvRxJH3P6WR1m6XU445U3EkuIGJH/OHe9pZyP7HYM9dcWqL6ET2VL0f7hMh9iLOi2tNypiMVD8X6QAOEJvZel6A',
                        'x-twitter-auth-type': 'OAuth2Session',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
                        'sec-ch-ua-platform-version': '"10.0.0"',
                        'cookie': cookie

                    }

                    data = {
                            'include_profile_interstitial_type': '1',
                            'include_blocking': '1',
                            'include_blocked_by': '1',
                            'include_followed_by': '1',
                            'include_want_retweets': '1',
                            'include_mute_edge': '1',
                            'include_can_dm': '1',
                            'include_can_media_tag': '1',
                            'include_ext_is_blue_verified': '1',
                            'include_ext_verified_type': '1',
                            'include_ext_profile_image_shape': '1',
                            'skip_status': '1',
                            'user_id': object_id,
                        }
                    follow = requests.post('https://x.com/i/api/1.1/friendships/create.json', headers=headers, data=data).text
                    countdown(time_sec)
                    if '"following":false' in follow or '"following":true' in follow:
                        json_data = {
                        'ads_id': adsid,
                        'account_id': ID,
                        'async': True,
                        #'captcha_token': '03AFcWeA73UiZDfMSvb2lpy4xcbo6PDmHGTukzWDZKFDIuKFZwfQWxFTc874Xl0pOm3SapT-aUJ2gsn-ukiALA5Ho5zzuHu772kLXXEpP8XjUEupreu6eD90_sHUoRyKbFCkG8pJebSpNDX2Ca3y1zTHmHbyVSYx0INAuf8ZLXeZW9mn_KZ22nMmwdWIC6PWJUodIdWaXUAuTpvF7_c2OthXcV9jcjfk4aDrrI_F3ZuQ86ZjGytjHC_2BxT4oJI1OugHR6QXSDpofL-WxZNOFKO3zMdt-1ZyO6ujQmifZtaRNdHsXB_Tbkxqow6FQAYR9IRj77jLOZzsfbkpbduJEVV7VhkgiZdpAmCQIhL0BnvGf_id51oIZ5CIiWbH1EYXCwRbPVFg1K9yWr4c-yXEAeo-j6TwGOZwdMurhLjLIuSfWx6CZRQlOXxa3zvqqkPx3qTdLL-r7dRa1RtMTEm6kKyWsbTTdXCuT__bX72T-R8VUBdPNC3OCPR7rdMfYBsjcxPxAs4exzR2u_I9wNX6yxR4g1lw1tUNcovfu5nwj9FNJpN4PnTQJNPiGVHNkA_rOFPFHtI_hUj3BNMp1Pq9uH2SkLoe0H9GIaaLRmm3QMkxytPhTmlG3-3b9vAKUpbAiLDqNhPFEhZXnGnd61-ZuP2LnvCiQ8KX6bO38VI2J9OOezM6HPiwIL7i1bHKIi9Wo0ODDfGbi2YefuYJKo-S8skPwyLPSGceSMPK9SCJDXYj-hM2u1lxR9mnpI5_jv2DAgRLtbLVE2RAmHiup6RbPWBg5XOo6CU0IhnStphCKFQ3CK9gyBAGaQ9_Z7BUkmwqqv1TMHAAbP2vd6prLecjJMD3dljwZIyav6M9wtdPiCXN5RLyz7D0d3GD63SDw4xJm03bV0r9af8G-sTPsoaFZLMSklr6boUNpTTOAVtHCNmWJPwoKWWIn4iagdSa1Q1qyCQK3l_dZ9xRuvLuVs9cbz2X1gkMY0yTVRjvXuPfxia69znc2XFVSLIja6wVtWRoY5jZrM64lfo8sVqNW4ahzhYbrFCyXKqrPFxVc88J5PdikAXCyPz9S0tir8a-edW9k2Ezw5L7_TB9B-',
                        #'captcha': 'recaptcha',
                        }
                        hoanthanh = requests.post(
                            'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                            headers=headersgl,
                            json=json_data,
                            impersonate="chrome").json()
                        dem += 1
                        local_time = time.localtime()
                        h, m, s = [f"{t:02d}" for t in (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)]
                        prices = hoanthanh['data']['prices']
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
                        'ads_id': adsid,
                        'account_id': ID,
                        'object_id': object_id,
                        }
                        boqua = requests.post(
                            'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs',
                            headers=headersgl,
                            json=json_data,
                            impersonate="chrome"
                        ).json()
                        print(boqua)
                elif package_name in ['comment']:
                    object_id=getjopX['data']['object_id']
                    messcomment=getjopX['data']['comment_run']['message']
                    comment_id=getjopX['lock']['comment_id']
                    adsid=getjopX['lock']['ads_id']
                    print(package_name)
                    print(messcomment)
                    headers = {
                            'accept': '*/*',
                            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'authorization': authorizationx,
                            'content-type': 'application/json',
                            'origin': 'https://x.com',
                            'priority': 'u=1, i',
                            'referer': 'https://x.com/compose/post',
                            'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                            'sec-ch-ua-arch': '"x86"',
                            'sec-ch-ua-bitness': '"64"',
                            'sec-ch-ua-full-version': '"135.0.7049.115"',
                            'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.115", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.115"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-model': '""',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-ch-ua-platform-version': '"10.0.0"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
                            'x-client-transaction-id': '18OqZMaPUvniyZMWRKIpl+gvQ9t3OcAP58mRmDQWdDk9DHUas+sRlW2NI1613s7Ev/paENQN/0dyeHfqGJnthaB59KXM1A',
                            'x-csrf-token': xcsrftoken,
                            'x-twitter-active-user': 'yes',
                            'x-twitter-auth-type': 'OAuth2Session',
                            'x-twitter-client-language': 'en',
                            'cookie': cookie,
                        }

                    json_data = {
                        'variables': {
                            'tweet_text':messcomment,
                            'reply': {
                                'in_reply_to_tweet_id':object_id,
                                'exclude_reply_user_ids': [],
                            },
                            'dark_request': False,
                            'media': {
                                'media_entities': [],
                                'possibly_sensitive': False,
                            },
                            'semantic_annotation_ids': [],
                            'disallowed_reply_options': None,
                            'engagement_request': {
                                'impression_id': 'abb4929a7d4f9a8',
                            },
                        },
                        'features': {
                            'premium_content_api_read_enabled': False,
                            'communities_web_enable_tweet_community_results_fetch': True,
                            'c9s_tweet_anatomy_moderator_badge_enabled': True,
                            'responsive_web_grok_analyze_button_fetch_trends_enabled': False,
                            'responsive_web_grok_analyze_post_followups_enabled': True,
                            'responsive_web_jetfuel_frame': False,
                            'responsive_web_grok_share_attachment_enabled': True,
                            'responsive_web_edit_tweet_api_enabled': True,
                            'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
                            'view_counts_everywhere_api_enabled': True,
                            'longform_notetweets_consumption_enabled': True,
                            'responsive_web_twitter_article_tweet_consumption_enabled': True,
                            'tweet_awards_web_tipping_enabled': False,
                            'responsive_web_grok_show_grok_translated_post': False,
                            'responsive_web_grok_analysis_button_from_backend': True,
                            'creator_subscriptions_quote_tweet_preview_enabled': False,
                            'longform_notetweets_rich_text_read_enabled': True,
                            'longform_notetweets_inline_media_enabled': True,
                            'profile_label_improvements_pcf_label_in_post_enabled': True,
                            'rweb_tipjar_consumption_enabled': True,
                            'verified_phone_label_enabled': False,
                            'articles_preview_enabled': True,
                            'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
                            'freedom_of_speech_not_reach_fetch_enabled': True,
                            'standardized_nudges_misinfo': True,
                            'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': True,
                            'responsive_web_grok_image_annotation_enabled': True,
                            'responsive_web_graphql_timeline_navigation_enabled': True,
                            'responsive_web_enhance_cards_enabled': False,
                        },
                        'queryId': 'IID9x6WsdMnTlXnzXGq8ng',
                    }
                    
                    commentx = requests.post('https://x.com/i/api/graphql/IID9x6WsdMnTlXnzXGq8ng/CreateTweet', headers=headers, json=json_data).text
                    countdown(time_sec)
                    if 'data' in commentx:
                        json_datacomment = {
                        'ads_id': adsid,
                        'account_id': ID,
                        'async': True,
                        #'captcha_token': '03AFcWeA7083t3eCPUk_CtvNCM-Cm1eCdNPY6KXWWGvygMvWBA94fot3S6oqtxul5O4OFSbhAkuKRhMC5kcOgx1_5QpxTnmsMrEhbG6SRPiwzG-qu_LNURtVnnjuOKXMShKv4YvsHTxyWA28gUAcg7MqQqstBheAYUD3OMnhMspsKdRZgOF4LtUvwPz87Ec3rS_aX4zoDYT_cyGYXV_O9eHMuVXlrbuGENqIis3845PibQbmFwBTiozYz2p4bimyNFcCezjP3l2SKD69Gw7eePHTuaAN3OXNvbzkIAqS5jz42cV3ZChZxSEOvo2dfiI2iesmzBPPzTDuQTsF4SQ0K7OrMidoDaKfnapbtfQPiUVMgQohudmW22XtCbZ_clR_48xw5rkU8JA_aqdhxNT2wriF9wjlU9akMLTAdnLJPkKSe3ua_6ClqlpeJ6dy2YE6472I4QUzmGKKR1Hvwv38QE0DbEgIO4O2d7MTq-l1y-OvjePTgnhm9x-YMm72L0P3DGxCb-QWwU475RxrCC6Toz2jZqblJdrzGsHChdHJcd5MpCmVv-xhhvxCVJMUu_8xSq3fHzL0w-z6HOY7i0f0idrMU0RbbhMJ9dfBekqXoeVQ1_xWBT2ug63-QjwXNwh6d9p-pWeLdaVGKDH1yBAE_HwSFRyRjEeeEc9OW5ecKjQKccP-A6Ev3h8vctNZ2Q2y5GF0SjebyH1xyCzneG1on3KowwNESO5J6Xj0nKSA3ttd_ALU-jZtSSPgcMEingC511Ydk9Z9hX3cA5QcrqaeCC9uo0nwAiT-N7yujGuyUaLkbiDUqxd8OOdkWB8N6iM8PgCFkMB43RTmWRMl_2QOGKU1BsjUtvUVv0I4-_jBR3YW0Wn7QAovQBng9PY6w6zcMq-Kb7b_NV7IpdVwsdjvlWmE2j4SvFCNEEbyDXdKhgwtVq1yAFvz7yhMW1ofXVaH6_oNAdFUO0rPlCKIQL-YDTM1ZP3ZfSFvA4tz4TAwP62-RGzVgPC8Tj7elkTgn8eMosGXZZZvbw6d8vGT8fF7sqpVjoPjXYEbUTDg',
                        #'captcha': 'recaptcha',
                        'comment_id': comment_id,
                        'message': messcomment,
                        }
                        hoanthanh = requests.post(
                            'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                            headers=headersgl,
                            json=json_datacomment,
                            impersonate="chrome").json()
                        dem += 1
                        local_time = time.localtime()
                        h, m, s = [f"{t:02d}" for t in (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)]
                        prices = hoanthanh['data']['prices']
                        tong += prices
                        chuoi = (
                            f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                            f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m  | "
                            f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                            f"\033[1;31mcomment\033[1;31m\033[1;32m\033[1;97m | "
                            f"\033[1;32mẨn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                            f"\033[1;33m{tong} vnđ"
                        )
                        print(chuoi)

                    else:
                        json_data = {
                        'ads_id': adsid,
                        'account_id': ID,
                        'object_id': object_id,
                        }
                        boqua = requests.post(
                            'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs',
                            headers=headersgl,
                            json=json_data,
                            impersonate="chrome"
                        ).json()
            except:
                json_data = {
                    'ads_id': adsid,
                    'account_id': ID,
                    'object_id': object_id,
                    }
                boqua = requests.post(
                        'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs',
                        headers=headersgl,
                        json=json_data,
                        impersonate="chrome"
                ).json()



            #print(f'{chay} |{object_id}|ads:{adsid}| {messhoanthanh} |{trangthai}')
            #print(f'{chay} |{object_id}|ads:{adsid}| {messhoanthanh} |')
            #sleep(5)

                #print(package_name)
             # Thoát vòng lặp nếu thành công
        else:
            print(getjopX['message'])
            countdown(10)

            
start()
    

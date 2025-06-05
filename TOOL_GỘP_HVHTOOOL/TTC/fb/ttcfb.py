import json
from curl_cffi import requests
import uuid
import os
from time import sleep
from datetime import datetime
from datetime import date
class TTCFB(object):
    def __init__(self, token):
        self.token = token

    def get_cookie_ttc(self):
        data = {
            'access_token': self.token
        }
        text_1 = requests.post("https://tuongtaccheo.com/logintoken.php", data= data)
        log = text_1.json()["status"]
        if log == "success" :
            xu = text_1.json()["data"]["sodu"]
            name = text_1.json()["data"]["user"]
            cookie = text_1.headers["Set-Cookie"]
            
        else :
            print (' \033[1;31m Đăng Nhập Thất Bại ')
            exit()
        return cookie

# ✅ Khởi tạo và sử dụng đúng cách
token = '6f8c066c8a8028731755d05c9bf0c0af'
i = TTCFB(token)
cookie = i.get_cookie_ttc()
print("Cookie:", cookie)
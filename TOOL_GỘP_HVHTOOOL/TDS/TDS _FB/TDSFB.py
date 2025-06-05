import os, json, sys
from sys import platform
from time import sleep
import urllib.parse
from curl_cffi import requests
from datetime import datetime
from random import randint
from pystyle import Colors, Colorate
import uuid, re
from bs4 import BeautifulSoup
def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f"""
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;97m☞ \033[1;31mTDS - Facebook\033[1;33m♔ \033[1;97m🔫
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
class Facebook_Api (object):
	def __init__(self, cookie):
		self.cookie = cookie
		self.user_id = cookie.split('c_user=')[1].split(';')[0]
		self.headers = {'authority': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-language': 'en-US,en;q=0.9','cookie': cookie}
	def get_thongtin(self):
		try:
			url = 'https://www.facebook.com/'
			response = requests.get(url, headers=self.headers, timeout=10, allow_redirects=True)
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
			self.fb_dtsg = fb_dtsg_match.group(1) if fb_dtsg_match else None
			if not self.fb_dtsg:
				raise ValueError("Could not find fb_dtsg in the response")
			# Extract jazoest
			jazoest_match = re.search(r'<input type="hidden" name="jazoest" value="(.*?)"', home)
			if not jazoest_match:
				jazoest_match = re.search(r'"name":"jazoest","value":"(.*?)"', home)
			self.jazoest = jazoest_match.group(1) if jazoest_match else None
			if not self.jazoest:
				raise ValueError("Could not find jazoest in the response")
			# Extract name (ten)
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
			#print(f"Tên: {ten}, User ID: {self.user_id}, fb_dtsg: {self.fb_dtsg}, jazoest: {self.jazoest}")
			return ten, self.user_id

		except Exception as e:
			#print(f"Error in get_thongtin: {str(e)}")
			return 1
    
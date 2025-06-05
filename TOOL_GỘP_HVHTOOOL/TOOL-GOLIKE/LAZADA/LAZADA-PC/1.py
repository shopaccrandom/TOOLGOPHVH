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

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3NDc1NzAyMDMsImV4cCI6MTc3OTEwNjIwMywibmJmIjoxNzQ3NTcwMjAzLCJqdGkiOiI2dzBRODk2WlVKcHVEc3A5Iiwic3ViIjoyNDAwNzQzLCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.ovWSoa-ac6qpPIfw1B5kvFnF0K4ZHgOAa5xllRKwIFg',
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'Accept': 'application/json, text/plain, */*',
    't': 'VFZSak1FNTZaM2hOVkVWNFQxRTlQUT09',
    'Content-Type': 'application/json;charset=UTF-8',
}

json_data = {
    'ads_id': 3780,
    'account_id': 29089,
    'async': True,
    'data': None,
    #'captcha_token': '03AFcWeA6acCZJPFQa2fgfuJc8WB88GtF_vFsWIrHT7LHny4ZDQpaVWca0P7d8NuEgzNJKvoNlzns3obO-cSiJ2e8p2_6oH6Xrq4Y9ts2u6Vgnuj3wXEkseW4EPjkpIW_ljPwL3nLP7QK2KYpP65nbG7vIE-ZITabeYcbBPxtdMo-C5GFF4G10RlGdfDWD-tVQP9LpHW1R-yhLGrQhWKhSGJ2UjYFMFmfgvSHFoj5sAYSptJgEKX2yCScMi8FrRRjuCAkpmzk3gFmx6hre7Z1ZvlJb8P0F4cRxr3G7OAjqQDlsv7ZY3Wk2zFcXcWC7VrxhdFiNYf2hVLRsUjFhlICiAXLc3uPR6yDXHr_O8-xBML44pZhkUDTaerjgaC4nZ-wDepxqu3pPwKvZXw_M5254pao0XhKMMasNd_jkEwPvEKI7xkk3Tmm8szC66qxz5-YKjD1zq6Q9aGLjwA8WJ6sStn2xA6Ln0AR-uubc5hTe9RmgOnM0K9w1lGh0BemDOaBNTwPtSYHtP4xeFx5kOtNtrviu5TlAjwC8LWl2n6WzO--r2inOveHkmbcUReDZVqTE5FL700kdrfwm4FaAmXoZlSWWkqJnR1qjlwBKBsfVvShWamAqIr5kz80irmrMIZd16wVFK4vaqCkI3QXWHpjJSLVW6IeRkKU3GEOsjhDu85ZYt5XPNFvIA97G4iZpuhFU7W8tECGWWbHaOvUyByqJyptRtrUgZNTbTP45PgDy8N9h2lAt_Gpr-_rVy9X26nRnhPGeNQRL7q9Dzi0dV8JspHv6-ekr-VahCDlbMDJaGXY4VmzodX9h19SYvqASMg1srfbCD1cl3-mnCfoNdDJN8HRlp24TCW1O2fyT1vGJFtOyqrI-ghSbyen6ZdSU2dxAmzvjtogEakg_MuaAMR0617H9hR4jlsSmW7I6cHC9eBv3ylel9BvFwOuexOZxFiB7LQG19EVE91e1UUafYTGDBsf97pjCV_VlRo5nUFY0IoC2LbrO51eLbgIKzgzMFn0NeZMEkIpP_Ebm',
    #'captcha': 'recaptcha',
}
response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/lazada/complete-jobs',
    headers=headers,
    json=json_data,
    impersonate="chrome"
).json()
print(response)

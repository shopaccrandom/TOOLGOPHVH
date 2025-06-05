import requests
import re
import urllib.parse

# Thay bằng access_token và cookie của bạn

access_token = "EAAGNO4a7r2wBOZCW0xxUZAvd8TbyyDi8Ws46jfcit1t3chfs1B7ehmrgwTDCSzO5rg4N6bxl4z6ZC2OvwNfzd7tDGjZAzuZCUHZAO4spTrsRX5jZCLU9eh18vL7Akuhjt62EKnbKCl2IHPBvlCCxdqSlbutRLBgpxWIWYtlxAyPs3DoyraWsaTrBKtgGkVdB9UIBOXilSCrZAAZDZD"  # Lấy từ Graph API Explorer
cookie = 'sb=2poEaP9VgWHxUwYVRwIqE2sa;c_user=61552599511401;datr=ChsoaKJ2ZqEVoA8_7kg0hJ2V;ps_l=1;ps_n=1;dpr=1.25;xs=11%3AHslbfj41-wpePg%3A2%3A1747458694%3A-1%3A6287%3A%3AAcU4_C5AmF9RYbQkr9Iiz_lTBaczOS-9c-UVeh4FsFA;fr=1d9FqBWCMvLqo8q60.AWes6h6dAUyVidn2ZAkO25_O9Dd9rGrXpuvUYLHcCRqVwlaD6VU.BoLCn0..AAA.0.0.BoLCpn.AWe_-WTjn7NvV2NCC60aW4mvQ5A;ar_debug=1;presence=EDvF3EtimeF1747725049EuserFA261552599511401A2EstateFDutF0CEchF_7bCC;wd=1152x919;'

result = {}

# Thử với Graph API (dùng code bạn cung cấp)
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
        user_id = api_data.get("id", "Không tìm thấy ID")
        user_name = api_data.get("name", "Không tìm thấy tên")
        print(f"id: {user_id}")
        print(f"name: {user_name}")
except requests.RequestException as e:
    result["api_error"] = f"Lỗi khi gửi yêu cầu API: {str(e)}"
except Exception as e:
    result["api_error"] = f"Lỗi API: {str(e)}"

# In lỗi nếu API thất bại


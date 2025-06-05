import requests
import time

# Thông tin cần thiết
access_token = input("NHẬP ACCESS_TOKEN: ")  # Token người dùng
cookie = input("NHẬP COOKIE: ")              # Cookie từ trình duyệt
comment_id = input("NHẬP ID BÌNH LUẬN: ")    
time_sec=int(input('Nhập delay:'))# ID bình luận muốn thích
api_version = "v22.0"

# Headers chứa cookie
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}
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
# Hàm lấy danh sách token của tất cả các Trang
def get_page_tokens():
    url = f"https://graph.facebook.com/{api_version}/me/accounts"
    params = {"access_token": access_token}
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        pages = data.get("data", [])
        if not pages:
            print("Không tìm thấy Trang nào.")
            return []
        print(f"Tìm thấy {len(pages)} Trang.")
        return [{"page_name": page["name"], "access_token": page["access_token"]} for page in pages]
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi lấy danh sách Trang: {e}")
        print(f"Phản hồi: {response.text}")
        return []

# Hàm thích bình luận bằng token của Trang
def like_comment_with_page(page_access_token, page_name):
    url = f"https://graph.facebook.com/{api_version}/{comment_id}/likes?access_token={page_access_token}"
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Thích bình luận {comment_id} thành công bằng Trang '{page_name}'!")
            return True
        else:
            print(f"Thích bình luận {comment_id} thất bại bằng Trang '{page_name}': {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi thích bình luận bằng Trang '{page_name}': {e}")
        print(f"Phản hồi: {response.text}")
        return False

# Thực thi chính
if __name__ == "__main__":
    pages = get_page_tokens()
    if pages:
        # Hiển thị danh sách các Trang
        print("Danh sách các Trang:")
        for i, page in enumerate(pages, start=1):
            print(f"[{i}]|{page['page_name']}")
        
        # Tiếp tục với hành động thích bình luận
        successful_likes = 0
        for page in pages:
            countdown(time_sec)
            print(f"Đang xử lý Trang: {page['page_name']}")
            if like_comment_with_page(page["access_token"], page["page_name"]):
                successful_likes += 1
            time.sleep(2)  # Độ trễ 2 giây để tránh giới hạn API
        print(f"Hoàn tất! Đã thích bình luận {comment_id} bằng {successful_likes}/{len(pages)} Trang.")
    else:
        print("Không có Trang nào để thực hiện hành động.")
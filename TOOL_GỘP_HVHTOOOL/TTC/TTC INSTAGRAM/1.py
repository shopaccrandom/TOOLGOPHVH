import random

# Danh sách các phiên bản hệ điều hành và model để tạo User-Agent
ios_versions = ["14_0", "14_1", "15_0", "15_1", "16_0", "16_1", "17_0"]
android_versions = ["10", "11", "12", "13"]
android_models = [
    "SM-G998B",  # Samsung Galaxy S21 Ultra
    "SM-S918B",  # Samsung Galaxy S23 Ultra
    "Pixel 6",   # Google Pixel 6
    "Pixel 7",   # Google Pixel 7
    "LYA-L29",   # Huawei P30 Pro
    "Mi 11",     # Xiaomi Mi 11
    "OnePlus 9", # OnePlus 9
    "Xperia 1 III", # Sony Xperia 1 III
    "Moto G100", # Motorola Moto G100
    "Nokia X20"  # Nokia X20
]
windows_versions = ["10.0", "11.0"]
macos_versions = ["10_15_7", "11_0", "12_0"]
linux_distros = ["Ubuntu", "Fedora", "Debian", "Arch Linux"]
chrome_versions = ["99.0.4844.73", "100.0.4896.58", "101.0.4951.41", "102.0.5005.63", "103.0.5060.53"]
firefox_versions = ["98.0", "99.0", "100.0", "101.0"]

# Các mẫu User-Agent cho từng loại thiết bị
iphone_template = "Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Mobile/15E148 Safari/604.1"
android_template = "Mozilla/5.0 (Linux; Android {android_version}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36"
windows_template = "Mozilla/5.0 (Windows NT {windows_version}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"
macos_template = "Mozilla/5.0 (Macintosh; Intel Mac OS X {macos_version}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"
linux_template = "Mozilla/5.0 (X11; {linux_distro}; Linux x86_64; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}"

# Tạo danh sách User-Agent
user_agents = []

# Tạo 50 User-Agent cho iPhone
for _ in range(50):
    ios_version = random.choice(ios_versions)
    version = ios_version.replace('_', '.')  # Chuyển 16_0 thành 16.0
    ua = iphone_template.format(ios_version=ios_version, version=version)
    user_agents.append(ua)

# Tạo 200 User-Agent cho Android
for _ in range(200):
    android_version = random.choice(android_versions)
    model = random.choice(android_models)
    chrome_version = random.choice(chrome_versions)
    ua = android_template.format(android_version=android_version, model=model, chrome_version=chrome_version)
    user_agents.append(ua)

# Tạo 100 User-Agent cho Windows
for _ in range(100):
    windows_version = random.choice(windows_versions)
    chrome_version = random.choice(chrome_versions)
    ua = windows_template.format(windows_version=windows_version, chrome_version=chrome_version)
    user_agents.append(ua)

# Tạo 100 User-Agent cho macOS
for _ in range(100):
    macos_version = random.choice(macos_versions)
    chrome_version = random.choice(chrome_versions)
    ua = macos_template.format(macos_version=macos_version, chrome_version=chrome_version)
    user_agents.append(ua)

# Tạo 50 User-Agent cho Linux
for _ in range(50):
    linux_distro = random.choice(linux_distros)
    firefox_version = random.choice(firefox_versions)
    ua = linux_template.format(linux_distro=linux_distro, firefox_version=firefox_version)
    user_agents.append(ua)

# Đảm bảo ít nhất 500 User-Agent bằng cách thêm ngẫu nhiên nếu thiếu
while len(user_agents) < 500:
    category = random.choice(["iphone", "android", "windows", "macos", "linux"])
    if category == "iphone":
        ios_version = random.choice(ios_versions)
        version = ios_version.replace('_', '.')
        ua = iphone_template.format(ios_version=ios_version, version=version)
    elif category == "android":
        android_version = random.choice(android_versions)
        model = random.choice(android_models)
        chrome_version = random.choice(chrome_versions)
        ua = android_template.format(android_version=android_version, model=model, chrome_version=chrome_version)
    elif category == "windows":
        windows_version = random.choice(windows_versions)
        chrome_version = random.choice(chrome_versions)
        ua = windows_template.format(windows_version=windows_version, chrome_version=chrome_version)
    elif category == "macos":
        macos_version = random.choice(macos_versions)
        chrome_version = random.choice(chrome_versions)
        ua = macos_template.format(macos_version=macos_version, chrome_version=chrome_version)
    else:  # linux
        linux_distro = random.choice(linux_distros)
        firefox_version = random.choice(firefox_versions)
        ua = linux_template.format(linux_distro=linux_distro, firefox_version=firefox_version)
    user_agents.append(ua)

# Loại bỏ trùng lặp (nếu có)
user_agents = list(set(user_agents))

# Chọn 500 User-Agent
user_agents = user_agents[:500]

# Lưu vào tệp theo định dạng yêu cầu
with open("user_agents.py", "w") as f:
    f.write("User_Agent=random.choice([\n")
    for ua in user_agents:
        f.write(f'    "{ua}",\n')
    f.write("])\n")
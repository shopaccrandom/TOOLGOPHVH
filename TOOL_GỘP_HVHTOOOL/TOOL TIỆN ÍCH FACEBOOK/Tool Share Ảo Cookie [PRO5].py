from time import sleep
import requests,threading,os,sys
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
def clear():
    if(sys.platform.startswith('win')):
        os.system('cls')
    else:
        os.system('clear')
def banner():
    print(f''' 

{tim}                                     ¶¶           
{hong}                                ¶1¶1111111¶       
{vang}        ¶¶111¶               ¶¶¶¶111111111¶¶¶1    
{xam}     ¶1¶¶¶¶¶111111¶         ¶¶¶1¶¶¶11111111¶1¶¶   
{xanhbienda}   ¶¶¶1¶1111111111¶¶1      ¶¶1¶¶¶1111111111111¶¶  
{cam}  ¶¶1¶¶1111111111111¶¶     ¶¶¶1¶¶¶¶1111111111111¶ 
{lam}  ¶¶ ¶1111111111111111¶¶   ¶¶¶¶¶¶11¶111111111111¶ 
{lamd} 11 ¶11111111111111111¶¶     ¶¶¶¶  ¶111111111111¶¶
{vangnhat}¶¶¶¶1111111111111111¶¶¶¶     1¶¶  11111111111111¶¶
{xanhlacay}¶¶¶¶11111111111¶¶¶¶¶¶¶      1¶1¶¶1111111111111111¶
{hongdam}¶¶1¶1111111111111¶¶¶¶¶¶     ¶¶¶¶¶¶11111111111111¶¶
{cam}¶¶11111111111111111111111¶¶   ¶¶¶¶¶¶1111111111¶¶¶ 
{tim} 1¶111111111111111111¶¶¶¶¶¶    ¶¶¶¶11111111111¶1  
{red}  ¶¶11111111111111111¶¶¶     ¶¶¶1111111111111¶1   
{trang}   ¶¶¶111111111111¶1¶¶¶    1¶¶111¶1111111¶11¶1    
{nau}    1¶¶¶11111111111¶¶¶¶111¶¶¶¶111111111¶11¶¶¶     
{purple}      ¶¶¶¶1111111111111¶¶¶¶1¶¶¶¶¶¶¶¶11¶11¶¶       
{luc}       ¶¶¶¶¶11111111111¶111¶   ¶¶¶111¶1¶¶¶        
{vang}         ¶¶¶¶¶¶111111111111¶  ¶¶¶111¶¶¶1          
{xam}            1¶¶¶¶¶11111111¶¶ ¶¶¶¶111¶¶            
{xanhbienda}              ¶¶¶¶¶¶¶1111111 ¶¶¶11¶¶1             
{tim}                 1¶¶¶¶¶¶1111¶¶¶1¶¶¶¶              
{xanhbienda}                    ¶¶¶¶¶¶1¶¶¶¶¶1¶                
{xanhlacay}                       ¶1¶¶¶1¶¶¶                  
{xanhngoc}                           11¶       
                        
{tim}                ██╗░░██╗██╗░░░██╗██╗░░██╗
{xanhbienda}                ██║░░██║██║░░░██║██║░░██║
{tim}                ███████║╚██╗░██╔╝███████║
{cam}                ██╔══██║░╚████╔╝░██╔══██║
{xanhlacay}                ██║░░██║░░╚██╔╝░░██║░░██║
{xanhngoc}                ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝             
                            
     ''')
print('')
clear()
banner()

ck_fb=input('\033[1m\033[38;5;51mNhập Cookie Facebook: \033[1;37m')
uid=input('\033[1m\033[38;5;51mNhập ID Bài Viết: \033[1;37m')
token_fb=input('\033[1m\033[38;5;51mNHẬP token facebook: ')

header={
    'cookie': ck_fb,
}
def Start(l):
    getTokenPage = requests.get(f"https://graph.facebook.com/v12.0/me/accounts?fields=access_token&limit=999999999&access_token={token_fb}",headers=header).json()['data']
    print(getTokenPage)
    for tach in getTokenPage:
        uid_page=tach['id']
        access_token_page=tach['access_token']
        buff = requests.post(f"https://graph.facebook.com/me/feed?link=https://www.facebook.com/{uid}&published=0&access_token={access_token_page}",headers=header).text
        if "error" in buff:
            print(f'\033[1m\033[38;5;237m[\033[38;5;54m🛠HVH🛠\033[38;5;237m]\033[0m \033[4m\033[38;5;164m{uid_page}\033[0m \033[1;31mTHẤT BẠI RỒI LÀ ACC DIE HAY GÌ Á RA COI ĐI')
        else:
            print(f'{tim}[ 🛠 HVH 🛠 ] {vangnhat}{buff} {xanhngoc} THÀNH CÔNG ✅')


soluong = int(input('\033[1m\033[38;5;51mNhập Số Lượng: \033[1;37m'))
clear()
banner()
print('')
threades = []
for l in range(soluong):
    threades += [threading.Thread(target=Start,args={l},)]
for t in threades:
    t.start()
for t in threades:
    t.join()
print('\033[1;31mChạy đủ số lượng rồi nhé')
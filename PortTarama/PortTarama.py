import socket
import sys
from queue import Queue
import threading
from datetime import datetime
import os

def clear():

    if os.name == 'nt':
        _ = os.system('cls')
 
    else:
        _ = os.system('clear')
clear()
    
print('''
      
$$$$$$$\                       $$\                                                                      
$$  __$$\                      $$ |                                                                     
$$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\          $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\ 
$$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        $$  _____|$$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$  ____/ $$ /  $$ |$$ |  \__| $$ |          \$$$$$$\  $$ /      $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |      $$ |  $$ |$$ |       $$ |$$\        \____$$\ $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |       
$$ |      \$$$$$$  |$$ |       \$$$$  |      $$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
\__|       \______/ \__|        \____/       \_______/  \_______|\_______|\__|  \__| \_______|\__|
|                                                                                                |
|--------------------------------------------By Sarikaya--------------------------------------|''')

print("\nGithub: https://github.com/Sarikayahsyn\n")


host = socket.gethostbyname(input("Ip/domain Adresi Giriniz: "))

normalPortStart = 1
normalPortEnd = 1024
allPort = 1
allPortEnd = 65535
customPortStart = 0
customPortEnd = 0

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Tarama Seçeneğini girin: ")
print("[+] Numara 1 1/1024 Port Taraması")
print("[+] Numara 2 1/65535 Port Taraması")
print("[+] Özel bağlantı noktası taraması için 3'ü seçin")
print("[+] Programdan Çıkmak için 4 e basın \n")

mode = int(input("[+] Herhangi bir seçeneği belirleyin: "))
print()

if mode == 3:
    customPortStart = int(input("[+] Başlangıç Portunu Girin: "))
    customPortEnd = int(input("[+] Bitiş Portunu Girin: "))

print("-"*50)
print(f"Hedef IP: {host}")
print("Tarama Başladı:" + str(datetime.now()))
print("-"*50)
def scan(port):
    s = socket.socket()
    s.settimeout(5)
    result = s.connect_ex((host, port))
    if result == 0:
       print("Açık port", port)
    s.close()

queue = Queue()
def get_ports(mode):
    if mode == 1:
        print("\n[+] Taranıyor..\n")
        for port in range(normalPortStart, normalPortEnd+1):
            queue.put(port)
    elif mode == 2:
        print("\n[+] Taranıyor..\n")
        for port in range(allPort, allPortEnd+1):
            queue.put(port)
    elif mode == 3:
        print("\n[+] Taranıyor..\n")
        for port in range(customPortStart, customPortEnd+1):
            queue.put(port)
    elif mode == 4:
        print("[-] Çıkış...")
        sys.exit()

open_ports = [] 
def worker():
    while not queue.empty():
        port = queue.get()
        if scan(port):
            print("Port {} Açık!".format(port))
            open_ports.append(port)

def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

run_scanner(1021, mode)
print(f"Tarama Tamamlandı: {current_time}")


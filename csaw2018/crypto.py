import socket
import time
from pwn import *
from string import ascii_lowercase

TCP_IP = 'crypto.chal.csaw.io'
TCP_PORT = 8042
BUFFER_SIZE = 1024*32

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)

pattern = '_WERTYUIOPASDFGHJ'

toSend = ''
#char = ord('a')
#for i in range(26):

for char3 in ascii_lowercase[1:]:
    for char2 in ascii_lowercase:
        for char in ascii_lowercase:
            toSend=char + char2 + char3 + pattern +  '\n'
            s.sendall(toSend)
            data = s.recv(BUFFER_SIZE).strip()
            try:
                data = data[-1]
            except IndexError:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((TCP_IP, TCP_PORT))
                continue
            print (char + char2+char3+" " + str(ord(data)))
           # if ord(data) != 10:
            #    input("AA")

#print (toSend)
#s.sendall(toSend)
#time.sleep(5)

s.close()
'''
QWERTYUIOPASDFGHflag
QWERTYUIOPASDFGHgalf
flagflagflagflagflag
galfgalfgalfgalfgalf
'''
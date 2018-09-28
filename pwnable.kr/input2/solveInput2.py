import os,time,sys
from pwn import *
import socket
# "06c5cec8"

#code = "c9cec506".decode("hex")*4 + "c8cec506".decode("hex")
#print (code + '\n')

#ss = ssh(host="pwnable.kr", user="input2", password="guest", port=2222,timeout=120)

tab = []
target = "/home/input2/input"
#target = "./a.out"
#target = "./input"
tab.append(target)

for i in range(99):
	tab.append(str(i)+' ')
tab[65]='\x00'
tab[66]='\x20\x0a\x0d'
tab[67]="50215"

argv=tab
r,w = os.pipe()
env = {"\xde\xad\xbe\xef":"\xca\xfe\xba\xbe"}

fp = open('\x0a',"w")
fp.write('\x00'*4)
fp.close()

HOST='127.0.0.1'
PORT=int(tab[67])
print str(PORT)

#io=ss.process(argv, stderr=r,env=env)

io=process(argv, stderr=r,env=env)


time.sleep(1)

io.sendline("\x00\x0a\x00\xff")
#sys.stderr.write("\x00\x0a\x02\xff" + '\n')
os.close(r)
os.write(w,"\x00\x0a\x02\xff")

time.sleep(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
s.send("\xde\xad\xbe\xef")
    


io.interactive()



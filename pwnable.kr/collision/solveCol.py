import os,time
from pwn import *
# "06c5cec8"

code = "c9cec506".decode("hex")*4 + "c8cec506".decode("hex")
#print (code + '\n')

r = ssh(host="pwnable.kr", user="col", password="guest", port=2222,timeout=120)

target = "/home/col/col"
argv=[target,code]

io=r.process(argv)
time.sleep(1)


io.interactive()



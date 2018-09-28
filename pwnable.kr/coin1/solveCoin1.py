from pwn import *

r = remote("pwnable.kr",9007)

def prepareLine(a,b):
	line = ''
	while a<=b:
		line+=str(a) + ' '
		a+=1
	return line

def solve():
	params =r.recvline_startswith('N')
	listParams = params.split(' ')
	N = int(listParams[0][2:])
	C = int(listParams[1][2:])
	start=0
	end=N-1
	while(start<=end):
		half = (start+end)/2
		#print "S:"+str(start) + ' ' + "E:"+str(end)
		lineHalf = prepareLine(start,half)
		#print lineHalf
		r.sendline(lineHalf)
		weight = r.recvline()
		#print weight
		if 'C' in weight:
			start=end+1
		else:

			if weight[-2] == '0':
				start=half+1	
			else:
				end = half

	print str(half)
for i in range(100):
	solve()
	print str(i)

r.interactive()

from pwn import *
#I made this AI because I love programming and I got so hyped that I didn't check code wisely.... and this AI didn't worked :( .. but it was SUPER FUN to write it! Real solutiun below code :))
print "PWNBLJ!"

r=remote("pwnable.kr",9009)
r.sendline("Y")
r.sendline("1")
betTime=True
stayed=False
cash=0
while(cash<1000000):
	if betTime:
		cash = int((r.recvline_startswith('Cash')).split('$')[1])
	if not stayed:
		mTotal = int((r.recvline_startswith('Your')).split('is ')[1])
		dTotal = int((r.recvline_startswith('The')).split('of ')[1])
	if betTime:
		r.sendline(str(cash/5))
		betTime=False

	print "$: "+(str(cash))
	print "M: "+(str(mTotal))
	print "D: "+(str(dTotal))

	if mTotal<dTotal:			#need to have more :(
		r.sendline("H")
		print ("H")
	else:
		if mTotal>=17:			#stay if already 17 and more than Dealer
			r.sendline("S")
			stayed=True
			print ("S")	
		else:
			r.sendline("H")		#lets try out this
			print ("H")


	question = r.recvline_startswith('Would')
	print question
	if 'Again' in question:
		r.sendline("Y")
		betTime=True
		stayed=False

r.interactive()

#	CHECH THIS PREVENTION ;)
'''
int betting() //Asks user amount to bet
{
 printf("\n\nEnter Bet: $");
 scanf("%d", &bet);
 
 if (bet > cash) //If player tries to bet more money than player has
 {
        printf("\nYou cannot bet more money than you have.");
        printf("\nEnter Bet: ");
        scanf("%d", &bet);
        return bet;				<=== LMAO XD
 }
 else return bet;
} // End Function
'''
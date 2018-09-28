from pwn import *

print "PWNLOTTO!!!"


'''
No need for program

// calculate lotto score
	int match = 0, j = 0;
	for(i=0; i<6; i++){
		for(j=0; j<6; j++){
			if(lotto[i] == submit[j]){
				match++;
			}
		}
	}


6 same numbers -> win
try smt like '######' (dec must be 1-46) few times and you will win
'''

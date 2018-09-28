from math import floor
def combineLine(a,b,c,d,e,f):
    return '(' + str(a) + ',' + str(b) + '),' + '(' + str(c) + ',' + str(d) + '),' + '(' + str(e) + ',' + str(f) + ')'

def perform2x3(x,y):
    first=combineLine(x,y,x,y+1,x+1,y)
    second=combineLine(x+2,y,x+2,y+1,x+1,y+1)

    #print first
    #print second
    return first+'\n'+second+'\n'

def perform3x2(x,y):
    first=combineLine(x,y,x+1,y,x,y+1)
    second=combineLine(x+1,y+1,x,y+2,x+1,y+2)

    #print first
    #print second
    return first+'\n'+second+'\n'

def perform4x3(x,y):
	solve=''
	solve+=perform3x2(x,y)
	solve+=perform3x2(x+2,y)
	return solve

def determine4x4(x,y):
	cordX=x-x%6
	cordY=y-y%3

	print str(cordX) + ' ' + str(cordY)
	return (cordX,cordY)
	
def determinePosition(x,y):
	fixedX= x%4
	fixedY= y%4
	return (fixedX,fixedY)


def prepareRest(x,y):
	i=0
	j=0
	solve=''
	while(i<y):
		solve+=perform4x3(x,i)
		i+=3
	i+=4
	while(i<=63):
		solve+=perform4x3(x,i)
		i+=3
	return solve

def solve4x4(x,y):
	fixed = determinePosition(x,y)
	fixx=fixed[0]
	fixy=fixed[1]

	corn1=combineLine(x,y,x+1,y,x,y+1)
	corn2=combineLine(x+2,y,x+3,y,x+3,y+1)
	corn3=combineLine(x,y+2,x,y+3,x+1,y+3)
	corn4=combineLine(x+2,y+3,x+3,y+3,x+3,y+2)

	innerCorn1=combineLine(x+1,y+2,x+2,y+2,x+2,y+1)
	innerCorn2=combineLine(x+1,y+1,x+1,y+2,x+2,y+2)
	innerCorn3=combineLine(x+1,y+1,x+2,y+1,x+2,y+2)
	innerCorn4=combineLine(x+1,y+1,x+2,y+1,x+1,y+2)

	print innerCorn1
	print innerCorn2
	print innerCorn3
	print innerCorn4
	


#for i in range(10):
	#a=input(':')
	#b=input(':')
	#cordOf4x4=determine4x4(a,b)

	#solve = prepareRest(cordOf4x4[0],cordOf4x4[1])
	#print solve
solve4x4(0,0)



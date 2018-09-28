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
for j in range(64):
           
    solve=''
    for i in range(20):
        solve+=perform2x3(i*3,j*2)
    for i in range(20):
        solve+=perform2x3(i*3,j*2+2)
    for i in range(20):
        solve+=perform2x3(i*3,j*2+4)

    solve+=perform3x2(60,j*3)
    solve+=perform3x2(60,j*3+3)

    solve+=perform3x2(62,j*3)
    solve+=perform3x2(62,j*3+3)
    #print solve
    f1=open('./solves/' + 'x-'+str(j),'w')
    f1.write(solve)
    f1.close()



##Parameters: Start,stop : The domain on a closed inteveral - defined by the set of integers
            ##a,b,c the values for the parabola ax^2+bx+c - defined by the set of integers
            ##Check to see if a parabola within a certain ibteger domain is one -to-one


def one2OneOrNah(start,stop,a,b,c):
    x = start
    y=start
    z=0
    i=start
    isOne2One = True
    while i<=stop and isOne2One:
        outputA =a*i**2 + b*i +c 
        x=y+z
        z+=1
        while x<=stop: 
            outputB = a*x**2 + b*x +c
            
            if outputA==outputB and x!=i:
                isOne2One= False
            x+=1
            #print("(" + str(i),str(outputA) + "),("+ str(x-1),str(outputB) +")")
        i+=1
    return isOne2One



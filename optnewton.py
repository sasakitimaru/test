import scipy.optimize
def f(x,y):
    return x*x+y*y-25
def f2(x,y):
    return 2*x
def g(x,y):
    return x*x+y*y+14*x-6*y-6
def g2(x,y):
    return 2*y-6
    
def newton(a,b):
    newa = a
    newb = b
    for i in range(5):
        newa = newa - f(newa,newb)/f2(newa,newb)
        
    return newx
    
#result1 = scipy.optimize.newton(f, -1.0)


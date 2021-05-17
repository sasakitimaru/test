def sign(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
def f(x):
    return x**2-3*x+2
def f2(x):
    return -(x**2)+4*x-2
def nibunn(a,b):
    c = 0.0
    for i in range(5):
        c = (a+b)/2.0
        if abs(f(c))<0.0001:
            return c
        if sign(f(a)) == sign(f(c)):
            a = c
        elif sign(f(b)) == sign(f(c)):
            b = c
        print("a:",a,"b:",b,"c:",c)
    print("(",c,",",f(c),")")
    return c
def hasamiuti(a,b):
    c = 0.0
    for i in range(5):
        c = ((a-b)/(f(b)-f(a)))*f(a)+a
        if abs(f(c))<0.0001:
            return c
        if sign(f(a)) == sign(f(c)):
            a = c
        elif sign(f(b)) == sign(f(c)):
            b = c
        print("a:",a,"b:",b,"c:",c)
    print("(",c,",",f(c),")")
    return c
def suiji(a):
    for i in range(5):
        a = f2(a)
        print(a)
    return a
#print(nibunn(-1,3/2))
print(suiji(0.5))

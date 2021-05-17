import scipy.optimize
def f(x):
    return x*x-3*x+2
def f2(x):
    return 2*x-3
def newton(a):
    newx = a
    for i in range(3):
        newx = newx - f(newx)/f2(a)
    return newx
print(newton(3))

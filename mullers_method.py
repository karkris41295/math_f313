#Muller's method
#MATH F313: Numerical Analysis

'''
Kinda like the secant method but now we're approximating our function
with a parabola (passing through f(x1), f(x2), f(x3) instead of a line
'''

def f(x):
    return x**3 -13*x - 12
    
x0, x1, x2 = 4.5, 5.5, 5. # initial guess x0<x2<x1
error = 1e-6 # permissible error

i = 0 # iteration counter
x3 = 0

while abs(f(x3))>error:
    h0 = x1 - x0
    h1 = x2 - x1
    d0 = (f(x1) - f(x0))/h0
    d1 = (f(x2) - f(x1))/h1
    a = (d1-d0)/(h1+h0)
    b = a*h1 + d1
    c = f(x2)
    rad = (b**2 - 4*a*c)**.5 # calculating discriminant of a**2 + bx + c
    if abs(b+rad) > abs(b-rad):
        den = b+rad
    else:
        den = b-rad  # den is the denominator of the quadritic root formula
    
    dxr = -2*c/den
    x3 = x2 + dxr
    x0, x1, x2 = x1, x2, x3 # updating values for next iteration
    i+=1

rt = x3 # storing the root as x2

print 'The root of the equation is ' + str(rt) + '\n' + 'f(root) = ' + str(f(rt))
print 'No. of iterations: ' + str(i)
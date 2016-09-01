#Secant Method
#MATH F313: Numerical Analysis

from math import e

def f(x):
    return 5*e**-x + x - 5
    
x1, x2 = -2., 1.5 # bracket values (x1,x2) = (-2,1.5)
error = 1e-6 # permissible error

i = 0 # iteration counter
x3 = 3

while abs(x2-x1)>error:
    x3 = x2 - (f(x2)*(x2-x1))/(f(x2)-f(x1)) # secant formula
    x1, x2 = x2, x3 # updating values for next iteration
    i+=1

rt = x2 # storing the root as x2

print 'The root of the equation is ' + str(rt) + '\n' + 'f(root) = ' + str(f(rt))
print 'No. of iterations: ' + str(i)
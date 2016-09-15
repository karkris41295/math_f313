#Fixed Point Iteration Method
#MATH F313: Numerical Analysis
from math import sqrt

def f(x):
    return x**3 + x**2 - 100

def phi(x):
    '''
    Function that re-writes f(x) in form of x_i+1 = phi(x_i)
    Here eq. is x**3 + x**2 - 100
    
    we can re-write it as x_n+1 = 10/(x+1)**.5
    
    Note: phi(x) should be such that |dphi(x)/dx| < 1 
    Here it is so.
    '''
    return 10/sqrt(x+1)

x1 = 8 # initial guess
error = 1e-6 # permissible error

i = 0 # iteration counter

while abs(f(x1))>error and i < 200:
    x2 = phi(x1)
    print x2, f(x2)
    x1 = x2
    i+=1 
    
rt = x1 # estimated root of the equation
      
print 'The root of the equation is ' + str(rt) + '\n' + 'f(root) = ' + str(f(rt))
print 'No. of iterations: ' + str(i)
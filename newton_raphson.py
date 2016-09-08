#Bisection Search
#MATH F313: Numerical Analysis

def f(x):
    '''
    6th order Legendre Polynomial Function
    '''
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1
    
def d_dtf(x):
    '''
    Derivative of f(x)
    '''
    return 6*924*x**5 - 5*2772*x**4 + 4*3150*x**3 - 3*1680*x**2 + 420*2*x - 42

def d2f(x):
    '''
    Derivative of f'(x) (for improved Newton-Raphson)
    '''
    return 5*6*924*x**4 - 4*5*2772*x**3 + 3*4*3150*x**2 - 2*3*1680*x + 420*2

def improve(i, x1):
    '''
    Function which optionally uses the improved newton method
    
    Takes 1 argument, if 'True', uses the improved method, else uses the regular method
    
    (comment: not sure about this but I think the improved method is not suitable
              if we're interested in finding certain roots in certain intervals
              it tends to overshoot to an 'unwanted' root due tp high rate of 
              convergence')
    '''
    if i == False:
        return f(x1)/d_dtf(x1)
    elif i == True:
        return (f(x1)*d_dtf(x1))/(d_dtf(x1)**2 - f(x1)*d2f(x1))                
    
import pylab as plt
import numpy as np

def inspect():
    '''
    Function to inspect the possible positions of roots
    '''
    a = np.linspace(0,1,1000)
    b = f(a)
    plt.plot(a,b)
    plt.show()
    
x1, x2 = 10., 0. # first guess and default for x2
error = 1e-6 # permissible error
numer = 10.
i = 0 # iteration counter

while numer>error and i < 200:
    x2 = x1 - improve(True, x1) # Newton-Raphson formula
    print 'x1 = {0}, x2 = {1}'.format(x1, x2)# test line
    numer = abs(x2-x1) # making sure 6 consecutive digits coincide
    x1 = x2
    i+=1 
    
rt = x1 # estimated root of the equation
      
print 'The root of the equation is ' + str(rt) + '\n' + 'f(root) = ' + str(f(rt))
print 'No. of iterations: ' + str(i)
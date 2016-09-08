#Newton-Raphson method for solving multiple nonlinear equations
#MATH F313: Numerical Analysis
#Exercise 6.17: Nonlinear circuits in Mark Newman's 'Computational Physics'

import numpy as np
from numpy.linalg import solve, norm
from math import e

#DATA
vp= 5. #V_plus in volts
r1, r2, r3, r4 = 1., 4., 3., 2. #k-ohm resistances
i = 3. #A constant originally in nA
vt = 0.05 #V_t in volts

def f(x):
    '''
    evaluates f(x) for where x is a 2-dim vector of voltage v1 and v2
    '''
    v1, v2 = x[0], x[1]
    y = np.array([(v1-vp)/r1 + v1/r2 + i*(e**((v1-v2)/vt)-1), (vp-v2)/r3 - v2/r4 + i*(e**((v1-v2)/vt)-1)])
    print y
    return y
    
def gradf(x):
    '''
    n-Derivative of f(x) where x is a vector of n-dimensions
    '''
    v1, v2 = x[0], x[1]
    m = np.array([[1./r1 + 1./r2 + (i/vt)*e**((v1-v2)/vt), (-i/vt)*e**((v1-v2)/vt)],\
    [(i/vt)*e**((v1-v2)/vt), -1*(1./r3 +1./r4 +(i/vt)*e**((v1-v2)/vt))]], dtype = np.float64)#the matrix for the 'grad' f function
    return m

def cls_newton(x):
    '''
    Classroom implementation of the newton raphson method
    '''
    v1, v2 = x[0], x[1]
    f_v1 = 1./r1 + 1./r2 + (i/vt)*e**((v1-v2)/vt)
    f_v2 = (-i/vt)*e**((v1-v2)/vt)
    g_v1 = (i/vt)*e**((v1-v2)/vt)
    g_v2 = -1*(1./r3 +1./r4 +(i/vt)*e**((v1-v2)/vt))
    
    f = (v1-vp)/r1 + v1/r2 + i*(e**((v1-v2)/vt)-1)
    g = (vp-v2)/r3 - v2/r4 + i*(e**((v1-v2)/vt)-1)
    
    print f
    print g
    print f_v2, g_v1, g_v1, f_v1
    v1n = v1 - (f*g_v2 - g*f_v2)/(f_v1*g_v2 - g_v1*f_v2)
    v2n = v2 - (g*f_v1 - f*g_v1)/(f_v1*g_v2 - g_v1*f_v2)
    print v1n
    print v2n
    return np.array([v1n,v2n])

x1 = np.array([4, 5]) #initial guess of roots are 1 and 1 volts
error = 1e-6 # permissible error
i = 0 # iteration counter

while norm(x1)>error and i < 50:
    x2 = cls_newton(x1)
    print x2
    print 'x1 = {0}, x2 = {1}'.format(x1, x2)# test line
    x1 = x2
    print x1
    i+=1 
    
rt = x1 # estimated root of the equation
      
print 'The root of the equation is ' + str(rt) + '\n' + 'f(root) = ' + str(f(rt))
print 'No. of iterations: ' + str(i)
#Newton-Raphson method for solving multiple nonlinear equations
#MATH F313: Numerical Analysis
#Exercise 6.17: Nonlinear circuits in Mark Newman's 'Computational Physics'

from sympy import Matrix, lambdify, symbols, E
from numpy.linalg import norm, solve
from numpy import array

v1, v2 = symbols('v1 v2')

#DATA
vp= 5. #V_plus in volts
r1, r2, r3, r4 = 1e3, 4e3 , 3e3, 2e3  #ohm, data in kilo-ohm
i = 3e-9 #A constant, data originally in nA
vt = 0.05 #V_t in volts

f = Matrix([(v1-vp)/r1 + v1/r2 + i*(E**((v1-v2)/vt)-1), (vp-v2)/r3 - v2/r4 + i*(E**((v1-v2)/vt)-1)]) # defines f(x)
wrt = Matrix([v1, v2]) # ordering matrix to calculate the jacobian
J = f.jacobian(wrt) # Jacobian matrix for f(x)

ki = lambdify([v1, v2], f, 'numpy') # function which subs v1, v2 in kirchoffs equation
gradf = lambdify([v1, v2], J, 'numpy') # function which subs v1, v2 in Jacobian

x = array([1., 5.]) # initial guess for v1 and v2
error = 1e-8 # permissible error
i = 0 # iteration counter

while norm(ki(x[0], x[1]))>error and i < 50:
    v1, v2 = x[0], x[1]
    delta = solve(gradf(v1, v2), ki(v1, v2))
    x_n = x - delta.T[0] # transposing and taking the first row of delta to match dim(x)
    print 'x_n at {0}'.format(i), ' iteration', x_n
    x = x_n    
    i+=1 
    
rt = x # estimated root of the equation
      
print 'The root of the equation is ',  rt , '\nf(root) = ', ki(rt[0], rt[1]).T[0]
print 'No. of iterations: ' + str(i)

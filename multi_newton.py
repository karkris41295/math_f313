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

x = array([1., 1.]) # initial guess for v1 and v2
error = 1e-6 # permissible error
i = 0 # iteration counter

while norm(x)>error and i < 50:
    v1, v2 = x[0], x[1]
    delta = solve(gradf(v1, v2), ki(v1, v2))
    print delta
    x_n = x - delta
    print x_n
    print 'x = {0}, v_n = {1}'.format(x, x_n)# test line
    x = x_n
    print x
    i+=1 
    
rt = x # estimated root of the equation
      
print 'The root of the equation is ' + str(rt) + '\n' + 'f(root) = ' + str(f(rt))
print 'No. of iterations: ' + str(i)

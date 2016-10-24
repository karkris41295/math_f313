#Matrix Solvers
#MATH F313: Numerical Analysis

import numpy as np

A = np.array([[ 2,  1,  4,  1 ],
           [ 3,  4, -1, -1 ],
           [ 1, -4,  1,  5 ],
           [ 2, -2,  1,  3 ]], float)
           
b = np.array([ -4, 3, 9, 7 ],float)

def gauss(A, b):
    """
    Solves matrices using Gaussian Elimination
    
    Parameters
    ----------
    A : 2-D Array of float 
        Matrix to solve
    b : Array of float
        Right hand side to solve for
    
    Returns
    -------
    Ab : 2-D Array
        Returns augmented Matrix with RREF
    """
    
    N = len(b)
    Ab = np.column_stack((A,b))  # Creating an augmented Matrix
    for m in range(N):
        
        # Divide by the diagonal element
        div = Ab[m,m]
        Ab[m,:] /= div
        
        # Now subtract from the lower rows
        for i in range(m+1,N):
            mult = Ab[i,m]
            Ab[i,:] -= mult*Ab[m,:]
            
    # Converting to RREF
    for m in range(N-1,-1,-1):
        for i in range(m+1,N):
            Ab[m,:] -= Ab[m,i]*Ab[i,:]
        
    return Ab[:,N] #Returns last column of augmented matrix
    
def gauss_pp():
    """
    Solves matrices using Gaussian Elimination with partial pivoting
    
    Parameters
    ----------
    A : 2-D Array of float 
        Matrix to solve
    b : Array of float
        Right hand side to solve for
    
    Returns
    -------
    Ab : 2-D Array
        Returns augmented Matrix with RREF
    """
   
    N = len(b)
    Ab = np.column_stack((A,b))  # Creating an augmented Matrix
    for m in range(N):
        
        # Divide by the diagonal element
        div = Ab[m,m]
        Ab[m,:] /= div
        
        # Now subtract from the lower rows
        for i in range(m+1,N):
            mult = Ab[i,m]
            Ab[i,:] -= mult*Ab[m,:]
            
    # Converting to RREF
    for m in range(N-1,-1,-1):
        for i in range(m+1,N):
            Ab[m,:] -= Ab[m,i]*Ab[i,:]
        
    return Ab[:,N] #Returns last column of augmented matrix
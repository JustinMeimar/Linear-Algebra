#topics in 125

import numpy as np


#show case dot products:
def showDotProd():
    v1 = [1,3,4]
    v2 = [5,4,2]
    print(np.dot(v1,v2))

#showcase matrix multiplication
def showMatrix():
    m1 = np.array([[1,0],[0,1]]) #indentity matrix
    m2 = np.array([[4,2],[7,3]]) #matrix 

    print(m1@m2)

#showCase EigenValues:
def showEigenValues():
    # i need to review my eigen knowledge....
    # temrs: normalization, diagonalization, transpose, orthogonal matrix... 
    pass

def main():
    showDotProd()
    showMatrix()
    print("hello world")

if __name__ == "__main__":
    main()

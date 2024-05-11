import numpy as np

def linear_system(coff,const):
    sol=np.linalg.solve(coff,const)
    return sol

def eigen(mat):
    Eigen_values,Eigen_vectors=np.linalg.eig(mat)
    return Eigen_values,Eigen_vectors

        
coff=np.array([[1,2],[3,4]])
const=np.array([5,6])
print(f"coff:\n{coff}\nconst:{const}\nsolution:\n{linear_system(coff,const)}\n\n\n")


mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
Eigen_values , Eigen_vectors=eigen(mat)     
print(f"Matrix:\n{mat}\nEigen values:{Eigen_values}\nEigen vector:\n{Eigen_vectors}")                                 
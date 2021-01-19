import numpy as np
from scipy.sparse import csc_matrix

###############################################################
## Creates diagonal algebra generators for so(N), su(N), sp(N)
###############################################################

def spin(k):
    if k==0:
        return csc_matrix((
            np.array([1+0j, 1+0j], dtype=np.complex), (
                np.array([0, 1]), 
                np.array([1, 0])
            )), shape=(2, 2))
    elif k==1:
        return csc_matrix((
            np.array([0-1j, 0+1j], dtype=np.complex), (
                np.array([0, 1]), 
                np.array([1, 0])
            )), shape=(2, 2))
    elif k==2:
        return csc_matrix((
            np.array([1+0j, -1+0j], dtype=np.complex), (
                np.array([0, 1]), 
                np.array([0, 1])
            )), shape=(2, 2))
    else:
        raise ValueError('the number of pauli matrices is 3')
        
def embed_spin(k, d, ax0, ax1):
    t = spin(k)
    T = csc_matrix((d_size, d_size), dtype=np.complex)
    T[ax0, ax0] = t[1,1]
    T[ax1, ax1] = t[1,1]
    T[ax0, ax1] = t[0,1]
    T[ax1, ax0] = t[1,0]
    return T

# def creation_annihilation(d_size, idx1, idx2):
#     op = np.zeros((d_size, d_size))
#     op[idx1, idx2] = 1
#     return op

# Up = creation_annihilation(3, 0, 1)
# Vp = creation_annihilation(3, 1, 2)
# Ip = creation_annihilation(3, 0, 2)

# 0.5*(Up+Up.T)
# -0.5j*(Up-Up.T)

# def mod_sign(arr_list):
#     new_list = []
    
#     for arr in arr_list:
#         new_sign = True
        
#         for new in new_list:
#             if np.abs(arr+new).sum()==0:
#                 new_sign=False
#                 break
#         if new_sign:
#             new_list.append(arr)
#     return new_list
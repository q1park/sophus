import numpy as np

###############################################################
## Creates diagonal Cartan generators for so(N), su(N), sp(N)
###############################################################

def make_cartans_suN(N):
    if N<2 or N>4:
        raise ValueError('choose range between 2 and 4')
    elif N==2:
        return [np.diag([1+0j, -1+0j])]
    elif N==3:
        return [
            np.diag([1+0j, -1+0j, 0+0j]),
            np.diag([1+0j, 1+0j, -2+0j])/np.sqrt(3)
        ]
    elif N==4:
        return [
            np.diag([1+0j, -1+0j, 0+0j, 0+0j])/np.sqrt(2), 
            np.diag([1+0j, 1+0j, -2+0j, 0+0j])/np.sqrt(6),
            np.diag([1+0j, 1+0j, 1+0j, -3+0j])/np.sqrt(12)
        ]
    
def make_cartans_soN(N):
    if N<3 or N>7:
        raise ValueError('choose range between 2 and 4')
    elif N==3:
        return [np.diag([1+0j, -1+0j, 0+0j])]
    elif N==4:
        return [
            np.diag([1+0j, -1+0j, 0+0j, 0+0j]), 
            np.diag([0+0j, 0+0j, 1+0j, -1+0j])
        ]
    elif N==5:
        return [
            np.diag([1+0j, -1+0j, 0+0j, 0+0j, 0+0j]), 
            np.diag([0+0j, 0+0j, 1+0j, -1+0j, 0+0j])
        ]
    
    elif N==6:
        return [
            np.diag([1+0j, -1+0j, 0+0j, 0+0j, 0+0j, 0+0j]), 
            np.diag([0+0j, 0+0j, 1+0j, -1+0j, 0+0j, 0+0j]),
            np.diag([0+0j, 0+0j, 0+0j, 0+0j, 1+0j, -1+0j])
        ]
    elif N==7:
        return [
            np.diag([1+0j, -1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]), 
            np.diag([0+0j, 0+0j, 1+0j, -1+0j, 0+0j, 0+0j, 0+0j]),
            np.diag([0+0j, 0+0j, 0+0j, 0+0j, 1+0j, -1+0j, 0+0j])
        ]
    
def make_cartans_spN(N):
    if N<4 or N>4:
        raise ValueError('choose range between 4 and 4')
    elif N==4:
        return [
            np.diag([1+0j, 0+0j, -1+0j, 0+0j]), 
            np.diag([0+0j, 1+0j, 0+0j, -1+0j])
        ]
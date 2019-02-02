import numpy as np
def Vi(ai):
    return 1/(3*(1+ai)**2)

def V(a_prms):
    D=1
    for a in a_prms:
        D*=(1+Vi(a))     
    return D-1

def S_i(ai,a):
    return Vi(ai)/V(a)

def S_T(ai,a):
    Dtot=V(a)
    return (Dtot+1)/(Vi(ai)+1)*Vi(ai)/Dtot

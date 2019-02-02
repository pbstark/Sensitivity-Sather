import numpy as np
import pandas as pd

k = 6

a2 = [0, 0, 6.52, 6.52, 6.52, 6.52]
b3 = [6.52, 6.52, 6.52, 6.52, 6.52, 6.52]


def A1(sm):
 dummyA1 = pd.DataFrame()
 for j in range(0,k):
  dummyA1[j] = np.prod(sm[sm.columns[0:j+1]], axis = 1)*(-1)**(j+1)
 return dummyA1.sum(axis=1)

def A2(sm):
 dummyA2 = pd.DataFrame()
 for j in range(0,k):
  dummyA2[j] = (abs(4*sm[sm.columns[j]]-2)+a2[j])/(1+a2[j])
 return (dummyA2.product(axis=1))

def B1(sm):
 dummyB1 = pd.DataFrame()
 for j in range(0,k):
  dummyB1[j] = (k-sm[sm.columns[j]])/(k-0.5)
 return dummyB1.product(axis=1)

def B2(sm):
 dummyB2 = pd.DataFrame()
 for j in range(0,k):
  dummyB2[j] = (sm[sm.columns[j]])**(1/k)
 return dummyB2.product(axis=1)*((1+1/k)**k)

def B3(sm):
 dummyB3 = pd.DataFrame()
 for j in range(0,k):
  dummyB3[j] = (abs(4*sm[sm.columns[j]]-2)+b3[j])/(1+b3[j])
 return (dummyB3.product(axis=1))

def C1(sm):
 dummyC1 = pd.DataFrame()
 for j in range(0,k):
  dummyC1[j] = pd.Series(abs(4*sm[sm.columns[j]]-2))
 return (dummyC1.product(axis=1))

def C2(sm):
 return (sm.product(axis=1)*2**k)

functions = [A1, A2, B1, B2, B3, C1, C2]

#AEA1

def Ek2(k):
 return((1/6)*(1-(1/3)**k)+(4/15)*((-1)**(k+1)*(1/2)**k+(1/3)**k))

def V(k):
 return((1/10)*(1/3)**k+(1/18)-(1/9)*(1/2)**(2*k)+(-1)**(k+1)*(2/45)*(1/2)**k)

for j in range(0, k):
 def Ej(j):
  return((1/6)*(1-(1/3)**(j))+(4/15)*((-1)**(j+1)*(1/2)**(j)+(1/3)**(j)))

 def T1(j):
  return((1/2)*((1/3)**(j-1)*(1-(1/3)**(k-j))))

 def T2(j):
  return((1/2)*((1/3)**j-(1/3)**k))

 def T3(j):
  return((3/5)*(4*(1/3)**(k+1)+(-1)**(j+k+1)*(1/2)**(k-j-2)*(1/3)**(j+1)))

 def T4(j):
  return((1/5)*((-1)**(j+2)*(1/3)*(1/2)**(j-2)-4*(1/3)**(j+1)))

 def T5(j):
  return((1/5)*((-1)**(k+1)*(1/3)*(1/2)**(k-2)+(-1)**(k+j)*(1/3)**(j+1)*(1/2)**(k-j-2)))

def A1ST(j):
 return((Ek2(k)-Ej(j)-(1/4)*(T1(j)-2*T2(j)+T3(j))-T4(j)-T5(j))/V(k))

def A1S(j):
 return((Ek2(k)-Ej(j)-(1/4)*(T1(j)-2*T2(j)+T3(j))-T4(j)-T5(j))*(12*(1-(-1/2)**k)**2)/(V(k)*27*((1/2)-(4/5)*\
   (-1/2)**k+(3/10)*(1/3)**k)))

#AEA2

def VjA2(j):
 return((1/3)/(1+a2[j])**2)

def VA2(j):
 productA2 = []
 for j in range(0, k):
  productA2.append(1+VjA2(j))
 return np.product(productA2)-1

def VnA2(j):
 return((VA2(j)+1)/(1+VjA2(j)))

def VTjA2(j):
 return VjA2(j)*(VnA2(j))

def A2ST(j):
 return(VTjA2(j)/VA2(j))

def A2S(j):
 return(VjA2(j)/VA2(j))

#AEB1

def p(j):
 return(12*(k-0.5)**2)

def B1ST(j):
 return((p(j)+1)**k/((p(j)+1)*((p(j)+1)**k-p(j)**k)))

def B1S(j):
 return(1/(p(j)*((1+1/p(j))**k-1)))

#AEB2

def B2ST(j):
 return((k+1)**(2*k-2)/(((k+1)**(2*k)-(k**2+2*k)**k)))

def B2S(j):
 return(1/((k**2+2*k)*((1+1/((k**2+2*k)))**k-1)))

#AEB3

def VjB3(j):
 return((1/3)/(1+b3[j])**2)

def VB3(j):
 productB3 = []
 for j in range(0, k):
  productB3.append(1+VjB3(j))
 return np.product(productB3)-1

def VnB3(j):
 return((VB3(j)+1)/(1+VjB3(j)))

def VTjB3(j):
 return VjB3(j)*(VnB3(j))

def B3ST(j):
 return(VTjB3(j)/VB3(j))

def B3S(j):
 return(VjB3(j)/VB3(j))

#AEC1

def C1ST(j):
 return 4**(k-1)/(4**k-3**k)

def C1S(j):
 return 3**(k-1)/(4**k-3**k)

#AEC2
def C2ST(j):
 return 4**(k-1)/(4**k-3**k)

def C2S(j):
 return 3**(k-1)/(4**k-3**k)

def create_dict(key, values):
 return dict(zip(key, values))

analyticalValues = [A1ST, A2ST, B1ST, B2ST, B3ST, C1ST, C2ST]

analyticalValuesF = [A1S, A2S, B1S, B2S, B3S, C1S, C2S]   

AE = []
AE_names = []
for w in analyticalValues:
 for j in range (0,k):
  AE.append(w(j))
  AE_names.append('AE' + str(w.__name__) + str(j+1))
AE_dic = create_dict(AE_names, AE)

AEF = []
AEF_names = []
for wf in analyticalValuesF:
 for j in range (0,k):
  AEF.append(wf(j))
  AEF_names.append('AE' + str(wf.__name__) + str(j+1))
AEF_dic = create_dict(AEF_names, AEF)

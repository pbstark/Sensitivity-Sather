import matplotlib 
import matplotlib.pyplot as plt
import numpy as np


def hyperSphere_hyperCube_ratio(N):
    Vsphere=[1]
    Ssphere=[2]
    Vcube=[1]
    SphereCubeRatio=[]

    dims=range(N)
    
    for n in dims:
        Ssphere.append(2*np.pi*Vsphere[n])
        Vsphere.append(Ssphere[n]/(n+1))
        Vcube.append(2**(n+1))
        SphereCubeRatio.append(Vsphere[-1]/Vcube[-1])
    
    return SphereCubeRatio

fig1, ax1 = plt.subplots()
# Pie chart
expl = (0.2, 0)  # only "explode" the fist slice (i.e. 'oat')

# Pie chart
mylabels = 'OAT', 'Global SA'

def update_pie(Ndim):
    ax1.clear()
    oat=hyperSphere_hyperCube_ratio(Ndim)[-1]
    sizes = [oat, 1-oat]
    ax1.pie(sizes, explode=expl, labels=mylabels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()    


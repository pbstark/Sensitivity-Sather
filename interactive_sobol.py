import chaospy as cp
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
import sobol_seq

f, ax = plt.subplots(2, 2, sharey=True, sharex=True)

u1 = cp.Uniform(0,1)
u2 = cp.Uniform(0,1)
jpdf = cp.J(u1, u2)

f.suptitle('Sobol sequences versus random sampling')

# dictionary of chaospy sampling methods
cp_smpl_dict={'C': 	'Chebyshev nodes', 'NC':  'Nested Chebyshev', 'K': 'Korobov', 'R': 	'(Pseudo-)Random',
                  'RG': 'Regular grid', 'NG': 'Nested grid', 'L': 'Latin hypercube', 'S': 'Sobol', 'H': 'Halton', 'M':  'Hammersley'}

def up_Sobol(N):
    ax[0][0].clear()
    ax[0][1].clear()
    ax[1][0].clear()
    ax[1][1].clear()
        
    sample_0 = np.random.rand(2**N, 2)
    samples_1 = jpdf.sample(size=2**N, rule='R')
    samples_2 = jpdf.sample(size=2**N, rule='L')
    samples_3 = jpdf.sample(size=2**N, rule='S')


    ax[0][0].scatter(sample_0[: 0],sample_0[: 1],size=1,color='b')
    ax[0][1].scatter(*samples_1,s=1,color='b')
    ax[1][0].scatter(*samples_2,s=1,color='b')
    ax[1][1].scatter(*samples_3,s=1,color='b')
    
    ax[0][0].set_title('Random')
    ax[0][1].set_title('(Pseudo-)Random')
    ax[1][0].set_title('Latin hypercube')
    ax[1][1].set_title('Sobol')
    
    plt.show()    


def print_table(table,col_labels,row_labels,precision):
    import pandas as pd
    
    pd_table=pd.DataFrame(table,columns=col_labels,index=row_labels)
    
    for i,label in enumerate(col_labels):
        pd_table[label]= pd_table[label].round(precision[i])
    
    print(pd_table)

def print_vectors_relerror(v1,v2,col_labels,row_labels,precision):
    import numpy as np
    
    the_table=np.column_stack((v1, v2, np.abs(v1-v2)*100/v2))
    print_table(the_table,col_labels,row_labels,precision)

def print_3vectors_relerror(v1,v2,va,col_labels,row_labels,precision):
    # va is the analytical vector
    # v1 and v2 are presented with relative errors wrt va
    import numpy as np
    the_table=np.column_stack((v1, v2, np.abs(v1-v2)*100/v2))
    the_table=np.column_stack((v1,np.abs(v1-va)*100/va, v2, np.abs(v2-va)*100/va))
    print_table(the_table,col_labels,row_labels,precision)

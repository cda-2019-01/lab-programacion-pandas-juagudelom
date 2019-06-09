##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv

import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

x0 = pd.read_csv('tbl2.tsv', sep='\t')
x0['lista'] = x0[['_c5a','_c5b']].apply(lambda x0: ':'.join(map(str,x0)), axis=1)
x0 = x0.sort_values('lista')
x1 = x0.groupby('_c0')['lista'].apply(lambda x0: ','.join(map(str, x0))).reset_index()
print(x1)
##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv


import pandas as pd
import numpy as np
import datetime
pd.set_option('display.notebook_repr_html', False)

x0 = pd.read_csv('tbl0.tsv', sep='\t')
x0 = x0.sort_values('_c2')
x1 = x0.groupby('_c1')['_c2'].apply(lambda x0: ':'.join(map(str, x0))).reset_index()
x1 = x1.rename(index=str, columns={"_c2": "lista","_c1": "_c0"})

print(x1)

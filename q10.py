##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv

import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

x0 = pd.read_csv('tbl1.tsv', sep='\t')
x0 = x0.sort_values('_c4')
x1 = x0.groupby('_c0')['_c4'].apply(lambda x0: ','.join(map(str, x0))).reset_index()
x1 = x1.rename(index=str, columns={"_c4": "lista","_c0": "_c0"})

print(x1)
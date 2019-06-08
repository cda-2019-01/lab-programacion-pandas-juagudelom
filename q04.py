##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

data = pd.read_csv("tbl1.tsv", sep="\t")
u = sorted(data['_c4'].unique())
print(str(u).upper())
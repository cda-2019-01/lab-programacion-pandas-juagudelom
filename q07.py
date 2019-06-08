##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 

import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

data = pd.read_csv("tbl0.tsv", sep="\t")
data['suma'] =data['_c0']+data['_c2']

print(data)

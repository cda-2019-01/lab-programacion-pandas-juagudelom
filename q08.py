##
## Agregue el año como una columna a la tabla tbl0.tsv 

import pandas as pd
import numpy as np
import datetime
import itertools

x = pd.read_csv('tbl0.tsv', sep='\t')
aux = x.copy()
aux['ano'] = aux['_c3'].replace('-[0-9][0-9]-[0-9][0-9]', '', regex=True).astype(object)
print(aux)


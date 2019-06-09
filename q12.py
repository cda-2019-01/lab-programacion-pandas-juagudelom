##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
 
import pandas as pd
import numpy as np
import itertools
pd.set_option('display.notebook_repr_html', False)

x0 = pd.read_csv("tbl0.tsv", sep="\t")
x1 = pd.read_csv("tbl2.tsv", sep="\t")
suma = x1.groupby('_c0').sum()['_c5b']
x0['suma']= suma
x0.groupby('_c1').sum()['suma']


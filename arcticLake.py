import pandas as pd
import numpy as np
from IPython import get_ipython
from nbformat import read
from IPython.core.interactiveshell import InteractiveShell
from scipy.special import polygamma
from scipy.special import digamma
import numpy as np
import math
from numpy.linalg import inv
import mydef

excel_file = "E:/thesis2/arctic_lake.xlsx"
arctic = pd.read_excel(excel_file)
Y1 = arctic['sand']
Y2 = arctic['silt']
Y3 = arctic['clay']
X = arctic['depth']

[[a1],[c1]]= mydef.mom(Y1)
[[r1],[e1]] = mydef.Gg(a1,c1,Y1)
#[[a1],[c1]] = [[a1],[c1]] - [[r1],[e1]]
a1 = a1 - r1
c1 = c1 - e1

print("Divya1")

[[r1],[e1]] = mydef.Gg(a1,c1,Y1)
a1 = a1 - r1
c1 = c1 - e1

print("Divya2")
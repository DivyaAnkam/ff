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

a = np.zeros(3)
c = np.zeros(3)
r = np.zeros(3)
e = np.zeros(3)
i=2
print(a[i]," ",c[i],"\n",r[i]," ",e[i])
anew = a
cnew = c
[[a[i]],[c[i]]]= mydef.mom(Y3)
mom = np.vectorize(mydef.mom,cache=False)
list(mom(Y3))
print(a[i]," ",c[i],"\n")
count = 0
while 1:
  [[r[i]],[e[i]]] = mydef.Gg(a[i],c[i],Y1)
  #[[a1],[c1]] = [[a1],[c1]] - [[r1],[e1]]
  anew[i] = a[i] - r[i]
  cnew[i] = c[i] - e[i]
  print("count is ",count,"\n")
  count += 1
  if (anew[i] <= 0 or cnew[i]<= 0 or abs(r[i]) < 0.01 or abs(e[i]) < 0.01) :
    print("break")
    break
  a[i] = anew[i]
  c[i] = cnew[i]
  print("div")

print(a[i]," ",c[i],"\n",r[i]," ",e[i])


print("Divya21")
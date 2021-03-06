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
Y = [[Y1],[Y2],[Y3]]
a = [0] * 3
c = [0] * 3
r = [0] * 3
e = [0] * 3
i=2
print(a[i]," ",c[i],"    ",r[i]," ",e[i])
anew = [0] * 3
cnew = [0] * 3
[[a[i]],[c[i]]]= mydef.mom(Y3)
print(anew[i]," ",cnew[i],"\n")
count = 0
while 1:
  [[r[i]],[e[i]]] = mydef.Gg(a[i],c[i],Y3)
  #[[a1],[c1]] = [[a1],[c1]] - [[r1],[e1]]
  print(a[i]," ",c[i],"   ",r[i]," ",e[i])
  mya = a[i]
  myc = c[i]
  anew[i] = mya - r[i]
  cnew[i] = myc - e[i]
  print(a[i]," ",c[i],"   ",r[i]," ",e[i])
  print("count is ",count,"\n")
  count += 1
  if (anew[i] <= 0 or cnew[i]<= 0 or abs(r[i]) < 0.01 or abs(e[i]) < 0.01) :
    print("break")
    break
  a[i] = anew[i]
  c[i] = cnew[i]
  print("div")

print(a[i]," ",c[i],"   ",r[i]," ",e[i])
print("y1",np.average(Y1))
print("y2",np.average(Y2))
print("y3",np.average(Y3))

#print(Y[i],Y3)
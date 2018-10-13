from scipy.special import polygamma
from scipy.special import digamma
import numpy as np
import math
from numpy.linalg import inv

def dg1da(a,b):
    value = trigamma(a)-trigamma(a+b)
    return value;

def trigamma(a):
    value = polygamma(1, a)
    return value;

def dg1db(a,b):
    value = -trigamma(a+b)
    return value;

def dg2da(a,b):
    return dg1db(a,b);

def dg2db(a,b):
    value = trigamma(b) - trigamma(a+b)
    return value;

def g1(a,b,xx):
    value = digamma(a) - digamma(a+b) - ((np.sum(np.log(xx)))/len(xx))
    return value;

def g2(a,b,xx):
    value = digamma(b) - digamma(a+b) - ((np.sum(np.log(np.subtract(1,xx))))/len(xx))
    return value;

def g(a,b,x):
    return [[g1(a,b,x)],[ g2(a,b,x)]]

def G(a,b):
    return [[dg1da(a,b),dg1db(a,b)],[dg2da(a,b),dg2db(a,b)]];

def Gg(a,b,X):
    return np.matmul(inv(G(a,b)),g(a,b,X))

def mom(X):
    x = (np.sum(X)) / len(X)
    S = np.std(X)
    a = x * ((x * (1 - x)) / (S * S) - 1)
    b = (1 - x) * ((x * (1 - x) / (S * S)) - 1)

    return [[a], [b]];


import sys
import pandas as pd
import numpy as np

a=sys.argv
if len(a)!=5:
    print("Incorrect number of parameters")
    sys.exit()

f=a[1]
w=a[2].split(',')
im=a[3].split(',')
out=a[4]

try:
    d=pd.read_csv(f)
except:
    print("File not found")
    sys.exit()

if d.shape[1]<3:
    print("Input file must contain three or more columns")
    sys.exit()

x=d.iloc[:,1:].values

try:
    x=x.astype(float)
except:
    print("Non numeric values found")
    sys.exit()

if len(w)!=x.shape[1] or len(im)!=x.shape[1]:
    print("Weights and impacts size mismatch")
    sys.exit()

for i in im:
    if i!='+' and i!='-':
        print("Impacts must be + or -")
        sys.exit()

w=np.array(w,dtype=float)
x=x/np.sqrt((x**2).sum(axis=0))
x=x*w

p=np.zeros(x.shape[1])
n=np.zeros(x.shape[1])

for i in range(x.shape[1]):
    if im[i]=='+':
        p[i]=x[:,i].max()
        n[i]=x[:,i].min()
    else:
        p[i]=x[:,i].min()
        n[i]=x[:,i].max()

sp=np.sqrt(((x-p)**2).sum(axis=1))
sn=np.sqrt(((x-n)**2).sum(axis=1))
s=sn/(sp+sn)

d['Topsis Score']=s
d['Rank']=s.argsort().argsort()+1
d.to_csv(out,index=False)

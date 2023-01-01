import numpy as np
import pandas as pd
#import mathplotlib as mpl

data=pd.read_csv('SAT.csv')
x=data['SAT']
y=data['GPA']



def linear(x,y):
    n=len(x)
    xm=x.mean()
    ym=y.mean()
    slope_num=((x-xm)*(y-ym)).sum()
    slope_den=((x-xm)**2).sum()
    slope=slope_num/slope_den
    coeff=ym-(slope*xm)
    line = 'y = {} + {}β'.format(coeff, round(slope, 3))
    return(slope,coeff,line)

def corr(x,y):
    N = len(x)
    num = (N * (x*y).sum()) - (x.sum() * y.sum())
    den = np.sqrt((N * (x**2).sum() - x.sum()**2) * (N * (y**2).sum() - y.sum()**2))
    R = num / den
    return R

def result(slope,coeff,x2):
    y=coeff+(slope*x2)
    return y

def cost(x,y,slope,coeff):
    n=len(x)
    pred=[]
    for i in range(0,n):
        yp=result(slope,coeff,x[i])
        pred.append(yp)

    a=1/2*n
    x=0
    for i in range(0,n):
        yb=(pred[i]-y[i])**2
        
        x+=yb
    J=a*x
    return J

b1,b2,line=linear(x,y)
r=corr(x,y)
#print("Goodness of fit: {}".format(r**2))


J=cost(x,y,b1,b2)

print("Cost function is: {}".format(J))
x2=int(input("Enter SAT score: "))
y=result(b1,b2,x2)
print("GPA for {} SAT score is {}".format(x2,y))

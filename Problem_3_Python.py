import numpy as np
import matplotlib.pyplot as plt

def datafit(data):
    x=data[:,0]
    y=data[:,1]
    
    if len(data)>=11:
        l=10
    else:
        l=len(data)-1
        
    error=np.zeros((1,l))
    
    for m in range (1,l):
        coeff=np.polyfit(x,y,m)
        f=np.polyval(coeff,x)
        error[0,m-1]=np.linalg.norm(y-f)
        
    FindError=error.argmin()
    FinalCoeff=np.polyfit(x,y,FindError+1)
    print(FinalCoeff)
    
    plt.scatter(x,y,label='data points')
    plt.plot(np.arange(min(x),max(x),0.0001),np.polyval(FinalCoeff,np.arange(min(x),max(x),0.0001)),'r-',label='graph of best fit')
    plt.title('Curve of Best Fit For Data Points (x,y)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper right')
    plt.grid()
    
print('Insert data as numpy format. Example, np.array([(1,2),(3,4),(5,6)])\n')
print('-----------------------------------------')
m = eval(input('Insert data: '))
print('-----------------------------------------')
datafit(m)

import numpy as np

def datafit(data):
    x = data[:,0]
    y = data[:,1]
    error=np.zeros((1,len(data)-1))
    
    if len(data) <= 10:
        for m in range(0,len(data)-1):
            coeff = np.polyfit(x,y,m)
            f = np.polyval(coeff,x)
            error[0,m] = np.linalg.norm(y-f)
    else:
       for m in range(1,10):
            coeff = np.polyfit(x,y,m)
            f = np.polyval(coeff,x)
            error[0,m] = np.linalg.norm(y-f)
        
    FindError = error.argmin()
    FinalCoeff = np.polyfit(x,y,FindError+1)
    print(FinalCoeff)
    
print('Insert data as numpy format. Example, np.array([(1,2),(3,4),(5,6)])\n')
print('-----------------------------------------')
m = eval(input('Insert data: '))
print('-----------------------------------------')
datafit(m)
    
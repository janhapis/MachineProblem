import math 
import numpy as np
import matplotlib.pyplot as plt

def y(h,vo,ang,ay,t):
    y=h+vo*math.sin(ang)*t+(1/2)*ay*t**2
    return y
def x(vo,ang,ax,t):
    x=vo*math.cos(ang)*t+(1/2)*ax*t**2
    return x

def xideal(vo,ang,t):
    xideal=vo*math.cos(ang)*t
    return xideal
    
def projectile(h,vo,ang,ax,ay):
    if ay == 0:
        raise Exception('Error! y-component cannot be greater than or equal to zero as the projectile will not reach the ground.')
        return
    if ay>=0:
        raise Exception('Error! y-component cannot be greater than or equal to zero as the projectile will not reach the ground.')
        return
    ang=(ang*math.pi)/180
    tfinal=(-vo*math.sin(ang)+((vo*math.sin(ang))**2-2*ay*h)**(1/2))/ay
    if tfinal<=0 or tfinal<(-vo*math.sin(ang)/ay):
        tfinal=(-vo*math.sin(ang)-((vo*math.sin(ang))**2-2*ay*h)**(1/2))/ay
    Y=[]
    X=[]
    XIDEAL=[]
    for t in np.arange(0,tfinal,0.01):
        Y=Y+[y(h,vo,ang,ay,t)]
        X=X+[x(vo,ang,ax,t)]
        XIDEAL=XIDEAL+[xideal(vo,ang,t)]
    
    plt.grid()    
    plt.title('Projectile Motion')
    plt.xlabel('Range in Meters(m)')
    plt.ylabel('Height in Meters(m)')
    plt.plot(X,Y, 'b-',label = 'Non-ideal trajectory')
    plt.plot(XIDEAL,Y, 'r--', label = 'Ideal trajectory')
    plt.legend(loc="upper right")
    plt.show()

print('-----------------------------------------')
z = eval(input('Insert height: '))
w = eval(input('Insert velocity: '))
p = eval(input('Insert angle: '))
o = eval(input('Insert x-component: '))
t = eval(input('Insert y-component: '))
print('-----------------------------------------')
projectile(z,w,p,o,t)            
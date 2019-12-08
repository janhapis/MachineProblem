import math as math
import numpy as np
import matplotlib.pyplot as plt

def yactual(h,vo,ang,ay,t):
    yactual=h+vo*math.sin(ang)*t+(1/2)*ay*t**2
    return yactual
def xactual(vo,ang,ax,t):
    xactual=vo*math.cos(ang)*t+(1/2)*ax*t**2
    return xactual
def yideal(h,vo,ang,t):
    yideal=h+vo*math.sin(ang)*t+(1/2)*(-9.8)*t**2
    return yideal
def xideal(vo,ang,t):
    xideal=vo*math.cos(ang)*t
    return xideal

def projectile(h,vo,ang,ax,ay):
    if ay>=0:
        raise Exception('y-component of acceleration cannot be greater than or equal to 0 as the projectile will not reach the ground.')
        return
    
    ang=(ang*math.pi)/180
    tfinal=(-vo*math.sin(ang)+((vo*math.sin(ang))**2-2*ay*h)**(1/2))/ay
    if tfinal <=0:
        tfinal=(-vo*math.sin(ang)-((vo*math.sin(ang))**2-2*ay*h)**(1/2))/ay
        
    Yactual=[]
    Xactual=[]
    Xideal=[]
    Yideal=[]
    
    for t in np.arange(0,tfinal,0.01):
        Yactual=Yactual+[yactual(h,vo,ang,ay,t)]
        Xactual=Xactual+[xactual(vo,ang,ax,t)]
        Yideal=Yideal+[yideal(h,vo,ang,t)]
        Xideal=Xideal+[xideal(vo,ang,t)]

    plt.title('Projectile Motion')
    plt.xlabel('range in meters(m)')
    plt.ylabel('height in meters(m)')
    plt.plot(Xactual,Yactual,'b-',label='actual trajectory')
    plt.plot(Xideal,Yideal,'r--',label='ideal trajectory')
    plt.legend(loc='upper right')
    plt.grid()
    
print('-----------------------------------------')
z = eval(input('Insert height in m: '))
w = eval(input('Insert velocity in m/s: '))
p = eval(input('Insert angle in degrees with respect to x-axis: '))
o = eval(input('Insert x-component of acceleration: '))
t = eval(input('Insert y-component of acceleration: '))
print('-----------------------------------------')
projectile(z,w,p,o,t)       

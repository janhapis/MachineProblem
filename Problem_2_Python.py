def circle(p1,p2,p3):
    x1 = float(p1[0])
    x2 = float(p2[0])
    x3 = float(p3[0])
    y1 = float(p1[1])
    y2 = float(p2[1])
    y3 = float(p3[1])
    
    k = ((((x1-x2)*(x2**2-x3**2+y2**2-y3**2))-((x2-x3)*(x1**2-x2**2+y1**2-y2**2)))/((2*(x1-x2)*(y2-y3))-(2*(x2-x3)*(y1-y2))))
    h = ((((x1**2-x2**2)+(y1**2-y2**2)-2*k*(y1-y2))/(2*(x1-x2))))
    radius = ((((x1-h)**2+(y1-k)**2)**(1/2)))
    D = -2*h
    E = -2*k
    F = h**2+k**2-radius**2
    
    print('vector:', 'D =',D, ', ', 'E =',E, ', ', 'F =',F)
    print('center: h =',+h, ', k =',+k )
    print('radius:',+radius)

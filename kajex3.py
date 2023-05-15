# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:28:34 2020

@author: lenovo
"""

import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

#function definitions

def functionx(xdash,z,w,x):
    
    k = (2*math.pi)/(w)
    
    return cmath.exp((((cmath.sqrt(-1))*k)/(2*z))*((x-xdash)**2))

def functiony(ydash,z,w,y,E0,xdash,x,xdash1,xdash2):
    
    k = (2*math.pi)/(w) #wavenumber
    X = SimpsonX(xdash1,xdash2,x,functionx,N,z,E0)
    c = (2*math.pi*z)
    
    return c*X*cmath.exp(((cmath.sqrt(-1)*k)/(2*z))*(y-ydash)**2) 


def SimpsonX(xdash1,xdash2,x,f,N,z,w):
    
    if N % 2 != 0:
        print('Enter an even value for N.')
    elif N % 2 == 0:     
        width = (xdash2-xdash1)/N 
        totalsum = functionx(xdash1,z,w,x) + functionx(xdash2,z,w,x)
        for i in range(1,N,2):
            dx = xdash1 + i*width
            totalsum += 4*functionx(dx,z,w,x)   
        for i in range(1,N,2):
            dx = xdash1 + i*width
            totalsum += 2*functionx(dx,z,w,x)
            
    return (width/3)*totalsum
 
def SimpsonY(xdash1,xdash2,x,ydash1,ydash2,y,f,N,z,w,E0):
 
    k = (2*math.pi)/(w)
    if N % 2 != 0:
        print('Enter an even value for N.')
    elif N % 2 == 0:       
        width = (ydash2-ydash1)/N
        totalsum = functiony(ydash1,z,w,y,E0,xdash1,x,xdash1,xdash2) + functiony(ydash2,z,w,y,E0,xdash2,x,xdash1,xdash2)
        for i in range(1,N,2):
            dy = ydash1 + i*width 
            totalsum += 4* functiony(dy,z,w,y,E0,dx,x,xdash1,xdash2) 
        for i in range(1,N,2):
            dy = ydash1 + i*width 
            totalsum += 2* functiony(dy,z,w,y,E0,dx,x,xdash1,xdash2)
    
    return (width/3)*totalsum*((k*E0)/z)


#value definitions

z = float(input('Enter a value for z: '))
N = int(input('Enter an even value for N: '))
xdash1 = -0.0001
xdash2 = 0.0001
ydash1 = -0.0001
ydash2 = 0.0001
w = 700E-9
E0 = 8.85E-12 #permeability of free space
E = 1E-8
c = 3E8 #speed of light


#menu

MyInput = '0'

while MyInput != 'q':
    
    MyInput = input('Enter a choice, "a", "b", "c" or "q" to quit: ')
    print('You entered the choice ', MyInput)
    
    #section A
    if MyInput == 'a':  
        x = 10
        print(SimpsonX(0,N,x,math.pi,math.sin))  
        
    #section B
    elif MyInput == 'b':
        xmin = -4E-3
        xmax = 4E-3
        NumPoints = 200
        dx = (xmax-xmin)/(NumPoints-1)
        xvalues = [0.0] * NumPoints
        yvalues = np.zeros(NumPoints)
        for i in range(NumPoints):
            xvalues[i] = xmin+i*dx
            yvalues[i] = abs((SimpsonX(xdash1,xdash2,xvalues[i],functionx,N,z,w))**2)
        plt.plot(xvalues,yvalues)
        plt.title('|X(x)|^2 as a function of x')
        plt.xlabel('x')
        plt.ylabel('|X(x)|^2')
        plt.show()   
        
    #section C
    elif MyInput == 'c':
        xmin = -0.00002
        xmax = 0.00002
        ymin = -0.00002
        ymax = 0.00002
        NumPoints = 50
        dx = (xmax-xmin)/(NumPoints-1)
        dy = (ymax-ymin)/(NumPoints-1)
        intensity = np.zeros((NumPoints,NumPoints))
        for i in range(NumPoints):
            y = ymin+(i*dy)
            for j in range(NumPoints):
                x = xmin+(j*dx)
                intensity[j,i] = E0*c*abs((SimpsonY(xdash1,xdash2,x,ydash1,ydash2,y,functiony,N,z,w,E)))**2
        plt.imshow(intensity,cmap="Greys")
        plt.show()
        
    
    elif MyInput == 'q':
        print('You have chosen to quit.')
from math import *
from cmath import *
import math
import numpy as np

def StableFactor_Cal(a, b, c, d, e, f, g, h):#S11 S21 S12 S22
    s11=complex(a*cos(b*pi/180), a*sin(b*pi/180));
    s12=complex(e*cos(f*pi/180), e*sin(f*pi/180));
    s21=complex(c*cos(d*pi/180), c*sin(d*pi/180));
    s22=complex(g*cos(h*pi/180), g*sin(h*pi/180));
#    s=zeros(2);
#    s(1,1)=s11;s(1,2)=s12;s(2,1)=s21;s(2,2)=s22;
    delta2=pow(abs(s11*s22-s12*s21), 2);
    k=(1-pow(abs(s11), 2)-pow(abs(s22), 2)+delta2)/(2*abs(s12*s21));
    return k ;

def conjugate(a):
    r=a.real;
    i=a.imag;
    i=-i;
    a=complex(r, i);
    return a;

def StableCircleParameter_Cal(a, b, c, d, e, f, g, h):#S11 S21 S12 S22 MAG&ANG
    s11=complex(a*cos(b*pi/180), a*sin(b*pi/180));
    s12=complex(e*cos(f*pi/180), e*sin(f*pi/180));
    s21=complex(c*cos(d*pi/180), c*sin(d*pi/180));
    s22=complex(g*cos(h*pi/180), g*sin(h*pi/180));
    delta=s11*s22-s12*s21;
    Cl=conjugate(s22-delta*conjugate(s11))/(abs(s22)**2-abs(delta)**2);
    Rl=abs(s12*s21/(abs(s22)**2-abs(delta)**2));
    Cs=conjugate(s11-delta*conjugate(s22))/(abs(s11)**2-abs(delta)**2);
    Rs=abs(s12*s21/(abs(s11)**2-abs(delta)**2));
    return Cl, Rl, Cs, Rs;

def gCal(order, epsilon, f1, f2):
    R0 = 50
    f1 = 37e9;
    f2 = 40e9;
    fc = (f1 + f2) / 2
    BW = (f2 - f1) / fc
    epsilon = 3
    order = int(order)
    N = int(order)
#    order = 5
    betta = log(cosh(epsilon / (40 * log10(exp(1))))/sinh(epsilon / (40 * log10(exp(1)))))
    gamma = sinh(betta.real / (2 * N))
    a=[0 for i in range(order)]
    b = [0 for i in range(order)]
    g = [0 for i in range(order+2)]
    for k in np.arange(0,N):
        a[k] = sin((2 * k +1 ) * pi / (2 * N))
        b[k] = gamma*gamma + (sin((k+1) * pi / N))*(sin((k+1) * pi / N))
    g[0]=1;
    g[1] = 2 * a[0] / gamma;
    for k in np.arange(2, N+1):#4
        g[k] = (4 * a[k -1] * a[k-2]) / ((b[k-2] * g[k-1]))
    if (N% 2) == 0:
        r = ((cosh( betta / 4))**2);
    else:
        r = 1
    g[N+1] = r
    ########################################################################################
    j = [0 for i in range(order + 1)]
    Z0e=[0 for i in range(order + 1)]
    Z0o=[0 for i in range(order + 1)]
    j[0] = (1 / R0) * sqrt((pi * BW) / (2 * g[1]))
    for k in range(1,N):
        j[k] = (1 / R0) * (pi * BW) / (2 * sqrt(g[k] * g[k + 1]))
    j[k + 1] = (1 / R0) * sqrt((pi * BW) / (2 * g[k + 2] * g[k+1]))#g4,g5

    for k in range (0,N + 1):
        Z0e[k] = R0 * (1 + (R0 * j[k]) + (R0 * j[k])**2)
        Z0o[k] = R0 * (1 - (R0 * j[k]) + (R0 * j[k])**2)

    return (g,Z0e,Z0o)

#def oddEvenModeCal()
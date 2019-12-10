"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Code to plot Mass as a function of radius

"""

import numpy as np
import scipy.integrate as area
import matplotlib.pyplot as plt

### Using Cartesian cootdinates
def fz(y,x,r):
    return(area.quad(lambda z:1,-np.sqrt(r**2 -x**2 -y**2),np.sqrt(r**2 -x**2 -y**2))[0])
def fy(x,r):
    return(area.quad(fz,-np.sqrt(r**2 -x**2),np.sqrt(r**2 -x**2),args=(x,r,))[0])
def vol(r):
    volu=area.quad(fy,-r,r,args=(r,))[0]
    return volu


### Using Sperical coordinates
def ar(r,p):
    return(r**2 * np.sin(p))
def fr(R,tet,p):
    return(area.quad(ar,0,R,args=(pi,))[0])
def fpi(R,tet):
    return(area.quad(fr,0,0.5 * np.pi,args=(R,tet,))[0])
def vol2(R):
    return(area.quad(fpi,0,2*np.pi,args=(R,))[0])


p=10
rs=np.linspace(0,10,100)
volu=[(lambda x:p*vol(x))(x) for x in rs]
plt.plot(rs,volu)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.title("Mass vs Radius")
plt.show()


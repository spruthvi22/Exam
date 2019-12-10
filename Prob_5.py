"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Code to plot Mass as a function of radius

"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as inter
import scipy.optimize as root

Theta=float(input("Give a number between 0.1 and 10 : "))
if Theta>10 or Theta<0.1:
    print(" Input Theta is not between 0.1 and 10 ")
    exit()

d_arr=np.loadtxt('data.txt',skiprows=5,usecols=1)
theta_arr=np.loadtxt('data.txt',skiprows=5,usecols=0)
d_func= inter.lagrange(theta_arr,d_arr)
print("The value of data at theta =",Theta," is : ",d_func(Theta))

theta_s=np.linspace(0.1,10,400)
fig=plt.figure()
plt.plot(theta_s,d_func(theta_s),'k',label="Interpolated")
plt.plot(theta_arr,d_arr,'ro',label="Data Points")
plt.xlabel("Theta")
plt.ylabel("d")
plt.title("d vs Theta")
plt.legend()

d_dol_func= lambda x: d_func(x)-370.4
sol=root.newton(d_func-370.4,0.1)
print("the sol = ", sol) 
print("value_sol = ",d_func(sol))

plt.show()

import numpy as np
import scipy.integrate as area
import scipy.optimize as root
import matplotlib.pyplot as plt

def dt(n,lamda):
    return(1/(lamda * n))

def t(n_fin,lamda):
    return(area.fixed_quad(dt,n_fin,10,args=(lamda,))[0])

lamda=1.5
t_10=lambda x: t(x,lamda) - 10
ns=np.linspace(10,0.1,0.01)
ts=[lambda x: t(x,lamda) for x in ns]
plt.plot(ts,ns)
plt.show()

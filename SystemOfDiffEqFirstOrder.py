from sympy.interactive import printing
printing.init_printing(use_latex = True)
import matplotlib.pyplot as plt
import numpy as np

from scipy.integrate import odeint


def solvr (x,t) :
    x1 = x[0]
    x2 = x[1]
    dx2dt = -2*x1 - x2 
    dx1dt = x2
    return [ dx1dt , dx2dt]
x0 = [1 , 0]
t = np.linspace (0,25,1000)

x = odeint (solvr,x0,t)

plt.plot(t,x
    )
plt.show()

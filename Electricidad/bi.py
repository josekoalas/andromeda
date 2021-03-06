import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sy

import sys
sys.path.insert(1, '../Base')
from reg_lin import reg_lin_b as rl
import mpl_config as mpl

mpl.inicio(3)

#Leer datos
d1 = pd.read_csv("BH-4.csv", sep=';', decimal=',')
I1 = d1["I"]
Be1 = d1["Bexp"]
d2 = pd.read_csv("BH-5.csv", sep=';', decimal=',')
I2 = d2["I"]
Be2 = d2["Bexp"]
d3 = pd.read_csv("BH-6.csv", sep=';', decimal=',')
I3 = d3["I"]
Be3 = d3["Bexp"]

#Regresión lineal sin término independiente
b1 = rl(I1, Be1)[0]
xr1 = np.linspace(0, max(I1), 10)
yr1 = b1 * xr1
b2 = rl(I2, Be2)[0]
xr2 = np.linspace(0, max(I2), 10)
yr2 = b2 * xr2
b3 = rl(I3, Be3)[0]
xr3 = np.linspace(0, max(I3), 10)
yr3 = b3 * xr3

#Gráficas
plt.plot(xr1, yr1, label="a=R")
plt.plot(xr2, yr2, label="a=R/2")
plt.plot(xr3, yr3, label="a=2R")

plt.scatter(I1, Be1, linewidth=0.5)
plt.scatter(I2, Be2, linewidth=0.5)
plt.scatter(I3, Be3, linewidth=0.5)

R = 0.2
N = 154
a, r, n, m = sy.symbols("a r n m")
frac = 2 / (1 + ((a**2) / (4 * r**2)))**(3/2)
mu = ((2 * m * r) / n) * (1 / frac)
fmu = sy.lambdify([a, r, n, m], mu, "numpy")

frac1 = frac.subs(a, r)
frac2 = frac.subs(a, r/2)
frac3 = frac.subs(a, 2r)

mu1 = fmu(R, R, N, b1)
mu2 = fmu(R/2, R, N, b2)
mu3 = fmu(2*R, R, N, b3)

mpl.guardar("BH2R", "I(A)", "B(T)")

print("Permeabilidad orginal: {}, P1: {}, P2: {} P3:{}".format(4 * np.pi * 10**(-7), mu1, mu2, mu3))

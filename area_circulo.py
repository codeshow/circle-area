# %%

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# %%

diametro = 10
raio = diametro / 2
origem = diametro/2, diametro/2

lado_quadrado = diametro

# %%

points = np.random.uniform(low=0, high=10, size=[100, 2])

df = pd.DataFrame(points, columns=['x', 'y'])
df.plot.scatter(x='x', y='y')
plt.show()

# %%

def dist(row, origem):
    p1 = np.array([row['x'], row['y']])
    p2 = np.array(origem)
    return np.linalg.norm(p1-p2)

df['dist_origem'] = df.apply(dist, args=(origem,), axis=1)
df['flag_circunferencia'] = df['dist_origem'] <= raio
df

# %%
df[df['flag_circunferencia']].plot.scatter(x='x', y='y')
plt.show()

# %%

area_quadrado = lado_quadrado * lado_quadrado
print("Área Quadrado (Exata):", area_quadrado)

area_circunferencia_aprox = area_quadrado * df['flag_circunferencia'].mean()
print("Área Circunferência (Aprox.):", area_circunferencia_aprox)
print("Área Circunferência (Exata):", np.pi * (raio ** 2))

# %%

p1 = 0.54, 9.75
p2 = 2.35, 8.02

dist = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)
print("Distancia na mão:", dist)

dist_np = np.linalg.norm(np.array(p1) - np.array(p2))
print("Distancia np:", dist_np)

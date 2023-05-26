# %%

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import argparse

def dist(row, origem):
    p1 = np.array([row['x'], row['y']])
    p2 = np.array(origem)
    return np.linalg.norm(p1-p2)


def plot(df):
    df[df['flag_circunferencia']].plot.scatter(x='x', y='y')
    plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--diametro", '-d', default=10, type=int)
    parser.add_argument("--samples", '-s', default=100, type=int)
    parser.add_argument("--plot", '-p', action='store_true')
    args = parser.parse_args()
    
    n = args.samples
    diametro = args.diametro
    raio = diametro / 2
    origem = diametro/2, diametro/2

    points = np.random.uniform(low=0, high=10, size=[n, 2])

    df = pd.DataFrame(points, columns=['x', 'y'])
    df['dist_origem'] = df.apply(dist, args=(origem,), axis=1)
    df['flag_circunferencia'] = df['dist_origem'] <= raio

    area_quadrado = diametro * diametro
    area_circunferencia_aprox = area_quadrado * df['flag_circunferencia'].mean()

    print(f"Tamanho da amostra: {n}")
    print("Área Quadrado (Exata):", area_quadrado)
    print("Área Circunferência (Aprox.):", area_circunferencia_aprox)
    print("Área Circunferência (Exata):", np.pi * (raio ** 2))

    if args.plot:
        plot(df)

if __name__ == "__main__":
    main()
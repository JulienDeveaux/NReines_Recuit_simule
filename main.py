import math
import random


def main():
    for i in range(0, 20):
        res = recuit(0)
        print(round(F(res), 1))

def recuit(X0):
    X = X0
    T = 500  # plus c'est haut plus longtemps on peut remonter la courbe (diminue au fur et a mesure)
    Nt = 100  # nb d'iteration
    Tratio = 10 ** -6
    Tarret = (Tratio ** (1/Nt))
    while F(X) > -9.8 and T > Tarret:
        for i in range(0, Nt):
            Y = voisin(X)
            dF = F(Y) - F(X)
            if accept(dF, T):
                X = Y
        T = decroissance(T)
    return X


def decroissance(T):
    value = (T - (T / 50) * 2)
    if value < 0.05:
        return 0
    else:
        return value


def voisin(x):  # inc ou decremente la valeur de +- 0.1
    rand = random.uniform(-0.1, 0.1)
    return x + rand


def F(x):       #min max -10 10
    return 10 * math.sin((0.3 * x) * math.sin(1.3 * (x ** 2) + 0.00001 * (x ** 4) + 0.2 * x + 80))


def accept(dF, T):
    if dF >= 0:
        A = math.exp(-dF / T)
        if random.uniform(0, 1) >= A:
            return False
    return True


if __name__ == '__main__':
    main()

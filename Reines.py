import math
import random
import time

tailleGrille = 100

def main():
    lesReines = list(range(tailleGrille))
    printPositions(lesReines)
    print(F(lesReines))
    start_time = time.time()
    res = recuit(lesReines)
    stop_time = time.time() - start_time
    printPositions(res)
    print(F(res), ' prises')
    print("temps  : ", stop_time * 1000)



def recuit(X0):
    X = X0
    T = 500  # plus c'est haut plus longtemps on peut remonter la courbe (diminue au fur et a mesure)
    Nt = 100  # nb d'iteration
    Tratio = 10 ** -6
    Tarret = (Tratio ** (1/Nt))
    while F(X) != 0:
        for i in range(0, Nt):
            Y = voisin(X)
            dF = F(Y) - F(X)
            if accept(dF, T):
                X = Y
        T = decroissance(T)
    return X


def decroissance(T):
    value = (T - (T / 50)*2)
    return value


def voisin(x):
    res = list(x)
    pos = random.randint(0, tailleGrille-1)
    pos2 = random.randint(0, tailleGrille-1)
    temp = res[pos]
    res[pos] = res[pos2]
    res[pos2] = temp
    return res


def F(x):       # calcul combien de prises ("energie") le tableau a
    energie = 0
    for i in range(0, tailleGrille):
        if estPrise(x, i, x[i]):
            energie = energie+1
    return energie


def estPrise(x, lig, col):
    for i in range(0, lig):
        if x.__len__() > i and col == x[i] or x[i] == col - (lig - i) or x[i] == col + (lig - i):
            return True
    return False


def accept(dF, T):
    if dF > 0:
        A = math.exp(-dF / T)
        if random.uniform(0, 1) >= A:
            return False
    return True


def printPositions(lesReines):
    grille = [[0] * tailleGrille for _ in range(tailleGrille)]
    output = ""
    it = 0
    for i in lesReines:
        grille[it][i] = 1
        it = it + 1

    for i in range(tailleGrille):
        for j in range(tailleGrille):
            if grille[i][j] == 1:
                output = output + " 👸 "
            else:
                output = output + " _ "
        output = output + "\n"
    print(output)


if __name__ == '__main__':
    main()

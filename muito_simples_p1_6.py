from cmath import sqrt

def distancia(xa, ya, xb, yb):
    distAB = sqrt((xa - xb)**2 + (ya - yb**2))
    d = round(distAB, 5)
    #d = f"{distAB:%.5f}"
    return d

distancia(1,2,5,6)

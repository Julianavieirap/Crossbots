from cmath import sqrt

def distancia(x):
    xy = sqrt((x[1][0] - x[0][0])**2 + (x[1][1] - x[1][0])**2)
    return xy

distancia(([1,2],[5,6]))

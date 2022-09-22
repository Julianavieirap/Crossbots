from array import array
from cmath import sqrt

def distancia(x):
    x = [[],[]]
    distancia_ab = sqrt((x[1][0] - x[0][0])**2 + (x[1][1] - x[1][0])**2)
    return distancia_ab

distancia([[1,2],[5,6]])
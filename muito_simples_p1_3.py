#Recebe um ponto no plano cartesiano e retorna a distância entre eles.

from cmath import sqrt

def distancia(x: list):
    xy = sqrt((x[1][0] - x[0][0])**2 + (x[1][1] - x[0][1])**2)
    return xy

distancia([1,2],[5,6])

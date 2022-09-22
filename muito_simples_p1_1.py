from cmath import sqrt


a = [1,2]
b = [5,6]

coordenada_ya = 2
coordenada_xb = 5
coordenada_yb = 6
coordenada_xa = 1

def distancia(x):
    distancia_ab = sqrt((coordenada_xb - coordenada_xa)**2 + (coordenada_yb - coordenada_ya)**2)
    return x


distancia(1,2,5,6)







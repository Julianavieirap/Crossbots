#Leia um vetor de 10 posições e ache a soma de duas.

lista = [13, 5, 7, 6, 4, 8, 16, 31, 9, 21]

def soma_de_duas_posicoes(num1 = 'Digite X: ', num2 = 'Digite Y: '):
    tamanho_lista = len(lista)
    x = 0
    for x <= num1 <= tamanho_lista & x <= num2 <= tamanho_lista:
        soma = lista(x) + lista(x)
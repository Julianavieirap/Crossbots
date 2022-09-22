# Verifica se um valor é perfeito ou não (soma dos divisores é o próprio valor)

n = int(input('Digite um número: '))
d = 0

for i in range(1,n):
    if (n % i == 0):
        d = d + i

if (d == n):
    print (f'O número {n} é perfeito.')

else print (f'O número {n} NÃO é perfeito.')
# Crie um programa que leia um número real qualquer pelo teclado e mostre em tela a sua porção inteira.

import math
n1 = float(input('Digite um valor:'))
n2 = math.trunc(n1)
print(f'O VALOR DIGITADO FOI DE {n1} E SUA PARTE INTEIRA É {n2}')




from math import trunc
n1 = float(input('Digite um valor:'))
n2 = trunc(n1)
print(f'O VALOR DIGITADO FOI DE {n1} E SUA PARTE INTEIRA É {n2}')

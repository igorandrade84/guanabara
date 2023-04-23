# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

n1 = float (input('DIGITE O VALOR DEFASADO DO SALÁRIO: R$'))
a = n1
b = (a * 15 / 100)
c = a + b
print(f'SALÁRIO PRÉ-AUMENTO: {a:.2f}  REAIS. SALÁRIO PÓS-AUMENTO DE 15%: {c:.2f} REAIS')
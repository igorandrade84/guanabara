# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# \n quebra alinha
# {:.2f} duas casas decimais flutuantes
#
#



n = int(input('DIGITE UM NÚMERO: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print(f'O DOBRO DE {n} É {d} E O TRIPLO DE {n} É {t}. jÁ A RAIZ QUADRADA DE {n} E {r:.3f}')
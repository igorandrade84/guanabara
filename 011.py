# Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área
# e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta, pinta
# uma área de 2m².


n1 = float(input('DIGITE O VALOR DA LARGURA DA PAREDE: '))
n2 = float(input('DIGITE O VALOR DA ALTURA DA PAREDE: '))
a = n1
b = n2
area = (a*b)
tinta = (area/2)
print(f'A ÁREA DA PAREDE É DE: {area}m² . É NECESSÁRIO {tinta} LITROS DE TINTA PARA EXECUTAR A PINTURA')
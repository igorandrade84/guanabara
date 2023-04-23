# Escreva um programa que pergunte a quantidade de Km percorridos por um carro 
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
# a pagar. Sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.


n1 = float(input('Km percorridos: '))
n2 = int(input('Dias alugado: '))
a = n1
b = n2
c = a * 0.15
d = b * 60
e = c + d
print(f'O VALOR TOTAL É {e:.2f}, SENDO KM PERCORRIDOS R$ {c:.2f} e DIAS ALUGADO R$ {d:.2f}')
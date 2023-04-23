# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto..

n1 = float(input('DIGITE AQUI O VALOR DO PRODUTO:'))
a = n1
b = (a * 5/100)
c = a-b
print(f' O VALOR DO PRODUTO É{a:.2f} reais MAS COM 5% DE DESCONTO O VALOR FINAL É DE = {c:.2f} reais')



# valor * % / 100
# preço - (preço - 5/100)
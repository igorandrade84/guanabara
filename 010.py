# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar
# U$$1.00=R$3.27 (2018)
# U$$1.00=R$5.05 (2023)
# EUR1.00=R$5.60 (2023)

n1 = float(input('COLOQUE O VALOR EM REAIS A SER CONVERTIDO EM DÓLAR(2018), DÓLAR(2023) e EURO (2023): R$'))
a = n1 
b = a/3.27
c = a/5.05
d = a/5.60
print(f'O VALOR de R${a:.2f} CONVERTIDO EM DÓLARES(2018) É U$${b:.2f}, DÓLAR (2023) É {c:.2F} E EURO (2023) É {d:.2f}')


# Descobrir como não ter tantas casas após a vírgula e aplicar?
# :.2f = esse f é de float. no caso quero 02 casas após a vírgula
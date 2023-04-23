# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimétros


medida = float(input('DIGITE O VALOR A SER CONVERTIDO: '))
a = medida 
dm = a * 10
cm = a * 100
mm = a * 1000
dam = a / 10
hm = a /100
km = a / 1000
print(f'O VALOR {a}m CONVERTIDO: {dm} DM  {cm} CM  {mm} MM  \b {dam} DAM  {hm} HM {km} KM')



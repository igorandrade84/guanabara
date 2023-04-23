# Crie um programa que converta uma temperatura digitada em °C e a converta para °F

temp = float(input('TEMPERATURA °C: '))
a = temp
b = 9 * a / 5 + 32
c = a + 273
print(f'{a:.2f}°C equivale a {b:.2f} °F e {c:.2f} °K')
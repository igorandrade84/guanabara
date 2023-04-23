# Faça um programa que leia algo pelo teclado e mostre em tela seu tipo primitivo
# e todas as informações possíveis sobre ela.
# a é o objeto ####
# type(variável) mostra o tipo primitivo da variável;
# a.isspace() mostra se so há espaços vazios;
# a.isnumeric() mostra se é um núemro;
# a.isalpha() mostra se é alfabético o que foi escrito
# a.isalnum mostra se é alfa numérico

a = input ("Digite qualquer coisa:")
print('O tipo primitivo desse valor é: ', type(a))
print ('só tem espaços? ', a.isspace())
print ('É um nuḿero?', a.isnumeric())
print('É alfabético? ', a.isalpha())
print ('É alfa numérico?', a.isalnum() )
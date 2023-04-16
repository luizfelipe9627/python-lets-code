
#* > Operações matemáticas(Aritméticas).

"""
  - Soma: "+".
  - Subtração: "-".
  - Multiplicação: "*".
  - Divisão: "/".
  - Divisão inteira: "//".
  - Resto de divisão: "%".
  - Potência: "**".
"""

num1 = 10; # Variável chamada num1 contendo um número inteiro.
num2 = 20; # Variável chamada num2 contendo um número inteiro.

print(num1 + num2); # Irá imprimir na tela o num1 somado com o num2.
print(num1 - num2); # Irá imprimir na tela o num1 subtraído pelo o num2.
print(num1 * num2); # Irá imprimir na tela o num1 multiplicado pelo o num2.
print(num1 / num2); # Irá imprimir na tela o num1 dividido pelo o num2, retornando tanto número inteiro quanto decimal.
print(num1 // num2); # # Irá imprimir na tela o num1 dividido pelo o num2, retornando apenas número inteiro.
print(20 % 3); # Irá imprimir na tela o resto da divisão de 20 dividido por 3.
print(2 ** 3); # Irá imprimir na tela 2 exponenciado por 3.

#* > Operações lógicos(Boolean).

age1 = 10; # Variável chamada age1 contendo um número inteiro.
age2 = 15; # Variável chamada age1 contendo um número inteiro.
fall1 = 1.77; # Variável chamada fall1 contendo um número quebrado.
fall2 = 1.65; # Variável chamada fall2 contendo um número quebrado.
fall3 = fall2; # Variável chamada fall3 contendo o valor da variável fall2.

print(age1 > age2); # Irá imprimir False na tela pois 10(age1) não é maior que 15(age2).
print(age1 <= age2); # Irá imprimir True na tela pois 10(age1) é maior(mas não igual) que 15(age2).
print('Python' == 'python'); # Irá imprimir False na tela pois Python não é igual ao python por conta da letra minuscula.
print('banana' != 'abacaxi'); # Irá imprimir True na tela pois banana é diferente de abacaxi.
print(fall1 >= fall2); # Irá imprimir True na tela pois 1.77(fall1) é maior(não igual) que 1.65(fall2).
print(fall2 > fall3); # Irá imprimir False na tela pois 1.65(fall2) não é maior que 1.65(fall3).
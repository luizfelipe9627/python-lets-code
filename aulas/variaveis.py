
#* > Variáveis.

"""
  Tipos de variáveis:

  1. init -> Números inteiros, sendo assim, números sem parte decimal como: 0, 5, -1, 1000.
  2. float -> Números reais, sendo assim, números com parte decimal como: 1.0, -2.7, 3.14.
  3. stf -> Cadeias de caracteres, sendo assim, dados textuais(string).
  4. bool -> Valores lógicos booleans como: True ou False.
"""

age = 19; # Cria uma variável chamada age que recebe o valor 19(number init).
print(age); # Imprimi na tela o valor armazenado na variável na tela.
print(type(age)); # Imprimi na tela o tipo de valor armazenado na variável.

tall = 1.75; # Cria uma variável chamada tall que recebe o valor 1.70(number float).
print(tall); # Imprimi na tela o valor armazenada na variável na tela.
print(type(tall)); # Imprimi na tela o tipo de valor armazenado na variável.

name = 'Luiz Felipe'; # Cria uma variável chamada name que recebe um texto(string/stf).
print(name); # Imprimi na tela a string armazenada na variável na tela.
print(type(name)); # Imprimi na tela o tipo de valor armazenado na variável.

study = True; # Cria uma variável chamada study que recebe um valor lógico(boolean/bool).
print(study); # Imprimi na tela o valor armazenada na variável na tela.
print(type(study)); # Imprimi na tela o tipo de valor armazenado na variável.

#* Usando o print para imprimir diversos valores.

print(name, age, study) # Para imprimir na tela o valor de várias variáveis é somente separar por uma virgula(",") e colocar a próxima. 

#* Obtendo dados do usuário e salvando em variáveis.

language = input('Qual é a linguagem de programação que você está estudando? '); # A variável language recebe o input que é um método usado para receber uma entrada de dado, sendo assim irá pegar a resposta do usuário e armazenar na variável.
print('A linguagem que você está estudando é:', language); # Imprimi na tela a string e em seguida a resposta do usuário.
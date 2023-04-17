
#* > Estruturas condicionais IF, ELSE e ELIF.

"""
  Faça uma condição na qual verifique se o usuário é maior ou menor de idade.
"""

#* > If e else.

age = 10; # Variável com o nome age recebendo um number.

# Se age(o valor armazenado) for maior(>) ou igual(=) a 18 irá executar o if.
if age >= 18:
  print("Você é maior de idade."); # Imprime na tela uma string.
# Senão irá executar o else.
else:
  print("Você é menor de idade."); # Imprime na tela uma string.

"""
  Imagine que você queira imprimir "Aprovado(o)", caso o estudante tenha uma média superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
"""

#* > If, elif e else.

media = float(input("Informe a média: ")); # Variável media que converte o valor digitado pelo usuário no input em número quebrado.

# Se media(o valor armazenado) for maior(>) ou igual(=) a 7 irá executar o if.
if media >= 7:
  print("Você foi aprovado."); # Imprime na tela uma string.
# Senão se media for(o valor armazenado) for maior(>) ou igual(=) a 5 irá executar o elif(else if).
elif media >= 5:
  print("Você foi para recuperação."); # Imprime na tela uma string.
# Senão caso as condicionais anteriores sejam falsas irá executar o else.
else:
  print("Você foi reprovado."); # Imprime na tela uma string.
 
grade = 9; # Variável com o nome grade recebendo um number.
presence = 50; # Variável com o nome presence recebendo um number.

#* > If e else com operador AND.

# Se grade(o valor armazenado) for maior(>) ou igual(=) a 7 E(os dois tem que ser verdadeiro) presence for maior ou igual a 70 irá executar o if.
if grade >= 7 and presence >= 70:
  print("Aprovado!"); # Imprime na tela uma string.
# Senão caso contrario irá executar o else.
else:
  print("Reprovado!"); # Imprime na tela uma string.
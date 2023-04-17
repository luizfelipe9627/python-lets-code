
#* > Laço de repetição FOR.

"""
  Os números sempre começam a partir do 0, sendo assim nunca chegara ao número desejado se não for acrescentado sempre 1 número a mais.
"""

# O range pode receber até 3 parâmetros. Quando ele recebe apenas 1 ele irá executar até chegar no valor atribuído. 
# Para um_parametro(nome criado para a variável) aplique uma faixa(repetição) de 10 loops.
for um_parametro in range(5):
  print(um_parametro)

# Quando é 2 parâmetros o primeiro é da onde o contador vai começar e o segundo em qual número ele irá finalizar o loop.
# Para dois_parametros(nome criado para a variável) aplique uma faixa(repetição) do número 10 até o 15.
for dois_parametros in range(10, 15):
  print(dois_parametros);

# Quando é 3 parâmetros o primeiro é da onde o contador vai começar e o segundo em qual número ele irá finalizar o loop e o terceiro é quantos números ele irá pular a cada loop.
# Para tres_parametros(nome criado para a variável) aplique uma faixa(repetição) do número 20 até o 30, pulando de 5 em 5.
for tres_parametros in range(5, 30, 4):
  print(tres_parametros);

#* Usando o FOR na prática.

# Uma solução que seria usada sem o FOR, mas que se tornaria mais extensa:
# grade1 = float(input('Informe sua 1° nota: '));
# grade2 = float(input('Informe sua 2° nota: '));
# grade3 = float(input('Informe sua 3° nota: '));

sum = 0; # Criado uma variável contadora chamada sum, que recebe um valor número neutro.

# Para i(variável de armazenamento) aplica uma repetição do número 1 até o 4(3 no caso pois começa do 0).
for i in range(1, 4):
  # Usamos o "f" antes da string para permitir que seja injetado uma variável dentro de uma string utilizando os "{}".
  grade = float(input(f'Informe sua {i}° nota: ')); # A variável grade recebe número quebrado e dentro dele o input que é um método usado para receber uma entrada de dado, sendo assim irá pegar a resposta do usuário e armazenar na variável e repetir até terminar o for.
  sum = sum + grade; # Reescreve a soma para somar o seu valor(já armazenado) mais o valor da nota dada pelo usuário a cada loop.
print(sum / 3); # Imprime na tela a soma do total das notas dividido por 3, para mostrar a média.
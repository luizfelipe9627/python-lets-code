
#* > Laço de repetição WHILE.

numero_sorteado = 15; # Criado uma variável chamada numero_sorteado que contém um number como seu valor.

numero_escolhido = int(input('Informe um número entre 1 e 20: ')); # A variável numero_escolhido recebe número inteiro e dentro dele o input que é um método usado para receber uma entrada de dado, sendo assim irá pegar a resposta do usuário e armazenar na variável.

#* O if, else ou elif executa apenas uma vez.

# Se numero_sorteado(o valor armazenado) for igual a numero_escolhido irá executar o if.
if numero_sorteado == numero_escolhido:
  print('Esse foi o número sorteado, boa!'); # Imprime na tela uma string.
# Senão caso contrario irá executar o else.
else:
  print('Infelizmente você errou.)'); # Imprime na tela uma string.

#* Diferente do while que executa diversas vezes.

# Enquanto numero_escolhido for diferente do numero_sorteado irá executar o while.
while numero_escolhido != numero_sorteado:
  print('Você errou, por favor tente novamente.'); # Imprime na tela uma string.

  numero_escolhido = int(input('Informe um número entre 1 e 20: ')); # A variável numero_escolhido recebe número inteiro e dentro dele o input que é um método usado para receber uma entrada de dado, sendo assim irá pegar a resposta do usuário e armazenar na variável.
print('Você acertou, parabéns!'); # Caso saia do loop do while imprime a string na tela.

#* Podemos fazer o while executar conforme um contador.

counter = 0; # Criado uma variável chamada counter que contém um number como seu valor.

# Enquanto counter for menor do que 5 irá executar o while.
while counter < 5:
  print(counter); # Irá imprimir o número atual do contador na tela.
  counter = counter + 1; # Reescreve a variável recebendo 1 número a mais a cada loop.
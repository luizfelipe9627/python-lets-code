
#* Introdução a funções.

# Funções que já utilizamos anteriormente:
# print(); # - Imprimi uma mensagem (int, float, str) no console (terminal, cmd).
# input(); # - Retorna um dado informado pelo usuário(entrada padrão) e pode receber uma string usada para se comunicar com o usuário.
# len(); # - Recebe uma lista e retorna o tamanho da lista.
# max(); # - Retorna o maior valor de uma lista. 

#* > Criação de função.

# Para cria uma função usamos a palavra reservada def e o nome da função fechado com "()".
def greeting():
  print('Olá, tudo bem?'); # Imprimi uma string na tela.
  print('Eu espero que sim :)'); # Imprimi uma string na tela.

greeting(); # Executa a função criada.

#* > Função com parâmetros.

# Para criar parâmetros é so definir o nome do dado dentro dos parenteses da função.
def greeting(name, course):
  # Usamos o "f" antes da string para permitir que seja injetado uma variável/parâmetro dentro da string utilizando os "{}".
  print(f'Seja bem vindo(a), {name}!'); # Imprimi uma string na tela.
  print(f'Fico feliz em ter você por aqui no curso de {course}.'); # Imprimi uma string na tela.

greeting('Luiz', 'Python'); # Executa a função criada, atribuindo/armazenando o valor digitado dentro do parâmetro da função.

#* > Função com parâmetros default.

# Podemos definir um parâmetro default atribuindo um valor a ele dentro dos "()" da função.
def greeting(name, course = 'JavaScript'):
  # Usamos o "f" antes da string para permitir que seja injetado uma variável/parâmetro dentro da string utilizando os "{}".
  print(f'Seja bem vindo(a), {name}!'); # Imprimi uma string na tela.
  print(f'Fico feliz em ter você por aqui no curso de {course}.'); # Imprimi uma string na tela.

greeting('Felipe'); # Executa a função criada, atribuindo/armazenando o valor digitado dentro do parâmetro da função.
greeting('Felipe', 'React'); # Executa a função criada, e caso não queira o parâmetro default podemos definir um novo valor.

#* > Função com retorno.

# Criado uma função chamada sum, que recebe dois parâmetros.
def sum(num1, num2):
  return num1 + num2; # O return é uma palavra reservada usada para retornar algo e após isso finalizar a função(sendo assim nada abaixo do return vai ser executado).

result = sum(5, 10); # Está definindo valores aos parâmetros da função e armazenando na variável chamada result.
print('O resultado da soma é:', result); # Imprimi na tela uma string e o resultado da soma.

#* > Exemplo utilizando função.

# Criado uma função chamada calculator, que recebe três parâmetros, sendo uma delas um parâmetro default.
def calculator(num1, num2, operator = '+'):
  # Se o operador for igual ao de soma(+) irá executar o if.
  if(operator == '+'):
    return num1 + num2; # Retorna a soma entre os números.
  # Senão se o operador for igual ao de subtração(-) irá executar o elif.
  elif(operator == '-'):
    return num1 - num2; # Retorna a subtração entre os números.
  # Senão se o operador for igual ao de multiplicação(*) irá executar o elif.
  elif(operator == '*'):
    return num1 * num2; # Retorna a multiplicação entre os números.
  # Senão se o operador for igual ao de divisão(/) irá executar o elif.
  elif(operator == '/'):
    return num1 / num2; # Retorna a divisão entre os números.
  
result = calculator(30, 15, '-'); # Está definindo valores aos parâmetros da função e armazenando na variável chamada result.
print(result); # Imprimi na tela o resultado armazenado na variável.
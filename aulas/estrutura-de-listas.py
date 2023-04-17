
#* > Estrutura de listas.

# Antes:
grade1 = 7.9;
grade2 = 9.7;
grade3 = 8.2;

# Utilizando lista:
grades = [7.9, 9.7, 8.2]; # Para criar uma estrutura de dados(uma lista de variáveis) em uma variável apenas utilizamos os "[]", separando cada um com ",".

# Criando listas:
list = list(); # O list é usado para criar uma lista vazia.
list = []; # Para criar uma lista vazia podemos adicionar os "[]" sem valores.
list = [26, 'Luiz', 3.145, False]; # Uma lista aceita vários tipos de valores.
list_of_lists = [10, [1, 2, 3]]; # Podemos criar uma nova lista dentro de uma lista.

# Indexação e slices(fatiamento):
list = [19, 'Luiz', 1.076]; # Uma lista contendo vários tipos de valores.

print(list[-1]); # Mostra na tela o último elemento presente no list.
print(list[-2]); # Mostra na tela o penúltimo elemento presente no list.
print(list[-3]); # Mostra na tela o antepenúltimo elemento presente no list.
print(list[0]); # Mostra na tela o elemento da posição 0 presente no list.
print(list[1]); # Mostra na tela o elemento da posição 1 presente no list.
print(list[2]); # Mostra na tela o elemento da posição 2 presente no list.

# Slices:
list = [10, 50, 30, 40, 25, 60, 5]; # Criado uma lista contendo 7 valores.

print(list[0:2]); # Imprime na tela o elemento do index 0 até 2(menor que 2, sendo assim até 1) da list.
print(list[4:]) # Imprime do elemento 4 até o final.
print(list[2:6:2]); # Imprime do elemento 2 até o 6(menor que 6, sendo assim até 5) pulando de 2 em 2.

#* > Iterações utilizando o FOR e Listas.

# Utilizando os próprios elementos da lista:

# Para cada element da lista percorre a lista assim executando o for a cada elemento da lista.
for element in list:
  print(element); # Imprimi na tela cada elemento(da lista).

# Utilizando os índices:

print('Quantidade de elementos da lista:', len(list)) # O len() é um método usado para contar quantos elementos há em uma lista.

# Para cada index(i) o range pega a quantidade(como o número 7) de elementos presente na lista através do método len.
for i in range(len(list)):
  print(i); # Imprime na lista a quantidade de elementos presente na lista 1 por 1.
  print(list[i]); # Imprime na lista o valor presente em cada elemento na lista 1 por 1.

#* > Métodos de listas.

# append()
print('----------------------------------------------------------------------------');
print('Antes do append: ', list); # Mostra na tela a string junto com a lista.
list.append(3); # O append é um método usado para adicionar um elemento ao final da lista.
print('Depois do append: ', list); # Mostra na tela a string junto com a lista.

# insert()
print('----------------------------------------------------------------------------');
print('Antes do insert: ', list); # Mostra na tela a string junto com a lista.
list.insert(2, 10); # O insert é um método usado para adicionar um elemento na posição desejada na lista. Recebe dois parâmetros, sendo o primeiro o índice que vai ser criado o elemento, e o segundo o elemento que vai ser inserido.
print('Depois do insert: ', list); # Mostra na tela a string junto com a lista.

# extend()
print('----------------------------------------------------------------------------');
list2 = [1, 1, 2, 3];

print('Antes do extend: ', list); # Mostra na tela a string junto com a lista.
list.extend(list2); # O extend é um método usado para juntar/concatenar duas listas em uma, adicionando os elemento da nova lista no final.
print('Depois do extend: ', list); # Mostra na tela a string junto com a lista.

# pop()
print('----------------------------------------------------------------------------');
print('Antes do pop: ', list); # Mostra na tela a string junto com a lista.
# O pop é um método usado remover o último elemento(caso não informe a posição), ou remover o elemento desejado informando o index dele.
list.pop(); # Tira o último elemento da lista.
print('Depois do pop: ', list); # Mostra na tela a string junto com a lista.
list.pop(0) # Tira o elemento de index 0 da lista.
print('Depois do pop: ', list); # Mostra na tela a string junto com a lista.

# remove()
print('----------------------------------------------------------------------------');
print('Antes do remove: ', list); # Mostra na tela a string junto com a lista.
list.remove(2); # O remove é um método usado remover um elemento através do valor definido na lista e não pelo seu index. Ele pega o primeiro que ele encontrar e não todos(por exemplo tem quatro 2, ele tira somente o primeiro 2 que ele encontrar).
print('Depois do remove: ', list); # Mostra na tela a string junto com a lista.

# count()
print('----------------------------------------------------------------------------');
print('A lista atual é: ', list); # Mostra na tela a string.
# O count é um método usado contar quantas vezes tal valor aparece na lista.
print('Quantidade de 1 na lista: ', list.count(1)); # Mostra na tela a string junto com a quantidade de elementos repetidos.

# index()
print('----------------------------------------------------------------------------');
print('A lista atual é: ', list); # Mostra na tela a string e a lista.
# O index é um método usado para localizar o retornar a posição de um index da lista.
print('Índice do elemento 10: ', list.index(10)); # Mostra na tela a string junto com a posição do elemento com valor 10 da lista.

# sort()
print('----------------------------------------------------------------------------');
print('Antes do sort ordenado: ', list); # Mostra na tela a string junto com a lista.
list.sort(); # O sort é um método usado para ordenar uma lista do menor para o maior.
print('Depois do sort ordenado: ', list); # Mostra na tela a string e a lista.

print('Antes do sort reverso: ', list); # Mostra na tela a string junto com a lista.
list.sort(reverse=True); # O sort é um método usado para ordenar uma lista do menor para o maior, nesse caso estamos fazendo o reverso.
print('Depois do sort reverso: ', list); # Mostra na tela a string e a lista.

#* > Funções para listas

# len
print('----------------------------------------------------------------------------');
# O len é um método usado para informar quantos elementos há em uma lista.
print('Utilizando o len há isso de elementos na lista:', len(list)); # Mostra na tela a string e a quantidade de elemento lista.

# sum
print('----------------------------------------------------------------------------');
# O sum é um método usado para somar.
print('Somando cada elemento da lista temos:', sum(list)); # Mostra na tela a string e o total da soma da lista.

# max
print('----------------------------------------------------------------------------');
# O max é um método usado para retornar o maior valor da lista.
print('O maior valor/número da lista é:', max(list)); # Mostra na tela a string e o maior valor da lista.

# min
print('----------------------------------------------------------------------------');
# O min é um método usado para retornar o menor valor da lista.
print('O menor valor/número da lista é:', min(list)); # Mostra na tela a string e o menor valor da lista.
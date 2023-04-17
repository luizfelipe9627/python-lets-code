
#* > Dicionários.

# Criando dicionários.
dictionary = {}; # Variável chamada lista, que armazena um dicionário. Para criar um dicionário vazio usamos as chaves({}).
dictionary = dict(); # Ou podemos criar um dicionário vazio utilizando o método dict().

print('----------------------------------------------------------------------------');
# Está criando elementos para um dicionário.
dictionary = {
  'nome': 'Luiz',
  'idade': 19,
  'altura': 1.70,
}
print(dictionary); # Imprimi na tela o dicionário.
print('O valor presente no elemento idade é:', dictionary['idade']); # Imprimi na tela o elemento idade que está dentro do dicionário.

# Adicionando elementos em um dicionário.
print('----------------------------------------------------------------------------');
dictionary['cidade'] = 'São Paulo'; # Caso um elemento não exista podemos adicionar um novo elemento no dicionário passando entre "[]" o nome e depois atribuindo o valor através do igual.
print(dictionary); # Imprimi na tela o dicionario com o elemento novo.

# Sobrescrever elemento de um dicionário.
print('----------------------------------------------------------------------------');
dictionary['nome'] = 'Felipe' # Caso o elemento já exista(nesse caso existe) ele sobrescreve e atualiza o valor para o definido recentemente.
print(dictionary);

# Iterando sobre um dicionário.
print('----------------------------------------------------------------------------');
# O key é a variável que vai percorrer por todo o dicionário presente no for.
for key in dictionary:
  print(key); # Imprimi na tela as chaves do dicionário por padrão.
  print(dictionary[key]) # Imprimi na tela os valores do dicionário. 

# Testando a existência de uma chave.
print('----------------------------------------------------------------------------');
# Para sabermos se existe um elemento no dicionário pegamos o nome e depois coloca in dicionary, assim ele irá retornar true ou false.
print('peso' in dictionary) # Imprimi False na tela.
print('nome' in dictionary) # Imprimi True na tela.
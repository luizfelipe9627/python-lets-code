
#* > Conversão de tipos.

age = '19';
num1 = '10';
num2 = '20';

print(num1 + num2); # Imprimi na tela os valores concatenados pois são do tipo string e não do tipo number.

#* > Conversão de string para int().

idade_inteira = int(age); # Pega a variável age e de string converte ela para number int.
print(idade_inteira, type(idade_inteira)); # Imprimi na tela o valor do age transformado em um número inteiro, em seguida mostra o tipo da variável idade_inteira.

#* > Converter o input(que por padrão é string) para float().

fall = float(input('Informe a sua altura: ')); # A variável fall recebe o float que é para transformar de string(padrão do input) para number, já o input que é um método usado para receber uma entrada de dado, sendo assim irá pegar a resposta do usuário e armazenar na variável.
print(fall, type(fall)); # Imprime a resposta do usuário e o tipo da variável.

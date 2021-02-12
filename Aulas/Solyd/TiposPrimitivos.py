nome = input("Digite seu nome: ") #variavel input usada pra receber dados
cpf = int(input("Digite seu cpf: "))
endereco = input("Digite seu endereco: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")
telefone = input("Digite seu telefone: ")
me = 100 # testando passagem de tipo de um numero inteiro escrito fora da entrada

# a função str() pode ser usada para converter dados de entrada em uma string.
# a função int() pode ser usada para converter dados de entrada para um número inteiro.
# a função float() pode ser usada para converter dados de entrada para um número real.
#Observe que algumas funções não devem ser concatenadas juntas, str + int na mesma linha nao cola
# Pra resolver isso passamos o int na variavel de entrada no caso cpf. Mesmo com a str no print o type exibe int para cpf


print ('Nome: ','"',nome+'"', ' de cpf ', '"'+str(cpf)+'"', '\n' 'mora em ', '"'+str(endereco)+'"',  ' tem ', '"'+str(idade)+'"', ' anos, mede ', '"'+str(altura)+'"', ' e seu número é ', '"'+str(telefone)+'"')

# a função type() pode ser usada para especificar o tipo de dado que uma variavel esta recebendo.

print (me, type(me), type(nome), type(cpf), type(endereco), type(idade), type(altura), type(telefone))

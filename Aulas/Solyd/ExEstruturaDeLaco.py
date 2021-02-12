'''
EXERCICIO: FaÃ§a um programa que leia a quantidade de pessoas que
serao convidadas para uma festa.
ApÃ³s isso o programa irÃ¡ perguntar o nome de todas as pessoas e
colocar numa lista de convidados
ApÃ³s isso irÃ¡ imprimir todos os nomes da lista
'''
print('Programinha de controle de festinhas 1.0')
print('########################################')

numero_de_convidados = input('Coloque o numero de convidados: ')
lista_de_convidados = []

i = 1 # i recebe o valor de 1
while i <= int(numero_de_convidados): #enquanto i for <= numero de covidados (repita o seguinte)
    nome_do_convidado = input('Coloque o nome do convidado #'+ str(i) +': ') #anote entradas em nome_do_convidado e concatene com i(1)
    lista_de_convidados.append(nome_do_convidado) #inclua o nome_do_convidado em lista_de_convidados
    i += 1 #incremente 1 a variavel i, #Toda vez que a stack chegar no final desse laço o valor de i é somado a 1.

print('Serão', numero_de_convidados, 'convidados') #seguindo o fluxo ja fora do laço exiba...

print('\nLISTA DE CONVIDADOS') #exiba a lista de convidados
for convidado in lista_de_convidados:  #Para convidado armazene o que estiver dentro de lista_de_convidados
    print(convidado)        #exiba o que estiver dentro do apelido de lista de convidados.

#nesse programa a variavel i assume um papel determinante, ela aparece sendo concatenada dentro do laço
#porque desta forma input consegue ler o valor atual dela a cada vez que um novo convidado é digitado.

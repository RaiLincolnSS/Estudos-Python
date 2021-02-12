#Class
#Syntaxe

#altura, cor_da_pele, idade

class Pessoa:
    def __init__(self, altura, cor_da_pele, idade):
        self.altura = altura
        self.cor_da_pele = cor_da_pele
        self.idade = idade

    def idioma(self):
        return 'inglês'

bruna = Pessoa('152', 'branca', '28')
rafael = Pessoa('180', 'moreno', '24')
anao = Pessoa('100', 'branca', '18')
print(f'{bruna.altura} {bruna.cor_da_pele} {bruna.idade} {bruna.idioma()}')
print(rafael.altura,rafael.cor_da_pele,rafael.idade)
print(anao.altura,anao.cor_da_pele,anao.idade)
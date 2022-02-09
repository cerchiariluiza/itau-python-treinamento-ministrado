paises = {'BRA': 'Brasil', 'ESP': 'Espanha', 'EUA': 'Estados Unidos', 'FRA': 'França'}
print("Exemplo de dicionário: ", paises)

for chave, valor in paises.items():
    if chave == 'BRA':
        print(chave + " =>>>> " + str(valor))


for chave in paises.keys():
    print(chave)


for values in paises.values():
    print(values)

paises.pop('ESP')
print(paises)

paises['ESP'] = 'Spanish'
print(paises)

paises.update({'ESP':'Span'})
print(paises)
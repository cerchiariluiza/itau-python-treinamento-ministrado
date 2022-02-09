lista_simples_inteiro = [1, 2, 3, 8, 14, 4, 5]
print(lista_simples_inteiro)

# Append()
lista_simples_inteiro.append(6)
print(lista_simples_inteiro)

# Insert()                  pos valor
lista_simples_inteiro.insert(0, 200)
print(lista_simples_inteiro)
print(len(lista_simples_inteiro))

# Remove()
lista_simples_inteiro.remove(2)
print(lista_simples_inteiro)
#fatiamento
lista_simples_inteiro = [1, 2, 3, 8, 14, 4, 5]
print(lista_simples_inteiro[0:4]) # Cortar lista da posição 0 a 4 (sem incluir a 4)
print(lista_simples_inteiro[3:]) # Cortar lista da posição 3 em diante
print(lista_simples_inteiro[:3]) # Cortar lista do início até a posição 3 (sem incluir a 3)
nova_lista = lista_simples_inteiro[:3] # Criar uma nova lista com base no corte de outra lista
print(nova_lista)

#exemplos de listas ()
def variaveis_locais():
    lista = ['Julia','Marcelo','Gabriela']
    if 'Julio' in lista:
        print('existe')
    else:
        print('Não existe')
    print(type(lista))
    print(lista[0])
variaveis_locais()
#print(lista[0])

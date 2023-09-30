lista = ['frutas', 'pao', 'carne', 'arroz', 'biscoito', 'macarrao']
#print('hoje eu vou comprar:', lista)

lista.append('feijao')
#print(lista)

lista.sort()
print('lista organizada:', lista)

#tirando o biscoito
lista.remove('biscoito')
print('lista sem o elemento removido:', lista)

#indicar o 3 elemento da lista
print('o 3 elemento eh:', lista[2])

#indicar o ultimo elemento
print('o ultimo elemento eh:', lista[-1])

#remover o 4 elemento
print('o 4 elemento removido foi:', lista.pop(4))

#exibir os 3 primeiros
print('os 3 primeiros elementos:', lista[0:3])

#PYTHON LISTAS DOCUMENTO

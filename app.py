

# removendo item da lsita
print(f'Lista antes de remover {lista}')

# pop - remove pelo indice
lista.pop(0)

print(f'Lista depois de remover {lista}')

# removendo o ultimo indice
lista.pop()

# removendo pelo valor, (remove a primeira ocorrencia)
lista.remove('cicrano')

lista_numeros = [n for n in  range(1,11)]

# removendo intervalo de valores
del lista[2:4]

print(f'Lista depois de remover {lista}')

listanomes = ['gomes','fulando','cicrano','beltrano','maria','pedro']
# alterando valor de lista

listanomes[1] = 'lucas'

print(listanomes)

numeros = ['1,2,3,4,5,6,7,8,9,10']
for i in range(len(numeros)):
    if numeros[1] > 10:
        numeros[1] = numeros[1] * 2
print(numeros)





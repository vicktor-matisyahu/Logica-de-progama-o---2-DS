'''
1. Crie um programa que o usuario possa digitar quantos numeros quiser
e ao terminar imprima a lista em ordem crescente.

'''

print('------ LISTA DE NÚMEROS ------')

lista_numeros = []

while True:
    numero = input("Digite um numero: ")
    numero = float(numero)
    lista_numeros.append(numero)
    print(lista_numeros)

    quebra = input("Deseja adicionar mais numero?(Enter - continua | n - Não)").lower()

    if quebra == "n":
        lista_numeros.sort()
        print(lista_numeros)
        break
    



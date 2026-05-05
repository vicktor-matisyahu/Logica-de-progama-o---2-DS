'''
2. Crie um programa que o usuario possa digitar a quantidade desejada de notas
de um determinado aluno (nota minima 0 e nota maxima 10) e o programa calcula
a media desse aluno, e ao final imprima se o aluno esta (aprovado =>7, reprovado 
recuperação >= 5)
'''

import os

os.system("cls")

print('--- Boletim Escolar ---')

lista_notas = []
mini = 1
maxi = 10

while True:
    nota = input(float(f'Digite um numero entre {mini} e {maxi}'))
    if nota >= mini <= maxi :
        print('Nota válida!!')
    else:
        print('Nota Inválida!!')
        break
    nota = float(nota)
    lista_notas.append(nota)
    print(lista_notas)

    opcao = input("Deseja adicionar mais notas?(Enter - continua | n - Não)").lower()

    if opcao == "n":
        break
    
media = sum(lista_notas) / len(lista_notas)

if media >= 7:
    print('O aluno está aprovado!!')

elif media <= 5:
    print('O aluno está reprovado!!')

else: 
    print('O aluno está de recuperação!!')


    
   

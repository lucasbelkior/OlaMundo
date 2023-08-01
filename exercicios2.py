'''
Fazer um programa que pergunte um numero inteiro e apresenta ao usario
o antecessor e o sucessor do numero informado
'''

nome = input("Qual é o seu nome?")
print("Ola,",nome,"tudo bem com voce?")

num = int(input("Informe um numero inteiro:"))
ant = num - 1
suc = num + 1

print("O antecessor é",ant,"O sucessor é",suc)


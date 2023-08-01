'''
Elabore um programa que pergunte ao aluno suas 3 notas escolares.
o programa devera calcular a media das 3 notas inseridas e
exibir esta media
'''

# Etapa 1: entrada de dados
nota1 = float(input("Informe a sua nota 1:"))
nota2 = float(input("Informe a sua nota 2:"))
nota3 = float(input("Informe a sua nota 3:"))

# Etapa 2: processamento de dados
media = (nota1 + nota2 + nota3) / 3

# Etapa 3: Saida de dados (resposta na tela do usuario
print("Sua media é", media)

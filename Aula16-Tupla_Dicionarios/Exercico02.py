#Construa um algoritmo que peça ao usuário para 
# informar o nome, a nota01 e a nota02 de um 
# aluno. Guarde estas informações em um 
# dicionário. Após, calcule a nota final deste 
# aluno [(nota01 + nota02) /2] e adicione 
# ao dicionário. Ao final, imprima todos os 
# dados do dicionário.

nome = input("Digite o nome: ")
nota01 = int( input("Digite a nota 01: "))
nota02 = int( input("Digite a nota 02: "))
aluno = { 
    "nome": nome, 
    "nota01": nota01 , 
    "nota02": nota02 
    }
nf = (nota01 + nota02) / 2
aluno["notaFinal"] = nf
print( aluno )
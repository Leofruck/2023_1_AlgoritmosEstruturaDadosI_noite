#Construa um algoritmo que possua uma tupla com os números escritos
#por extenso de “zero” a “nove”. Peça ao usuário para digitar um número
#de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas
#condicionais (if e switch).

numeros = "Zero", "Um", "Dois", "Três", "Quadro", "Cinco", "Seis", "Sete", "Oito", "Nove"
valor = int( input("Digite um número de 0 a 3: ") )
print( str(valor), "por extenso é: " , str(numeros[valor]) )
filho1 = { "nome":"Júlia" , "idade": 14}
filho2 = { "nome":"Carlos" , "idade" : 10}

print( filho1 )
print( "Nome: " + filho1["nome"])
print( filho1.keys() )

for chave, valor in filho1.items():
    print( chave, " - ", valor)

for chave in filho1.keys():
    print( chave, " - ", filho1[chave])

filho3 = { "nome":"Maria" , "idade" : 5}
filhos = filho1 , filho2
print( filhos )
#filhos[0] = filho3
filho1["nome"] = "Maria"
print( filhos )

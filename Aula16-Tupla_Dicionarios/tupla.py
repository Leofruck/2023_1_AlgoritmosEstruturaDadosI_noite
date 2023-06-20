jogadores = "João" , "Maria", "Júlia", "Suzy", "José"
print("-------------")
print( jogadores )
print("-------------")
print( jogadores[1]  )
print( jogadores[1:3]  )
print( jogadores[1:-1]  )
print( jogadores[:-2]  )

def calcular(x, y):
    return x+y , x-y , x*y , x/y

result = calcular(10 , 5 )
a, b, c, d = calcular(10 , 5 )
#e, f = calcular(10 , 5 )
print( result )
print( "Soma: " + str( a ) )
print( "Multiplicação: " + str( c ) )
#print( e )
#print( f )

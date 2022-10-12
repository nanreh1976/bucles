# While 

# se usa sin saber cuantas veces hay que repetir el bucle

num = 10

while num != 0 : 
    print(" su numero : ", num)
    num = int(input(" Ingrese un numero : "))
print("fin del programa while")

# For

# se usa sabiendo la cantidad de veces que queres repetir un bucle de antemano

for i in "hernanchogomez@gmail.com" : #repite la secuencia de los char que estan entre ""
    print(i)

for i in range (1,11) : #repite la secuencia de i=a hasta i=10
    print ("hola n1 : ", i)
else :
    print ("secuencia recorrida")
print ("fin del programa for-range")        

# Break

for letra in " Hola" : # repite la secuencia de los char hasta que if == a rompe el for
    print (letra)
    if letra == "a" :
        break

print ("fin del programa for-break")


# Continuo

for letra in " Hola" : # repite la secuencia de los char hasta que if == a continua
    print (letra)
    if letra == "a" :
        continue
        print("fin del bucle")
    else :
        print ("Secuencia recorrida")

print (" fin del programa for-continue")


print ("fin del programa ")

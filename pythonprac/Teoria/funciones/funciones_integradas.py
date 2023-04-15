numeros = [4, 6 , 2 , 5 , 7]

#Econtrando el numero max y el min

print("---------------------MAX Y MIN------------------------")
numero_alto = max(numeros)
print(f" su numero mayor es: {numero_alto}")

numero_bajo = min(numeros)
print(f"Su numero bajo es: {numero_bajo}")


print("---------------------ROUND------------------------------")
#Round sirve para redondear numeros y sacarle decimales

nume = round(12.456789,2)
nume2 = round(45.247796214456)
print(nume2)
print(nume)


print("----------------BOOL y ALL------------------")

#Bool devuelve True si el dato es distinto de 0

ejem = (4, 6 ,8, "Holaa" )
ejem2= ("")
ejem3=all(("hola",0,123))



print(bool(ejem))
print(bool(ejem2))

#ALL retorna true si los valores son verdaderos
print(all(ejem2))
print(ejem3)


print("------------------------SUM-----------------------------")

#suma todos los numeros

a = 44, 6 , 8, 9 , 10,3
print(sum(a))



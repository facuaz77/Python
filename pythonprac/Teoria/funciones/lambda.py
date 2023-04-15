#Funcion anonima / palabra clave

"""Una limitación de las expresiones lambda en Python es que solo pueden tener una línea. 
Por lo tanto, solo pueden usarse para cosas muy sencillas. 
En otros lenguajes esa limitación no existe, es una manía de Python. Además, no hace falta la 
palabra clave return, se devolverá el valor de expresión en sí."""


multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(5))

#La función filter() integrada de Python puede usarse para crear un 
# nuevo iterador a partir de un iterable existente (como una lista o un diccionario)


numeros= (4,5,7,8,8,2,1,3,546,123,47,95,63,14)

numeros_pares = filter(lambda x:x%2 ==0,numeros)
print(list(numeros_pares))

numeros_impares = filter(lambda x:x%2 ==1,numeros)
print(list(numeros_impares))


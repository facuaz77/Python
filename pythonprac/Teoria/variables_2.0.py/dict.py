
diccionario = dict(nombre = "facundo" , apellido="alaniz" )

print(diccionario)


#las listas no pueden ser claves y en un conjunto si utilizando el frozenset

diccionario2 = {frozenset(["hola"]): "adios"}

#fromkeys

diccionario3 = dict.fromkeys("Uno") #none
diccionario4 = dict.fromkeys(["Facundo"], "mi nombre")

print(diccionario3, diccionario2)

print(diccionario4)
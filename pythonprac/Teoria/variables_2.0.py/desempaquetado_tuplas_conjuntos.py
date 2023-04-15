
#se puede crear en tuplas y listas y conjuntos(set)

datos = ("Facundo", "apellido" , 44931800)

tupla = tuple(["dato", "dato2","dato3"])

nombre,apellido,dni = datos


print(nombre,apellido,dni)

variable, variable2, variable3 = tupla

print(variable,variable2,variable3)


#tupla sencilla
tupla2 = "hola", 12, 3

tupla3= "adios",

print(tupla2,tupla3)

#conjuntos

conjunto = set(["Datazo"])


#frozenset un conjunto dentro de otro
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)


#Teoria de conjuntos


conjunto_1 = {"hola" , 2 , 5 , 6, 8, 9, 66, 22, "como", "estas"}

conjunto_2 = {2 , 5 , 6}


#verificacion de subconjuntos
rta = conjunto_2.issubset(conjunto_1)
rta2 = conjunto_2.issuperset(conjunto_1)

print(rta,rta2)





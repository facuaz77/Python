#list crea una lista


ejemplo = list(["hola", "como estas" , 123])

lista = ["uno" , 2 , "tres"]

lista2 = ["otra lista"] 

lista3 = [3, 4 ,88 ,72 ,25 ,10 ,6, 1 , 0 , 777 , 100 ,200 ,300 ,250 ,999 ,249, True , False]


#len list

#print(len(ejemplo))



#append se utiliza para agregar un string a una lista

ejemplo.append("chau")

#print(ejemplo)


#insert agrega un string en la posicion que indiquemos

lista.insert(2, 2.5)

#print(lista)

#extend podemos agregar varios elementos a nuestra lista

lista2.extend(["agregamos" , "mas", "D",4,"tos"])

#print(lista2)

#pop elimina el dato de una lista indicandole desde su indice


lista.pop(0)

#con - podemos eliminar a la inversa 

lista.pop(-1)

#print(lista)

#print(len(lista))

#remove elimina por su valor

ejemplo.remove("hola")

#print(ejemplo)

#clear remueve una lista por completo

ejemplo.clear()
#print(ejemplo)

#sort ordena numeros de menor a mayor y booleanos

lista3.sort()

#print(lista3)

#tambien se puede invertir el orden

lista3.sort(reverse=True)
#print(lista3)

#o simplemente con .reverse la lista ya se invierte

lista3.reverse()

print(lista3)



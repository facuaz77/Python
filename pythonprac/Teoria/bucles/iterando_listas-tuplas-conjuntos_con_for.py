animales = ["pescado", "perro" , "gato" , "caballo"]

numeros = [4 , 68 , 72 , 32 ]


#recorriendo la lista animales

for animal in animales:
    print(f"Su animal es: {animal}")
    
print("----------------------------------------------------------")
    
#multiplicando numeros en un for

for num in numeros:
     
    print(f"Sus numeros multiplicados por 3 son: {num*3}")
    
    
#iterando dos listas con zip

print("------------------USANDO ZIP PARA ITERAR DOS LISTAS------------------")
usuarios = ["Lucas", "Felipe" ,"Codesal","Facundo"]
id = [1,2,3,4]

for lista1,lista2 in zip(usuarios,id):
    print(f"Su usuario es:{lista1}")
    print(f"Su id es: {lista2}")
    
    
#funcion in range

print("--------------------in range----------------")

for hola in range(20):
    print(hola)
    
#recorrer una lista por su indice
print("------------------------------------------------------------------")
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"Su indice es {indice} y su valor es {valor}")
    
    
#else en un for

print("-------------------ELSE-------------------")

for numero in numeros:
    print(f"Recorriendo el bucle: {numero}")
else:
    print("El bucle finalizo")
    
    
#Todos estos valores funcionan de igual manera con una tupla y un conjunto
    

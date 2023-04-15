#String methods  date.method()
#todos los metodos son funciones pero no todas las funciones son metodos, por ej dir, len

cadena = "Hola mi nombre es facundo"
cadena2 = "uno dos tres cuatro"
cadena3 = "1234566666"
cadena4 = "abcdefghiklmnñopqrstuvwyz"
cadena5= "texto,con,comas"

#dir indica todo lo que podemos hacer con un objeto

print(dir(cadena))


#upper convierte todo a mayuscula 


print(cadena.upper())

#lower todo a minuscula

print(cadena.lower())

#capitalize primera en mayuscula

print(cadena2.capitalize())


"""find y index busca una cadena en otra cadena, la diferencia es que find tira -1 al no encontrar nada
y index tira un exception """
print(cadena2.find("o"))
print(cadena2.index("u"))

#Isnumeric devuelve un true si el string es numerico

print(cadena3.isnumeric()) #Por mas que sea un string y no un int nos va a devolver que es numerico ya que es lo que contiene



#isAlpha solo nos va  a devolver un true cuando no hayas espacios ni caracteres especiales, solo letras
print(cadena4.isalpha())



#count nos cuenta cuantas coincidencias hay en un dato

print(cadena3.count("6")) 
print(cadena.count("a"))


#para recordar len vuelve hacer una funcion y no un metodo como los anteriores

print(len(cadena))

#starstwith verifica si una cadena empieza con otra dada, si es verdad dara True si no False

print(cadena.startswith("Hola"))

#endswith es lo contrario verifica con que termina
print(cadena.endswith("do"))

#replace remplaza la cadena que le otorguemos

print(cadena.replace("Hola" , "Hello")) #sirve con comas por ej
remplazo  = cadena5.replace(",", " ")
print(remplazo.capitalize())


#Split separa la cadena con lo que le indiquemos creando una lista

remplazo2 = cadena5.split(",")
print(remplazo2)
print(remplazo2[0])











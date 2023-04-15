diccionario = {
    
    "nombre": "Facundo",
    "apellido": "Alaniz",
    "DNI": 44931800,
    "Sexo": "M"
    
}



#obtienes las llaves del dict
print(diccionario.keys())


#get obtienes los valores
print(diccionario.get("nombre"))


#clear elimina por completo el diccionario y pop elimina una llave con su valor
#diccionario.clear()
diccionario.pop("Sexo", "DNI")
print(diccionario)


print(diccionario.items()) #se pueden iterar elementos

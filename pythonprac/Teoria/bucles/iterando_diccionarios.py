diccionario = {
    
    "Nombre" : "Facundo",
    "Apellido": "Alaniz",
    "Edad": 19,
    
    
}


#ver sus claves

for Key in diccionario:
    Key
    print(Key)

print("------------------------------------------------------")


#para recorrer un diccionario con for necesitamos del elemento items

for di in diccionario.items():
    llave = di[0]
    value= di[1]
    print("DATO DEL USUARIO")
    print(f" Su {llave} es {value} ")
    


print("-------------------------------")
#para crear funciones utilizamos def
def saludo():
    print("hola usuario!")
    
saludo()

print("-----------------------")
    
    

#creando una funcion con parametros

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        apodo = "genia"
        
    elif (sexo == 'hombre'):
        apodo = "genio"
    
    print(f"Hola {nombre} {apodo} ¿como andas?")
    
saludar("Camila" , "mujer")
saludar("Ramiro" , "Hombre")


#creando una contraseña aleatoria

def crear_contraseña(num):
    chars = 'abcdefjhijklmnñopqrstuvwxyz0123456789'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 3
    c2 = num - 1
    c3 = num 
    c4 = num - 4
    c5 = num - 2
    c6 = num  - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{chars[c5]}{chars[c6]}"
    return contraseña

print("----------RANDOM PASSWORD------------")

#aca se desempaqueta la funcion
#Cambiando el numero nos dara diferentes contraseñas
password = crear_contraseña(2) #<-----

fin = f"Su contraseña aleatoria es: {password}"
print(fin)



    


#elif if else

"""
if 5 > 7:
    print("Si es mayor")
else:
    print("no es mayor")
"""   
    
edad = 24

if edad >= 18:
    print("Sos mayor de edad") 
else:
    print("no sos mayor de edad")
    
#Ejemplo inicio de sesion    

contraseña = "123"

contraseña_almacenada = '123'

if contraseña == contraseña_almacenada:
    print("Iniciando sesion")
else:
    print("Contraseña incorrecta")
    
    
#Ingresos 

dinero_ganado = 12000

gasto = 3000


#if anidado
if dinero_ganado > 10000:
    if dinero_ganado < gasto:
        print("Podrias vivir tranquilo en cualquier lugar")
    elif dinero_ganado - gasto > 3000:
        print("Estas bien economicamente")
    else:
        print("Estas en deficit")
    
        
elif dinero_ganado >= 1000:
    print("Estas muy bien economicamente")
    
elif dinero_ganado >= 500:
    print("Estas bien en Argentina")
    

    
else:
    print("estas bien en venezuela")
    
    
    
    
    
    
"""_
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla 
en líneas distintas el nombre del usuario tantas veces como el número introducido.    
    """
    

n = input("Como es su nombre?: ")
n_e = int(input("Ingrese un numero entero: "))





print(n.split(" ") * n_e)
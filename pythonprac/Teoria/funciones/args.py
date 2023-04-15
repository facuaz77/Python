#el * siempre tiene que ir despues
def suma (nombre,*numeros):
    
    return f"{nombre} la suma de tus numeros es: {sum(numeros)}"


rs = suma("Lucas",4,5,6,9)

print(rs)

#el apodo ir por defecto pero podemos modificarlo
def frase (nombre,apellido,apodo = "Crack"):
    return f"Hola {nombre} {apellido}. sos {apodo}"

frase_rs = frase("Felipe", "Reynoso","Capo")
print(frase_rs)
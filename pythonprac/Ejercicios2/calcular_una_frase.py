#Calcular el tiempo de una frase

usuario_frase = input("Ingrese una frase: ")

frase = usuario_frase.split(" ")

cantidad_palabras = len(frase)

print(f"Dijiste {cantidad_palabras} y tardarias {cantidad_palabras / 2}") #dividido dos ya que tardamos un segundo en decir 2 palabras


if cantidad_palabras > 100:
    print("Estas escribiendo un libro")

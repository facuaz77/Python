
#Una persona tiene diferentes tipos de frutas, va a comer la que quiera pero hay una la cual le hizo mal



frutas = ("Manzana" , "Pera" , "Banana" ,"Ciruela" , "Granada" , "Kiwi" , "Naranja" , "Uvas")


print("---------------CONTINUE------------------")
for fru in frutas:
    if fru == "Ciruela":
        continue
    print(f"Me voy a comer una: {fru}")
    

print("------------BREAK--------")

#Con el break no se ejecutara el else
for fru in frutas:
    if fru =="Granada":
        break
    print(f"Me voy a comer una: {fru}")
    
print("Me duele la panza, no como mas")



#recorriendo una string con for
print("-------------------------")
cadena = "Hola como estas"

for cad in cadena:
    print(cad)


print("-------------------Forma rapida------------------------------")

#recorrer en una sola linea
#duplicando numeros



nume = (1 , 3 , 8 , 4 , 54)
numero = [x*2 for x in nume]
print(numero)









print("-------------Otra forma de hacerlo----------")


numeros = list()

for num in nume:
    numeros.append(num*4)
print(numeros)
    

        

    

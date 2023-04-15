inv = float(input("Hola! ¿cuanto desea invertir?: "))
interes = float(input("¿Cuanto es el interes anual?: "))
años = int(input("Y por ultimo ¿por cuantos años invertira?: "))


rs = inv * años / interes

print("Capital final: " + str(round(inv * (interes / 100 + 1) ** años)))



import random

def juego():
    
    jugador = int(input("Elige una opcion Piedra(1) Papel(2) Tijeras(3): "))
    
    compu = random.choice((1,2,3))
    
    inputs = {
        #tijeras
        1: {
            'pierde': 2,
        'gana':3
            },
        
        #papel
        2:{
            'pierde': 1,
            'gana': 3    
        },
        
        #Piedra
        3:{
            'piedra':2,
            'gana':1
            
            
        }
    }
    
    if inputs[jugador].get('gana') == compu:
        print(f"Has ganado! compu a elegido {compu}")
        
    elif [jugador] == [compu]:
        print(f"Empataron! compu a elegido {compu}")
        
    else:
        print(f"Has perdido! compu a elegido {compu}")
    
juego()
        
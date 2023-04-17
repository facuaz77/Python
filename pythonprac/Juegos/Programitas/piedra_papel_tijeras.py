
#Piedra papel o tijera

import random


def juego():
    
    jugador = int(input("Elige una opcion Piedra(1) Papel(2) Tijeras(3): "))
    
    
    compu = random.choice((1,2,3))
    
    if jugador == 1 and compu == 3:
        print(f"Has ganado! compu a elegido Tijeras({compu})")
    elif jugador == 3 and compu ==2:
        print(f"Has ganado! compu a elegido Papel({compu})")
        
    elif jugador == 2 and compu==1:
        print(f"Has ganado! compu a elegido Piedra({compu})")
        
    if compu == 1 and jugador == 3:
        print(f"Has perdido! compu a elegido Piedra({compu})")
    elif compu == 3 and jugador ==2:
        print(f"Has perdido! compu a elegido Tijeras({compu})")
        
    elif compu == 2 and jugador==1:
        print(f"Has perdido! compu a elegido Papel({compu})")
    
    elif compu == 1 and jugador == 1:
        print(f"Empataron! vos y la compu eligieron Piedra({compu})")
    elif compu == 2 and jugador == 2:
        print(f"Empataron! vos y la compu eligieron Papel({compu})")
    elif compu == 3 and jugador == 3:
        print(f"Empataron! vos y la compu eligieron Tijeras({compu})")
           
juego()
        
        
    
    
        
    
        

        
    
        
    
import random

def juego_piedra_papel_tijera():
    puntuacion_jugador = 0
    while True:
        opciones = ["rock", "paper", "scissors"]
        oponente = random.choice(opciones)
        jugador = input("Ingrese una opción (rock, paper, scissors): ").lower()
        while jugador not in opciones:
            print("Opción no válida. Intente de nuevo.")
            jugador = input("Ingrese una opción (rock, paper, scissors): ").lower()
        print(f"Oponente eligió: {oponente}")
        if jugador == oponente:
            print("Empate!")
        elif (jugador == "rock" and oponente == "scissors") or \
             (jugador == "paper" and oponente == "rock") or \
             (jugador == "scissors" and oponente == "paper"):
            print("Ganaste!")
            puntuacion_jugador += 1
        else:
            print("Perdiste!")
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo!= "s":
            break
    print(f"Tu puntuación final es: {puntuacion_jugador}")

juego_piedra_papel_tijera()

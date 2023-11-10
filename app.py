import random

opciones = ["papel", "tijeras", "roca"]

puntos_usuario = 0
puntos_compu = 0

while True:
    usuario = input("Eligen una opción: papel, tijeras o roca. Escribe 'salir' para terminar el juego: ")
    usuario = usuario.lower()

    if usuario == "salir":
        break
    if usuario not in opciones:
        print("Opción inválida. Inténtalo de nuevo.")
        continue

    computadora = random.choice(opciones)

    print("La computadora eligió: ", computadora)
    
    if usuario == computadora:
        print("Empate.")
    elif usuario == "papel" and computadora == "roca":
        print("Ganaste. El papel envuelve a la roca.")
        puntos_usuario += 1
    elif usuario == "papel" and computadora == "tijeras":
        print("Perdiste. Las tijeras cortan el papel.")
        puntos_compu += 1
    elif usuario == "tijeras" and computadora == "papel":
        print("Ganaste. Las tijeras cortan el papel.")
        puntos_usuario += 1
    elif usuario == "tijeras" and computadora == "roca":
        print("Pediste. La roca rompe a las tijeras.")
        puntos_compu += 1
    elif usuario == "roca" and computadora == "papel":
        print("Pediste. El papel envuelve a la roca.")
        puntos_compu += 1
    elif usuario == "roca" and computadora == "tijeras":
        print("Ganaste. La roca rompe a las tijeras.")
        puntos_usuario += 1
    
    print("Puntos del usuario:", puntos_usuario)
    print("Puntos del compu:", puntos_compu)
    print("")

print("Fin del juego. Gracias por jugar")
if puntos_usuario > puntos_compu:
    print("Lo siento, Has ganado el juego.")
elif puntos_usuario < puntos_compu:
    print("Lo siento, Has perdido el juego.")
else:
    print("Has empatado con la compu")
turnos = []
contador = 0

def tomar_turno():
    global contador
    contador += 1
    turnos.append(contador)
    print(f"Turno {contador} tomado.")

def ver_siguiente_turno():
    if turnos:
        print(f"El siguiente turno es el número {turnos[0]}.")
        turnos.pop(0)
    else:
        print("No hay turnos en espera.")

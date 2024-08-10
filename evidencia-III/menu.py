import turnos

def mostrar_menu():
    print("\nMenú de Turnos:")
    print("1. Tomar un turno")
    print("2. Ver el siguiente turno")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            turnos.tomar_turno()
        elif opcion == "2":
            turnos.ver_siguiente_turno()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()


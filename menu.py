def mostrar_menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Opción 5")
    print("6. Opción 6")
    print("7. Opción 7")
    print("8. Opción 8")
    print("9. Opción 9")
    print("10. Opción 10")
    print("11. Opción 11")
    print("12. Opción 12")
    print("13. Opción 13")
    print("14. Opción 14")
    print("15. Opción 15")
    print("16. Opción 16")
    print("17. Opción 17")
    print("18. Opción 18")
    print("19. Opción 19")
    print("20. Opción 20")
    print("21. Opción 21")
    print("22. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        print("Ejecutando opción 1")
        # Agregar código para la opción 1
    elif opcion == 2:
        print("Ejecutando opción 2")
        # Agregar código para la opción 2
    elif opcion == 3:
        print("Ejecutando opción 3")
        # Agregar código para la opción 3
    elif opcion == 4:
        print("Ejecutando opción 4")
        # Agregar código para la opción 4
    elif opcion == 5:
        print("Ejecutando opción 5")
        # Agregar código para la opción 5
    elif opcion == 6:
        print("Ejecutando opción 6")
        # Agregar código para la opción 6
    elif opcion == 7:
        print("Ejecutando opción 7")
        # Agregar código para la opción 7
    elif opcion == 8:
        print("Ejecutando opción 8")
        # Agregar código para la opción 8
    elif opcion == 9:
        print("Ejecutando opción 9")
        # Agregar código para la opción 9
    elif opcion == 10:
        print("Ejecutando opción 10")
        # Agregar código para la opción 10
    elif opcion == 11:
        print("Ejecutando opción 11")
        #Agregar código para la opción 11
    elif opcion == 12:
        print("Ejecutando opción 12")
        # Agregar código para la opción 12
    elif opcion == 13:
        print("Ejecutando opción 13")
        # Agregar código para la opción 13
    elif opcion == 14:
        print("Ejecutando opción 14")
        # Agregar código para la opción 14
    elif opcion == 15:
        print("Ejecutando opción 15")
        # Agregar código para la opción 15
    elif opcion == 16:
        print("Ejecutando opción 16")
        # Agregar código para la opción 16
    elif opcion == 17:
        print("Ejecutando opción 17")
        # Agregar código para la opción 17
    elif opcion == 18:
        print("Ejecutando opción 18")
        # Agregar código para la opción 18
    elif opcion == 19:
        print("Ejecutando opción 19")
        # Agregar código para la opción 19
    elif opcion == 20:
        print("Ejecutando opción 20")
        # Agregar código para la opción 20
    elif opcion == 21:
        print("Ejecutando opción 21")
        # Agregar código para la opción 21
    elif opcion == 22:
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción no válida")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Selecciona una opción: "))
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()

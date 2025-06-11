from consultar_clima import consultar_clima
from ver_historial import ver_historial_personal
from estadisticas import estadisticas_globales
from consejo_ia import consejo_ia
#from acerca_de import acerca_de

def menu_principal(usuario_actual):  

    while True:
        print("\nGUARDIANCLIMA ITBA")
        print("1. Consultar Clima Actual y Guardar en Historial Global")
        print("2. Ver Mi Historial Personal de Consultas por Ciudad")
        print("3. Estadísticas Globales de Uso y Exportar Historial Completo")
        print("4. Consejo IA: ¿Cómo Me Visto Hoy?")
        print("5. Acerca De...")
        print("6. Cerrar sesión")
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            consultar_clima(usuario_actual)
        elif opcion == "2":
            ver_historial_personal(usuario_actual)
            print("En desarrollo\n")
        elif opcion == "3":
            estadisticas_globales()
            print("En desarrollo\n")
        elif opcion == "4":
            API_KEY_GEMINI = "AIzaSyBdBHVCj7NLzgLQ1EC6MPqWJv-122ybjlU"
            consejo_ia(usuario_actual, API_KEY_GEMINI)
            print("En desarrollo\n")
        elif opcion == "5":
            #acerca_de()
            print("En desarrollo\n")
        elif opcion == "6":
            print("Sesión cerrada.\n")
            break
        else:
            print("Opción inválida. Ingrese una opción entre 1 y 6.")

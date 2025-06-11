from registro import registrar_usuario, iniciar_sesion
from main import menu_principal


while True:
    print("\nBIENVENIDO/A A GUARDIANCLIMA ITBA")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ").strip()

    if opcion == '1':
        usuario = iniciar_sesion()
        if usuario:
            print(f"Bienvenido, {usuario}!")
            menu_principal(usuario)
            
    elif opcion == '2':
        usuario = registrar_usuario()
    elif opcion == '3':
        print("Saliendo del programa. ¡Hasta luego!")
        break   



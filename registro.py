import csv # Importa csv para poder manejar archivos CSV
import os # Importa os (operating system) para poder chequear que archivos existen
import re # Importa re (regual expresions) para poder verificar las contraseñas

USUARIOS = "usuarios_simulados.csv"  # Agrega el archivoCSV donde se guardan los usuarios

def validar_contraseña(contra): #Chequea una lista de posibles errores en la contraseña y devuelve una lista con estos errores
    errores = []
    if len(contra) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres")
    #agregar más errores

    return errores

def usuario_existente(usuario): #Chequea que el usuario exista en el CSV
    if not os.path.exists(USUARIOS):
        return False #Si no encuentra el archivo devuelve False
    with open(USUARIOS, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for fila in reader:
            if fila[0] == usuario:
                return True #Si el archivo existe, lo abre, lo lee y busca la fila que coincida con el nombre de usuario y devuelve True
    return False #Si no encuentra ese nombre de usuario devuelve False

def registrar_usuario():
    print("\nRegistro de usuario")
    while True:
        usuario = input("Ingrese nombre de usuario: ").strip()
        if usuario_existente(usuario):
            print("El nombre de usuario ya existe. Por favor, elija otro.")
        else:
            break

    while True:
        contraseña = input("Ingrese contraseña: ").strip()
        errores = validar_contraseña(contraseña)
        if errores:
            print("Errores en la contraseña:")
            for error in errores:
                print(f"- {error}")
        else:
            break

    with open(USUARIOS, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([usuario, contraseña])

    print("¡Usuario registrado exitosamente!")

def iniciar_sesion():
    print("\nIniciar sesión")
    usuario = input("Ingrese nombre de usuario: ").strip()
    contraseña = input("Ingrese contraseña: ").strip()

    if not usuario_existente(usuario):
        print("El nombre de usuario no existe.")
        return

    with open(USUARIOS, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for fila in reader:
            if fila[0] == usuario and fila[1] == contraseña:
                print("¡Inicio de sesión exitoso!")
                return
    print("Contraseña incorrecta.")

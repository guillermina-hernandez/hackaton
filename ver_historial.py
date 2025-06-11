import csv
import os

HISTORIAL = "historial_global.csv"

def ver_historial_personal(usuario_actual):
    if not os.path.exists(HISTORIAL):
        print("\nAún no hay historial disponible.")
        return

    historial_usuario = []

    with open(HISTORIAL, mode='r', newline='', encoding='utf-8') as file:  
        reader = csv.DictReader(file)
        for fila in reader:
            if fila["Usuario"] == usuario_actual:  
                historial_usuario.append(fila)

    if not historial_usuario:
        print(f"\nNo hay historial de consultas para el usuario '{usuario_actual}'.")
        return
    
    historial_usuario.sort(key=lambda x: x["FechaHora"], reverse=True) # Ordenar por fecha y hora
    print(f"\nHistorial de consultas para el usuario '{usuario_actual}':")

    print(f"\nHistorial de consultas para {usuario_actual}:\n")
    ciudad_actual = ""
    for fila in historial_usuario:
        if fila["Ciudad"] != ciudad_actual:
            ciudad_actual = fila["Ciudad"]
            print(f"\nCiudad: {ciudad_actual}")
        print(f" - {fila['FechaHora']}: {fila['Temperatura_C']}°C, {fila['Condicion_Clima']}, "
              f"Humedad: {fila['Humedad_Porcentaje']}%, Viento: {fila['Viento_kmh']} km/h")
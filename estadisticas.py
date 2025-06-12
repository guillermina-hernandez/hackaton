import csv
import os
from collections import Counter
import shutil

HISTORIAL = "historial_global.csv"
EXPORTADO = "historial_exportado.csv"

def estadisticas_globales():
    if not os.path.exists(HISTORIAL):
        print("\nNo hay historial para generar estadísticas.")
        return

    total_consultas = 0
    usuarios = []
    ciudades = []

    with open(HISTORIAL, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for fila in reader:
            total_consultas += 1
            usuarios.append(fila["Usuario"])
            ciudades.append(fila["Ciudad"])

    usuario_mas_frecuente = Counter(usuarios).most_common(1)[0]
    ciudad_mas_consultada = Counter(ciudades).most_common(1)[0]

    print("\n Estadísticas Globales de Uso:")
    print(f"- Total de consultas realizadas: {total_consultas}")
    print(f"- Usuario con más consultas: {usuario_mas_frecuente[0]} ({usuario_mas_frecuente[1]} consultas)")
    print(f"- Ciudad más consultada: {ciudad_mas_consultada[0]} ({ciudad_mas_consultada[1]} veces)")

    try:
        shutil.copy(HISTORIAL, EXPORTADO)
        print(f"\n Historial completo exportado como '{EXPORTADO}'.")
    except Exception as err:
        print(f"Error al exportar el historial: {err}")

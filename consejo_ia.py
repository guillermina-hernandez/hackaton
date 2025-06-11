import google.generativeai as genai
import csv
from datetime import datetime

def obtener_ultima_consulta(usuario_actual, archivo_historial="historial_global.csv"):
    try:
        with open(archivo_historial, newline='', encoding='utf-8') as file:
            lector = csv.DictReader(file)
            consultas_usuario = [
                fila for fila in lector if fila['Usuario'] == usuario_actual
            ]
        if not consultas_usuario:
            print("No se encontraron consultas previas para este usuario.")
            return None

        consultas_usuario.sort(key=lambda x: datetime.strptime(x['FechaHora'], '%Y-%m-%d %H:%M:%S'), reverse=True)
        return consultas_usuario[0]
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None
    except Exception as err:
        print(f"Error leyendo historial: {err}")
        return None

def generar_prompt(consulta):
    ciudad = consulta['Ciudad']
    temperatura = consulta['Temperatura_C']
    clima = consulta['Condicion_Clima']
    viento = consulta['Viento_kmh']
    humedad = consulta['Humedad_Porcentaje']

    return (
        f"Soy un asistente que da consejos sobre cómo vestirse según el clima. "
        f"El usuario está en {ciudad}. Actualmente hace {temperatura}°C, el clima está '{clima}', "
        f"la humedad es de {humedad}% y el viento corre a {viento} km/h. "
        f"¿Cuál sería una recomendación práctica sobre cómo vestirse para estar cómodo hoy?"
    )

def consejo_ia(usuario_actual, api_key_gemini):
    consulta = obtener_ultima_consulta(usuario_actual)
    if not consulta:
        return

    prompt = generar_prompt(consulta)

    try:
        genai.configure(api_key=api_key_gemini)
        model = genai.GenerativeModel('gemini-pro')
        print("\nGenerando consejo de vestimenta con IA...")
        response = model.generate_content(prompt)
        print("\nConsejo de vestimenta sugerido por IA:\n")
        print(response.text if response.text else "No se pudo generar un consejo en este momento.")
    except Exception as err:
        print(f"Error al contactar la API de Gemini: {err}")

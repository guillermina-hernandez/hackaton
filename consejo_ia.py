import google.generativeai as genai
import csv
from datetime import datetime

def obtener_ultimo_clima_usuario(usuario_actual):
    historial = []
    try:
        with open('historial_global.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                historial.append(row)
    except FileNotFoundError:
        print("El archivo historial_global.csv no se encontró. No hay historial de consultas.")
        return None
    except Exception as e:
        print(f"Error al leer historial_global.csv: {e}")
        return None

    consultas_usuario = [
        consulta for consulta in historial
        if consulta.get('Usuario') == usuario_actual
    ]
    
    if not consultas_usuario:
        print(f"No se encontraron consultas de clima para el usuario '{usuario_actual}' en el historial.")
        return None

    try:
        consultas_usuario.sort(
            key=lambda x: datetime.strptime(x['FechaHora'], '%Y-%m-%d %H:%M:%S'),
            reverse=True
        )
    except ValueError as e:
        print(f"Error al parsear la fecha: {e}")
        return None
    
    return consultas_usuario[0] if consultas_usuario else None

def obtener_consejo_ia_gemini(api_key_gemini, temperatura, condicion_clima, humedad, viento_kmh):
    try:
        genai.configure(api_key=api_key_gemini)
        model = genai.GenerativeModel('gemini-1.5-pro-latest')


        prompt_diseñado_por_equipo = (
            f"Actúa como un asesor de vestimenta profesional. "
            f"Con los siguientes datos climáticos:\n"
            f"- Temperatura: {temperatura}°C\n"
            f"- Condición climática: {condicion_clima}\n"
            f"- Humedad: {humedad}%\n"
            f"- Viento: {viento_kmh} km/h\n"
            f"Brinda un consejo breve, práctico y directo sobre cómo vestirse hoy. "
            f"No incluyas saludos ni repitas los datos climáticos, solo el consejo."
        )

        print("\nGenerando consejo de vestimenta con IA...")
        response = model.generate_content(prompt_diseñado_por_equipo)

        if response.text:
            return response.text.strip()
        else:
            return "No se pudo generar un consejo en este momento."
    except Exception as e:
        print(f"Error al contactar la API de Gemini: {e}")
        return "Error al generar el consejo de IA."

def consejo_ia(usuario_actual, api_key_gemini):
    print("\n--- Consejo IA: ¿Cómo Me Visto Hoy? ---")
    
    ultima_consulta = obtener_ultimo_clima_usuario(usuario_actual)

    if ultima_consulta:
        temperatura = ultima_consulta.get('Temperatura_C')
        condicion_clima = ultima_consulta.get('Condicion_Clima')
        humedad = ultima_consulta.get('Humedad_Porcentaje')
        viento_kmh = ultima_consulta.get('Viento_kmh')

        if all([temperatura is not None, condicion_clima is not None, humedad is not None, viento_kmh is not None]):
            print(f"Datos climáticos para el consejo (última consulta):")
            print(f"  Ciudad: {ultima_consulta.get('Ciudad')}")
            print(f"  Temperatura: {temperatura}°C")
            print(f"  Condición: {condicion_clima}")
            print(f"  Humedad: {humedad}%")
            print(f"  Viento: {viento_kmh} km/h")
            
            consejo = obtener_consejo_ia_gemini(
                api_key_gemini,
                temperatura,
                condicion_clima,
                humedad,
                viento_kmh
            )
            print("\n--- Consejo de Vestimenta de la IA ---")
            print(consejo)
            print("--------------------------------------")
        else:
            print("No se pudieron obtener todos los datos climáticos necesarios de la última consulta.")
            print("Asegúrate de que la última consulta de clima contenga Temperatura_C, Condicion_Clima, Humedad_Porcentaje y Viento_kmh.")
    else:
        print("No se encontró una consulta de clima previa para generar un consejo. Por favor, realiza una consulta de clima primero.")

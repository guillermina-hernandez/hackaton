import requests
import csv
from datetime import datetime
import os


API_KEY = "SU_API_KEY_DE_OPENWEATHERMAP"  # Reemplazar con su API Key de OpenWeatherMap
HISTORIAL = "historial_global.csv"

def consultar_clima(usuario_actual): 
    while True:
        print("\nCONSULTAR CLIMA ACTUAL")     
        ciudad = input("Ingrese el nombre de la ciudad: ").strip()
        if not ciudad:
            print("Debe ingresar un nombre de ciudad.")
            return
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"

        parametros = {
            'q': ciudad,
            'appid': API_KEY,
            'units': 'metric',
            'lang': 'es'
        }

        print(f"\nConsultando el clima en {ciudad}...")

        try:
            respuesta = requests.get(url,params=parametros, timeout=10)
            respuesta.raise_for_status()  
            datos = respuesta.json()

            temperatura = datos["main"]["temp"]
            sensacion = datos["main"]["feels_like"]
            humedad = datos["main"]["humidity"]
            viento = datos["wind"]["speed"] * 3.6 
            descripcion = datos["weather"][0]["description"].capitalize()
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"\nClima en {ciudad}:")
            print(f"Temperatura: {temperatura}°C (Sensación: {sensacion}°C)")
            print(f"Humedad: {humedad}%")
            print(f"Viento: {viento:.1f} km/h")
            print(f"Descripción: {descripcion.capitalize()}")
            print(f"Fecha y hora de consulta: {fecha_hora}")

            guardar_historial_global(usuario_actual, ciudad, fecha_hora, temperatura, descripcion, humedad, viento)

        except requests.exceptions.HTTPError as err:
            if respuesta.status_code == 401:
                print("Error: API Key inválida.")
            elif respuesta.status_code == 404:
                print(f"Ciudad '{ciudad}' no encontrada.")
            else:
                print(f"Error HTTP: {err}")
            print(f"Error al consultar el clima: {err}")
        
        except requests.exceptions.RequestException as err:
            print(f"Error de conexión: {err}")
        
        except KeyError:
            print("Error: Formato inesperado en datos recibidos.")
        except Exception as err:
            print(f"Error inesperado: {err}")

        opcion = input("\n¿Desea consultar otra ciudad? (si/no): ").strip().lower()
        if opcion != 'si':
            print("Volviendo al menú principal...\n")
            break

def guardar_historial_global(usuario, ciudad, fecha_hora, temp, clima, humedad, viento):
    encabezado = ["Usuario", "Ciudad", "FechaHora", "Temperatura_C", "Condicion_Clima", "Humedad_Porcentaje", "Viento_kmh"]
    nueva_fila = [usuario, ciudad, fecha_hora, temp, clima, humedad, round(viento, 1)]

    archivo_nuevo = not os.path.exists(HISTORIAL)
    with open(HISTORIAL, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if archivo_nuevo:
            writer.writerow(encabezado)
        writer.writerow(nueva_fila)
    
    print("\nConsulta guardada en el historial global.")

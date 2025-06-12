# GuardiánClima ITBA
Es una aplicación de consola desarrollada en Python que permite consultar el clima, registrar usuarios con validación de contraseñas seguras, generar estadísticas globales a partir del historial de uso y obtener consejos personalizados mediante Inteligencia Artificial.

## Requisitos del Entorno

- Python 3.10 o superior
- Librerías necesarias:
  - `requests`
  - `google-generativeai`

## Instalación de dependencias

    1.Cloná el repositorio o descargá los archivos
    2.Instalá las librerías necesarias:
- `pip install requests google-generativeai`

## Configuración de API Keys

Para funcionar correctamente, la app necesita dos claves:

- `OPENWEATHERMAP_API_KEY`: para obtener datos del clima.
- `GEMINI_API_KEY`: para generar consejos inteligentes de vestimenta.

### Forma segura de configurarlas

1. Crear un archivo `.env` en la raíz del proyecto (no subirlo al repositorio):

OPENWEATHERMAP_API_KEY=tu_clave_openweathermap
GEMINI_API_KEY=tu_clave_gemini

2. Acceder desde el código Python usando `os`:

python
import os

weather_key = os.getenv("OPENWEATHERMAP_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")


Nunca subas estas claves al repositorio. 
Asegurate de que el archivo `.env` esté en el `.gitignore`.

## Cómo ejecutar la aplicación

Desde terminal o consola:

python main.py


## Flujo de Menús

### Menú de Acceso (antes del login)

1. **Iniciar Sesión**  
   - Usuario y contraseña (valida contra `usuarios_simulados.csv`)
2. **Registrar Usuario**  
   - Verifica que no exista  
   - Valida contraseña con al menos 3 criterios de seguridad  
   - Da sugerencias si es débil  
   - Al registrarse, pasa directo al Menú Principal
3. **Salir de la aplicación**

### Menú Principal (tras iniciar sesión)

1. **Consultar Clima Actual y Guardar en Historial**  
   - Pide ciudad  
   - Conecta con OpenWeatherMap  
   - Muestra datos (temperatura, clima, humedad, viento, etc.)  
   - Guarda todo en `historial_global.csv`

2. **Ver mi Historial Personal por Ciudad**  
   - Filtra `historial_global.csv` por usuario y ciudad  
   - Muestra resultados ordenados

3. **Estadísticas Globales + Exportación**  
   - Ciudad más consultada  
   - Total de consultas  
   - Temperatura promedio  
   - El archivo CSV puede usarse en Excel para generar:
     - Gráfico de barras (consultas por ciudad)
     - Gráfico de líneas (tendencia de temperatura por ciudad)
     - Gráfico de torta (condiciones climáticas registradas)

4. **Consejo IA: ¿Cómo me visto hoy?**  
   - Usa la última consulta del usuario o permite seleccionar  
   - Conecta con Gemini y da sugerencia según el clima actual

5. **Acerca de...**  
   - Explica cómo usar la app  
   - Describe el flujo, validaciones, estructura, advertencias y APIs  
   - Muestra los nombres del grupo

6. **Cerrar Sesión**  
   - Vuelve al Menú de Acceso

## Estructura del Proyecto

/guardianclima
│
├── main.py                         # Punto de entrada
├── gestion_usuarios.py            # Registro, login, validación de contraseñas
├── clima.py                       # Conexión a OpenWeatherMap
├── inteligencia.py                # Conexión a Gemini (IA)
├── estadisticas.py                # Procesamiento de historial global
├── utils.py                       # Funciones auxiliares
├── usuarios_simulados.csv         # Simulación de base de usuarios
├── historial_global.csv           # Registro global de consultas
├── requirements.txt
└── README.md

## Advertencia

## Autores

- Micaela Kenigsberg 
- Josefina Freire
- Guillermina Hernandez 
- Dante Reda
- Bianca Vivoda

Grupo: La Consola del tiempo
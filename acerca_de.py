def mostrar_acerca_de():
    print("""
GuardíanClima ITBA es una aplicación de consola desarrollada en Python que permite consultar el clima, guardar un historial, generar estadísticas y recibir consejos de vestimenta usando IA.

El flujo comienza en el Menú de Acceso, donde el usuario puede registrarse o iniciar sesión. Luego accede al Menú Principal con las opciones de consultar clima, ver historial, estadísticas, consejo de vestimenta, información y cerrar sesión.

La creación de usuarios es simulada, con validación de contraseñas según criterios de seguridad. Se informa al usuario si su contraseña es débil y se sugieren mejoras. Las contraseñas se guardan en un archivo CSV de forma no segura, y se aclara que en una app real se usaría hashing.

Los datos climáticos se obtienen desde una API externa y se guardan en un historial global. A partir de estos datos, se generan estadísticas y un archivo CSV que puede usarse para gráficos. La IA devuelve consejos según el clima de cada consulta.

Desarrolladores: [Bianca Vivoda, Dante Reda, Guillermina Hernández, Josefina Freire y Micaela Kenigsberg]  
Grupo: [La Consola del Tiempo]
""")

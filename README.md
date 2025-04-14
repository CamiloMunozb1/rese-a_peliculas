# 🎬 Calificador de Películas

Este proyecto permite registrar, calificar, reseñar y administrar una colección personal de películas o series. Toda la información se almacena en una base de datos SQLite local y se sincronizada con una base de datos en la nube a través de la API de Notion.

## 📦 Funcionalidades

- Registrar el nombre de una película o serie
- Agregar reseñas y calificaciones
- Subir los datos a Notion automáticamente
- Eliminar registros locales y archivarlos en Notion
- Visualizar todas las películas calificadas en formato tabla

## ⚙️Configuración

Edita las siguientes líneas con tu propia clave y ID de base de datos de Notion:
  
    self.api_key = "TU_API_KEY"
    self.database_id = "TU_DATABASE_ID"

Puedes obtener tu API Key desde Notion Integrations y el ID de tu base de datos desde la URL del tablero.

## 🚀Cómo usar

1. Registrar una nueva película
   Ejecuta ingreso_pelicula.py y sigue las instrucciones para registrar, calificar y subir una película.
   
3. Eliminar una película
   Ejecuta eliminar_pelicula.py para eliminar una película de la base de datos local y archivar su entrada en Notion.

4. Mostrar todas las películas registradas
   Ejecuta mostrar_peliculas.py para ver una tabla con todas las películas, reseñas y calificaciones.

## 🧪 Requisitos

- Python 3.8 o superior
- SQLite3 (incluido por defecto en Python)
- Librerías externas:
  - `requests` para interactuar con la API de Notion
  - `pandas` para mostrar y manejar los datos de forma tabular

  Instala los paquetes necesarios con:
  ```bash
    pip install requests pandas

## 👨‍💻 Autor

Proyecto desarrollado por Juan Camilo Muñoz.

## Licencia

Este proyecto esta bajo una licencia MIT.






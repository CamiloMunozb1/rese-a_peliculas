import sqlite3
import requests

# Clase que maneja la conexión a la base de datos SQLite
class IngresoDB:
    def __init__(self,conexionDB):
        try:
            self.conn = sqlite3.connect(conexionDB)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}")

    def cierre_conexion(self):
        self.conn.close()
        print("Cierre de la base de datos exitoso.")

# Clase para eliminar una película y sus datos relacionados tanto en la base de datos local como en Notion
class EliminarPelicula:
    def __init__(self,conexion):
        self.conexion = conexion

    # Método que elimina la película, reseña y calificación de la base de datos local
    def eliminacion_pelicula(self):
        try:
            # Solicita al usuario el nombre de la película
            self.pelicula_name = str(input("Ingresa el nombre de la pelicula a eliminar: ")).strip()
            if not self.pelicula_name:
                print("Este campo no puede estar vacio.")
                return

            # Busca el ID de la película en la tabla principal
            self.conexion.cursor.execute("SELECT pelicula_id FROM movie_user WHERE pelicula_name = ?", (self.pelicula_name,))
            pelicula = self.conexion.cursor.fetchone()

            if pelicula:
                pelicula_id = pelicula[0]
                # Elimina registros relacionados en las tablas de reseñas y calificaciones
                self.conexion.cursor.execute("DELETE FROM reseña_user WHERE pelicula_id = ?", (pelicula_id,))
                self.conexion.cursor.execute("DELETE FROM calificacion_user WHERE pelicula_id = ?", (pelicula_id,))
                # Elimina por ultimo el nombre de la pelicula o serie
                self.conexion.cursor.execute("DELETE FROM movie_user WHERE pelicula_id = ?", (pelicula_id,))
                self.conexion.conn.commit()
                print("Nombre de la pelicula junto con su reseña y calificacion eliminada con exito.")
        
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}.")

    # Método que busca en Notion la página de la película para obtener su ID
    def buscar_archivo(self):
        try:
            # Claves necesarias para autenticar la API de Notion
            self.api_key = "TU_API_KEY"
            self.database_id = "TU_DATA_BASE_ID"

            url = "https://api.notion.com/v1/search"
                        
            headers = {
                "Authorization" : f"Bearer {self.api_key}",
                "Content-type" : "application/json",
                "Notion-Version" : "2022-06-28"
            }

            # Realiza una búsqueda usando el nombre de la película
            data = {
                "query" : self.pelicula_name,
                "filter": {
                    "value" : "page",
                    "property" : "object"
                }
            }
            
            respuesta = requests.post(url=url, json=data, headers=headers)
            resultado = respuesta.json().get("results")

            # Si se encuentra, devuelve el ID de la página en Notion
            if resultado:
                return resultado[0]["id"]
            else:
                return None
            
        except Exception as error:
            print(f"Error en el programa: {error}.")

    # Método que archiva (elimina visualmente) la página de la película en Notion
    def archivar_nube(self):
        try:
            # Busca el ID de la página a archivar
            page_id = self.buscar_archivo()
            if not page_id:
                print("No se encontro el nombre de la pelicula o serie en la nube de Notion.")
                return

            url = f"https://api.notion.com/v1/pages/{page_id}"

            headers = {
                "Authorization" : f"Bearer {self.api_key}",
                "Content-type" : "application/json",
                "Notion-Version" : "2022-06-28"
            }

            # En Notion, "archived": True elimina la visibilidad de la página
            data = {
                "archived" : True
            }

            respuesta = requests.patch(url=url, json=data, headers=headers)

            if 200 <= respuesta.status_code < 300:
                print("Nombre de la pelicula o serie junto con su reseña y calificacion eliminada de la nube.")
            else:
                print(f"Error: {respuesta.status_code},{respuesta.text}")
        
        except Exception as error:
            print(f"Error en el programa: {error}.")


# Se crea la conexión a la base de datos local
rutaDB = r"C:\Users\POWER\calificador_peliculas.db"
conexion = IngresoDB(rutaDB)

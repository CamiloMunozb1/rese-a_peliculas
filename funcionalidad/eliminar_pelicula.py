import sqlite3
import requests


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

class EliminarPelicula:
    def __init__(self,conexion):
        self.conexion = conexion

    def eliminacion_pelicula(self):
        try:

            self.pelicula_name = str(input("Ingresa el nombre de la pelicula a eliminar: ")).strip()
            if not self.pelicula_name:
                print("Este campo no puede estar vacio.")
                return
            self.conexion.cursor.execute("SELECT pelicula_id FROM movie_user WHERE pelicula_name = ?",(self.pelicula_name,))
            pelicula = self.conexion.cursor.fetchone()
            if pelicula:
                pelicula_id = pelicula[0]
                self.conexion.cursor.execute("DELETE FROM reseña_user WHERE pelicula_id = ?",(pelicula_id,))
                self.conexion.cursor.execute("DELETE FROM calificacion_user WHERE pelicula_id = ?",(pelicula_id,))
                self.conexion.cursor.execute("DELETE FROM movie_user WHERE pelicula_id = ? ",(pelicula_id,))
                self.conexion.conn.commit()
                print("Nombre de la pelicula junto con su reseña y calificacion eliminada con exito.")
        
        except Exception as error:
            print(f"Error en el programa: {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

    def buscar_archivo(self):
        try:

            self.api_key = "TU_API_KEY"
            self.database_id = "TU_DATA_BASE_ID"

            url = "https://api.notion.com/v1/search"

                        
            headers = {
                "Authorization" : f"Bearer {self.api_key}",
                "Content-type" : "application/json",
                "Notion-Version" : "2022-06-28"
            }

            data = {
                "query" : self.pelicula_name,
                "filter":{
                    "value" : "page",
                    "property":"object"
                }
            }
            
            respuesta = requests.post(url=url, json=data, headers=headers)
            resultado = respuesta.json().get("results")
            if resultado:
                return resultado[0]["id"]
            else:
                return None
            
        except Exception as error:
            print(f"Error en el programa: {error}.")


    def archivar_nube(self):
        try:

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

            data = {
                "archived" : True
            }

            respuesta = requests.patch(url = url, json=data, headers=headers)
            if 200 <= respuesta.status_code < 300:
                print("Nombre de la pelicula o serie junto con su reseña y calificacion eliminada de la nube.")
            else:
                print(f"Error: {respuesta.status_code},{respuesta.text}")
        
        except Exception as error:
            print(f"Error en el programa: {error}.")


rutaDB = r"C:\Users\POWER\calificador_peliculas.db"
conexion = IngresoDB(rutaDB)

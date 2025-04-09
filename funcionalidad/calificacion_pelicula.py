import sqlite3
import requests

class IngresoDB:
    def __init__(self, conexionDB):
        try:
            self.conn = sqlite3.connect(conexionDB)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

    def cierre_conexion(self):
        self.conn.close()
        print("Cierre de la base de datos exitoso.")

class CalificacionPelicula:
    def __init__(self, conexion):
        self.conexion = conexion

    def calificacion_contenido(self):
        try:

            self.pelicula_name = str(input("Ingresa el nombre de la pelicula o serie a reseñar antes registrado: ")).strip()
            self.calificacion_usuario = int(input("Ingresa una calificacion para la pelicula o serie (1-10): "))
            if not self.pelicula_name or not self.calificacion_usuario:
                print("No se puede tener el espacio en blanco.")
                return
        
            self.api_key = "TU_API_KEY"
            self.database_id = "TU_API_KEY"

            self.conexion.cursor.execute("SELECT pelicula_id FROM movie_user WHERE pelicula_name = ?",(self.pelicula_name,))
            pelicula = self.conexion.cursor.fetchone()
            if pelicula:
                pelicula_id = pelicula[0]
                self.conexion.cursor.execute("INSERT INTO calificacion_user(calificacion_usuario,pelicula_id) VALUES (?,?)",(self.calificacion_usuario,pelicula_id))
                self.conexion.conn.commit()
                print("Reseña de la pelicula o serie subida con exito.")
            else:
                print("Nombre de la pelicula o serie no encontrada.")

        except Exception as error:
            print(f"Error en el programa: {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
    
    def subina_nube(self):
        try:

            url = "https://api.notion.com/v1/pages"

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-type" : "application/json",
                "Notion-Version" : "2022-06-28"
            }

            data = {
                "parent" : {"database_id" : self.database_id},
                "properties":{
                    "calificacion_usuario":{
                        "number" : self.calificacion_usuario
                    }
                }
            }

            respuesta = requests.post(url=url, json=data, headers=headers)
            if 200 <= respuesta.status_code < 300:
                page_id = respuesta.json()["id"]
                print("Calificacion de la serie o reseña subida a la nube de Notion.")
                return page_id
            else:
                print(f"Error: {respuesta.status_code}, {respuesta.text}.")

        except Exception as error:
            print(f"Error en el programa: {error}.")



rutaDB = r"C:\Users\POWER\calificador_peliculas.db"
conexion = IngresoDB(rutaDB)


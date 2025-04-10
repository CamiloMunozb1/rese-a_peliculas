import sqlite3
import requests

class IngresoDB:
    def __init__(self,conexionDB):
        try:
            self.conn = sqlite3.connect(conexionDB)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

    def cierre_conexion(self):
        self.conn.close()
        print("Cierre de la base de datos exitoso.")

class IngresoPelicula:
    def __init__(self,conexion):
        self.conexion = conexion
    
    def nueva_pelicula(self):
        try:
            
            self.pelicula_name = str(input("Ingresa el nombre de la pelicula a reseñar y calificar: ")).strip()
            if not self.pelicula_name:
                print("No se pueden ingresar registros en blanco.")
                return

            self.conexion.cursor.execute("INSERT INTO movie_user(pelicula_name) VALUES (?)",(self.pelicula_name,))
            self.conexion.conn.commit()
            print(f"Nombre de la pelicula: {self.pelicula_name} subida con exito.")
        
        except Exception as error:
            print(f"Error en el programa: {error}.")
        
        except Exception as error:
            print(f"Error en la base de datos: {error}.")
    
    def nueva_reseña(self):
        try:
            self.reseña_usuario = str(input("Ingresa la reseña de la pelicula o serie: ")).strip()
            if not self.reseña_usuario:
                print("Los campos no pueden estar vacios.")
                return

            self.conexion.cursor.execute("SELECT pelicula_id FROM movie_user WHERE pelicula_name = ?",(self.pelicula_name,))
            pelicula = self.conexion.cursor.fetchone()
            if pelicula:
                pelicula_id = pelicula[0]
                self.conexion.cursor.execute("INSERT INTO reseña_user (reseña_usuario,pelicula_id) VALUES (?,?)",(self.reseña_usuario,pelicula_id))
                self.conexion.conn.commit()
                print("Reseña de la pelicula o serie subida con exito.")
        
        except Exception as error:
            print(f"Error en el programa: {error}.")
        except sqlite3.error as error:
            print(f"Error en la base de datos: {error}.")

    def calificacion_pelicula(self):
        try:

            self.calificacion_usuario = int(input("Ingresa una calificacion para la pelicula o serie (1-10): "))
            if not self.calificacion_usuario:
                print("No se puede tener el espacio en blanco.")
                return
            
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
    
        
    def subida_nube(self):
        try:

            self.api_key = "TU_API_KEY"
            self.database_id = "TU_DATA_BASE_ID"

            url = "https://api.notion.com/v1/pages"

            headers = {
                "Authorization" : f"Bearer {self.api_key}",
                "Content-type" : "application/json",
                "Notion-Version" : "2022-06-28"
            }

            data = {
                "parent" : {"database_id" : self.database_id},
                "properties" : {
                    "pelicula_name" : {
                        "title": [{
                            "text" : {"content" : self.pelicula_name}
                        }]
                    },
                    "reseña_usuario": {
                        "rich_text": [{
                            "text": {"content": self.reseña_usuario}
                        }]
                    },
                    "calificacion_usuario":{
                        "number": self.calificacion_usuario
                    }
                }
            }
            respuesta = requests.post(url=url, json=data, headers=headers)
            if 200 <= respuesta.status_code < 300 :
                print("Nombre de la pelicula o serie junto con su reseña y calificacion, subida con exito a la nube de Notion.")
            else:
                print(f"error: {respuesta.status_code}, {respuesta.text}")

        except Exception as error:
            print(f"Error en el programa: {error}.")


rutaDB = r"C:\Users\POWER\calificador_peliculas.db"
conexion = IngresoDB(rutaDB)



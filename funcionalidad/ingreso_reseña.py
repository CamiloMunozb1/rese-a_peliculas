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
        print("cierre de la base de datos exitoso.")

class IngresoReseña:
    def __init__(self, conexion):
        self.conexion = conexion

    def nueva_reseña(self):
        try:

            self.pelicula_name = str(input("Ingresa el nombre de la pelicula o serie a reseñar antes registrado: ")).strip()
            self.reseña_usuario = str(input("Ingresa la reseña de la pelicula o serie: ")).strip()
            if not self.pelicula_name or not self.reseña_usuario:
                print("Los campos no pueden estar vacios.")
                return
        
            self.api_key = "TU_API_KEY"
            self.database_id = "TU_DATABASE_ID"

            self.conexion.cursor.execute("SELECT pelicula_id FROM movie_user WHERE pelicula_name = ?",(self.pelicula_name,))
            pelicula = self.conexion.cursor.fetchone()
            if pelicula:
                pelicula_id = pelicula[0]
                self.conexion.cursor.execute("INSERT INTO reseña_user (reseña_usuario,pelicula_id) VALUES (?,?)",(self.reseña_usuario,pelicula_id))
                self.conexion.conn.commit()
                print("Reseña de la pelicula o serie subida con exito.")

        except Exception as error:
            print(f"Error en el programa: {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

    def subida_nube(self):
        try:

            url = "https://api.notion.com/v1/pages"
            
            headers = {
                "Authorization" : f"Bearer {self.api_key}",
                "Content-type" : "application/json",
                "Notion-Version" : "2022-06-28"
            }

            data = {
                "parent" : {"database_id" : self.database_id},
                "properties" : {
                    "reseña_usuario" : {
                        "rich_text" : [
                            {
                                "text" : {
                                    "content" : self.reseña_usuario
                                }
                            }
                        ]
                    }
                }
            }

            respuesta = requests.post(url=url, json=data, headers=headers)
            if 200 <= respuesta.status_code < 300:
                page_id = respuesta.json()["id"]
                print("Reseña de la pelicula o serie subida a la nube de Notion.")
                return page_id
            else:
                print(f"Error: {respuesta.status_code}, {respuesta.text}.")

        except Exception as error:
            print(f"Error en el programa : {error}.")


rutaDB = r"C:\Users\POWER\calificador_peliculas.db"
conexion = IngresoDB(rutaDB)




        
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
        
            self.api_key = "TU_API_KEY"
            self.database_id = "TU_API_KEY"

            self.conexion.cursor.execute("INSERT INTO movie_user(pelicula_name) VALUES (?)",(self.pelicula_name,))
            self.conexion.conn.commit()
            print(f"Nombre de la pelicula: {self.pelicula_name} subida con exito.")
        
        except Exception as error:
            print(f"Error en el programa: {error}.")
        
        except Exception as error:
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
                "properties":{
                    "pelicula_name" :{
                        "title":[
                            {
                                "text":{
                                    "content": self.pelicula_name
                                }
                            }
                        ]
                    }
                }
            }

            respuesta = requests.post(url=url, json=data, headers=headers)
            if 200 <= respuesta.status_code < 300 :
                page_id = respuesta.json()["id"]
                print("Nombre de la pelicula subida con exito a la nube de Notion.")
                return page_id
            else:
                print(f"error: {respuesta.status_code}, {respuesta.text}")

        except Exception as error:
            print(f"Error en el programa: {error}.")


rutaDB = r"C:\Users\POWER\calificador_peliculas.db"
conexion = IngresoDB(rutaDB)



import sqlite3
import pandas as pd

# Clase para conectarse a la base de datos SQLite
class IngresoDB:
    def __init__(self,conexionDB):
        try:
            self.conn = sqlite3.connect(conexionDB)
            self.cursor = self.conn.cursor()
        except sqlite3.error as error:
            print(f"Error en la base de datos: {error}.")
    
    def cierre_conexion(self):
        self.conn.close()
        print("Cierre de la base de exitoso.")  # mensaje de confirmación

# Clase encargada de mostrar las películas guardadas en la base de datos
class MostrarPeliculas:
    def __init__(self,conexion):
        self.conexion = conexion

    # Método que consulta y muestra las películas junto con su reseña y calificación
    def peliculas_registradas(self):
        try:
            # Consulta SQL que hace JOIN entre las 3 tablas usando el ID de la película
            query = """
                    SELECT
                        movie_user.pelicula_name,
                        reseña_user.reseña_usuario,
                        calificacion_user.calificacion_usuario
                    FROM movie_user
                    JOIN reseña_user ON movie_user.pelicula_id = reseña_user.pelicula_id
                    JOIN calificacion_user ON movie_user.pelicula_id = calificacion_user.pelicula_id
                """
            
            # Usamos pandas para hacer la consulta y convertirla en DataFrame
            resultado_df = pd.read_sql_query(query, self.conexion.conn)
            
            # Verificamos si hay resultados y los mostramos
            if not resultado_df.empty:
                print(resultado_df)
            else:
                print("No se encuentran peliculas o series, reseñas o calificacion.")
        
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

# Conexión a la base de datos local
rutaDB = r"C:\Users\POWER\calificador_peliculas.db"
conexion = IngresoDB(rutaDB)

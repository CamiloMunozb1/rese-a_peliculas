from funcionalidad.ingreso_pelicula import IngresoDB, IngresoPelicula
from funcionalidad.eliminar_pelicula import IngresoDB, EliminarPelicula
from funcionalidad.mostrar_peliculas import IngresoDB, MostrarPeliculas

rutaDB = r"C:\Users\POWER\calificador_peliculas.db"
conexion = IngresoDB(rutaDB)

while True:
    print(
        """
            Bienvenido al calificador de peliculas o serie.
            1. Ingresa una pelicula o serie.
            2. Eliminar pelicula o serie.
            3. Mostar peliculas o series registradas.
            4. Salir.
        """
    )
    try:

        usuario = str(input("Ingresa la opcion que desees: "))
        if not usuario:
            print("No se puede tener este campo en blanco, por favor ingresar una opcion valida.")
            break
        elif usuario == "1":
            ingreso = IngresoPelicula(conexion)
            ingreso.nueva_pelicula()
            ingreso.nueva_reseña()
            ingreso.calificacion_pelicula()
            ingreso.subida_nube()
        elif usuario == "2":
            eliminar = EliminarPelicula(conexion)
            eliminar.eliminacion_pelicula()
            eliminar.archivar_nube()
        elif usuario == "3":
            mostrar = MostrarPeliculas(conexion)
            mostrar.peliculas_registradas()
        elif usuario == "4":
            print("Gracias por usar el calificador de peliculas o series.")
            break
        else:
            print("Ingresa una opcion valida entre 1 a 4.")
        
        input("\nPresiona Enter para continuar...")

    except ValueError:
        print("Ingresa un valor valido.")
    except Exception as error:
        print(f"Error en el progama: {error}.")
        
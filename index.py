from funcionalidad.ingreso_pelicula import IngresoDB, IngresoPelicula



rutaDB = r"C:\Users\POWER\calificador_peliculas.db"
conexion = IngresoDB(rutaDB)

while True:
    print(
        """
            Bienvenido al calificador de peliculas o serie.
            1. Ingresa una pelicula o serie.
            2. Ingresa una reseña de la pelicula o serie.
            3. Ingresa una calificacion para la pelicula o serie.
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
            ingreso.subida_nube()
        elif usuario == "2":
            print("Proxima funcionalidad.")
        elif usuario == "3":
            print("Proxima funcionalidad.")
        elif usuario == "4":
            print("Gracias por usar el calificador de peliculas.")
            break
        else:
            print("Ingresa una opcion valida entre 1 a 4.")

    except ValueError:
        print("Ingresa un valor valido.")
    except Exception as error:
        print(f"Error en el progama: {error}.")
        
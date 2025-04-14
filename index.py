# Importación de clases desde los módulos correspondientes
from funcionalidad.ingreso_pelicula import IngresoDB, IngresoPelicula
from funcionalidad.eliminar_pelicula import IngresoDB, EliminarPelicula
from funcionalidad.mostrar_peliculas import IngresoDB, MostrarPeliculas

# Ruta local a la base de datos SQLite
rutaDB = r"C:\Users\POWER\calificador_peliculas.db"

# Inicializa la conexión con la base de datos
conexion = IngresoDB(rutaDB)

# Menú principal del sistema
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
        # Solicita al usuario que elija una opción del menú
        usuario = str(input("Ingresa la opcion que desees: ")).strip()

        # Verifica si el campo está vacío
        if not usuario:
            print("No se puede tener este campo en blanco, por favor ingresar una opcion valida.")
            break

        # Opción 1: Ingreso de nueva película o serie con reseña, calificación y subida a Notion
        elif usuario == "1":
            ingreso = IngresoPelicula(conexion)
            ingreso.nueva_pelicula()
            ingreso.nueva_reseña()
            ingreso.calificacion_pelicula()
            ingreso.subida_nube()

        # Opción 2: Eliminación de película/serie localmente y archivado en la nube
        elif usuario == "2":
            eliminar = EliminarPelicula(conexion)
            eliminar.eliminacion_pelicula()
            eliminar.archivar_nube()

        # Opción 3: Mostrar las películas o series registradas con sus detalles
        elif usuario == "3":
            mostrar = MostrarPeliculas(conexion)
            mostrar.peliculas_registradas()

        # Opción 4: Salida del programa
        elif usuario == "4":
            print("Gracias por usar el calificador de peliculas o series.")
            break

        # Validación en caso de opción no reconocida
        else:
            print("Ingresa una opcion valida entre 1 a 4.")

        # Pausa para que el usuario lea los resultados antes de volver al menú
        input("\nPresiona Enter para continuar...")

    # Manejo de error si se ingresa un tipo de dato incorrecto
    except ValueError:
        print("Ingresa un valor valido.")

    # Manejo de cualquier otro error inesperado
    except Exception as error:
        print(f"Error en el progama: {error}.")

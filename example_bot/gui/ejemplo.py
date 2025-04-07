import os
import sys

def importar_modulo_de_otra_carpeta(ruta_relativa_al_modulo):
    """
    Importa un módulo de Python desde una ruta de archivo dada, que es relativa
    al directorio del script que se está ejecutando.

    Args:
        ruta_relativa_al_modulo (str): La ruta al módulo que se va a importar,
            relativa al directorio del script actual.  Debe incluir el
            nombre del archivo del módulo.
            Por ejemplo: 'carpeta_a/subcarpeta_a1/modulo_a1.py'
    Returns:
        El módulo importado, o None si la importación falla.
    """
    # Obtiene la ruta absoluta del directorio del script actual.
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # Construye la ruta absoluta al módulo que queremos importar.
    ruta_absoluta_al_modulo = os.path.join(directorio_actual, ruta_relativa_al_modulo)

    # Obtiene el directorio del módulo (eliminando el nombre del archivo).
    directorio_del_modulo = os.path.dirname(ruta_absoluta_al_modulo)

    # Obtiene el nombre del módulo (sin la extensión .py).
    nombre_del_modulo = os.path.splitext(os.path.basename(ruta_absoluta_al_modulo))[0]

    # Agrega el directorio del módulo al sys.path para que Python lo pueda encontrar.
    sys.path.insert(0, directorio_del_modulo) # Insertar al frente para tener prioridad

    try:
        # Intenta importar el módulo usando importlib.import_module().
        # Esto es más robusto que usar __import__().
        import importlib.util
        spec = importlib.util.spec_from_file_location(nombre_del_modulo, ruta_absoluta_al_modulo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        return modulo
    except Exception as e:
        print(f"Error al importar el módulo {nombre_del_modulo} desde {ruta_absoluta_al_modulo}: {e}")
        return None
    finally:
        # Limpia el sys.path para evitar posibles conflictos con otras importaciones.
        if directorio_del_modulo in sys.path:
            sys.path.remove(directorio_del_modulo)

# Ejemplo de uso:
# Importa modulo_a1.py
modulo_a1 = importar_modulo_de_otra_carpeta("../features/indicators.py")

if modulo_a1:
    # Ahora puedes usar las funciones y clases de modulo_a1
    print(f"Módulo {modulo_a1.__name__} importado exitosamente.")
    # Si modulo_a1.py define una función llamada mi_funcion:
    # modulo_a1.mi_funcion()
else:
    print("No se pudo importar modulo_a1.py")


#Si tienes un paquete, por ejemplo
#mi_proyecto/
#    paquete_a/
#        __init__.py
#        modulo_a.py
#    carpeta_b/
#        script.py
#
# desde script.py puedes importar modulo_a usando:
#
# import sys
# import os
#
# # Obtiene el directorio del script actual
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir) # Un nivel arriba
# sys.path.append(parent_dir)
#
# from paquete_a import modulo_a
#
# modulo_a.mi_funcion()
#

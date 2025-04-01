
import sys
import os

# Obtiene la ruta absoluta del directorio padre
directorio_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), 'example_bot'))

# Agrega el directorio padre a sys.path
sys.path.append(directorio_padre)

# Ahora puedes importar mi_modulo
import features.cleaning as cleaning

cleaning.print_hello()
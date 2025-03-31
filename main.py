import sys
import os

# Obtiene el directorio del script actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre (la raíz del proyecto)
directorio_raiz = os.path.dirname(directorio_actual)
# Agrega el directorio raíz al sys.path
sys.path.append(directorio_raiz)

from example_bot.app import print

print.print_hello()

from example_bot.app.app2 import print_2

print_2.print_hello2()



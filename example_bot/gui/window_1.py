import tkinter as tk
from tkinter import ttk
import os

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa del ícono
icon_path = os.path.join(current_dir, "..", "..", "images", "icon.ico")

# Crear la ventana principal
root = tk.Tk()
root.title("Finance")
root.geometry("400x350")  # Tamaño de la ventana (ancho x alto)
# Establecer el ícono de la ventana
root.iconbitmap(icon_path)


# Etiqueta
label = tk.Label(root, text="¡Bienvenido a la interfaz gráfica!", font=("Arial", 14))
label.pack(pady=10)  # Agregar espacio vertical

# Entrada de texto
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Botón
def on_button_click():
    user_input = entry.get()
    label_result.config(text=f"Hola, {user_input}!")

button = tk.Button(root, text="Aceptar", command=on_button_click)
button.pack(pady=5)

# Etiqueta para mostrar resultados
label_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
label_result.pack(pady=10)

# Combobox (desplegable)
label_combobox = tk.Label(root, text="Selecciona una opción:")
label_combobox.pack(pady=5)

options = ["Opción 1", "Opción 2", "Opción 3"]
combobox = ttk.Combobox(root, values=options)
combobox.pack(pady=5)


# Iniciar el bucle principal de la aplicación
root.mainloop()

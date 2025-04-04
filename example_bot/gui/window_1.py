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
root.geometry("400x300")  # Tamaño de la ventana (ancho x alto)
# Establecer el ícono de la ventana
root.iconbitmap(icon_path)
# Cambiar el color de fondo de la ventana
root.configure(bg="white")

# Etiqueta
label = tk.Label(root, text="¡Bienvenido a la interfaz gráfica!", font=("Arial", 14), bg="white")
label.pack(pady=10)  # Agregar espacio vertical

# Crear un marco para organizar los botones y las flechas
frame = tk.Frame(root, bg="white")
frame.pack(pady=20)

# Funciones para cambiar el estilo del botón al pasar el mouse y al presionarlo
def on_enter(event):
    event.widget.config(bg="lightblue")

def on_leave(event):
    event.widget.config(bg="white")

def on_press(event):
    event.widget.config(bg="white", relief="sunken")

def on_release(event):
    event.widget.config(bg="white", relief="flat")

# Crear los botones y las flechas
for i in range(4):
    # Crear un marco para cada fila (flecha + botón)
    row_frame = tk.Frame(frame, bg="white")
    row_frame.pack(fill="x", pady=5)

    # Crear la flecha
    arrow_canvas = tk.Canvas(row_frame, width=20, height=20, bg="white", highlightthickness=0)
    arrow_canvas.pack(side="left", padx=5)
    arrow_canvas.create_line(5, 5, 15, 10, fill="black", width=2)  # Línea diagonal superior
    arrow_canvas.create_line(5, 15, 15, 10, fill="black", width=2)  # Línea diagonal inferior

    # Crear el botón
    button = tk.Button(row_frame, text=f"Botón {i + 1}", relief="flat", highlightthickness=0, bg="white")
    button.pack(side="left", padx=10)

    # Asociar eventos para cambiar el estilo del botón
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    button.bind("<ButtonRelease-1>", on_release)


# Iniciar el bucle principal de la aplicación
root.mainloop()

import tkinter as tk
from style import Style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class window_2(Style):
    """
    Clase secundaria.
    """
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.setup_window(geometry="700x575", resizable=True)
        self.create_widgets()
        
    def create_widgets(self):
        """
        Crea y organiza los widgets de la ventana.
        """
        label = tk.Label(self.root, text="Real-Time Signals", font=("Arial", 18, "bold"), bg=self.ventana_bg, fg=self.etiqueta_fg)
        label.pack(pady=(10, 0))

        frame = tk.Frame(self.root, bg=self.boton_bg)  # frame del botón
        frame.pack(pady=10, padx=10, anchor="nw")  # Ajusta la posición del frame a la parte superior izquierda

        # crea una fila con un botón
        options=['Option 1', 'Option 2', 'Option 3']
        self.create_dropdown_button(frame, options)

        self.create_button_row(frame, 1, 'Back')
        label.bind("<Enter>", self.on_enter_label)
        label.bind("<Leave>", self.on_leave_label)

    def create_button_row(self, parent, index, name_b):
        """
        Crea una fila con un botón.
        """
        row_frame = tk.Frame(parent, bg=self.boton_bg)
        row_frame.pack(fill="x", pady=2, side="left")

        button = tk.Button(row_frame, text=f"{name_b}", relief="flat", highlightthickness=0, bg=self.boton_bg, font=("Arial", 14), command=lambda: self.handle_button_click(index))
        button.pack(side="left", padx=2)
        button.config(borderwidth=0, highlightbackground=self.boton_bg, highlightcolor=self.boton_bg, highlightthickness=0)
        button.config(relief="flat", overrelief="flat", width=12, height=1, padx=5, pady=2, cursor="hand2")

        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)
        button.bind("<ButtonRelease-1>", self.on_release)

    def handle_button_click(self, index):
        """
        Maneja los clics en los botones.
        """
        if index == 0:  # Botón "Option 1"
            self.root.destroy()  # Cierra la ventana actual
            from window_1 import window_1  # Importa la clase de la ventana principal
            root = tk.Tk()
            app = window_1(root)  # Crea una instancia de la ventana principal
            root.mainloop()
            
        elif index == 1:  # Botón "Back"
            self.root.destroy()  # Cierra la ventana actual
            from window_1 import window_1  # Importa la clase de la ventana principal
            root = tk.Tk()
            app = window_1(root)  # Crea una instancia de la ventana principal
            root.mainloop()
        else:
            #print(f"Button {index + 1} clicked")
            pass

    def create_dropdown_button(self, parent, options, button_text="Select Option"):
        """
        Crea un botón que despliega una lista de selección.
        """
        dropdown_frame = tk.Frame(parent, bg=self.boton_bg)
        dropdown_frame.pack(fill="x", pady=2, side="left")

        # Variable para almacenar la opción seleccionada
        selected_option = tk.StringVar(value=button_text)

        # Botón principal que despliega el menú
        dropdown_button = tk.Menubutton(dropdown_frame, textvariable=selected_option, relief="flat", bg=self.boton_bg, font=("Arial", 14), cursor="hand2")
        dropdown_button.menu = tk.Menu(dropdown_button, tearoff=0, bg=self.boton_bg, font=("Arial", 12))
        dropdown_button["menu"] = dropdown_button.menu

        # Agregar opciones al menú
        for option in options:
            dropdown_button.menu.add_command(label=option, command=lambda opt=option: self.handle_dropdown_selection(opt, selected_option))

        dropdown_button.pack(side="left", padx=2)

    def handle_dropdown_selection(self, option, selected_option):
        """
        Maneja la selección de una opción del menú desplegable.
        """
        selected_option.set(option)
        print(f"Selected option: {option}")
        self.execute_action_based_on_option(option)

    def execute_action_based_on_option(self, option):
        """
        Ejecuta acciones específicas basadas en la opción seleccionada.
        """
        if option == "Option 1":
            self.show_plot()
        elif option == "Option 2":
            print("You selected Option 2!")
        elif option == "Option 3":
            print("You selected Option 3!")
        else:
            print("Unknown option selected!")

    def show_plot(self):
        """
        Muestra un gráfico de matplotlib en la interfaz gráfica.
        """
        import matplotlib.pyplot as plt

        # Datos de ejemplo
        x = [1, 2, 3, 4, 5]
        y = [10, 20, 25, 30, 40]

        # Crear la figura y el gráfico
        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o', linestyle='-', color='b')
        ax.set_title("Example Plot")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")

        # Integrar el gráfico en la ventana de tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(pady=10)

        # Dibujar el gráfico
        canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = window_2(root)
    root.mainloop()
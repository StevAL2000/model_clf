import tkinter as tk
from style import Style

class window_1(Style):
    """
    Clase principal que representa el menú de la aplicación finance.
    """
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.setup_window()
        self.create_widgets()

    def create_widgets(self):
        """
        Crea y organiza los widgets de la ventana.
        """
        label = tk.Label(self.root, text="Menu", font=("Arial", 22, "bold"), bg=self.ventana_bg, fg=self.etiqueta_fg)
        label.pack(pady=(20, 0))

        frame = tk.Frame(self.root, bg=self.boton_bg)
        frame.pack(pady=20, side='left', padx=40)

        buttons = ['Real-Time Signals', 'Backtest Create', 'Backtest Load', 'Exit']
        for i in range(len(buttons)):
            name_b = buttons[i]
            self.create_row(frame, i, name_b)

        label.bind("<Enter>", lambda event: self.on_enter_label(event))
        label.bind("<Leave>", self.on_leave_label)

    def create_row(self, parent, index, name_b):
        """
        Crea una fila 
        """
        row_frame = tk.Frame(parent, bg=self.boton_bg)
        row_frame.pack(fill="x", pady=5)

        button = tk.Button(row_frame, text=f"{name_b}", relief="flat", highlightthickness=0, bg=self.boton_bg, font=("Arial", 14), command=lambda: self.handle_button_click(index))
        button.pack(side="left", padx=5)
        button.config(borderwidth=0, highlightbackground=self.boton_bg, highlightcolor=self.boton_bg, highlightthickness=0)
        button.config(relief="flat", overrelief="flat", width=18, height=1, padx=10, pady=2, cursor="hand2")

        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)
        button.bind("<ButtonRelease-1>", self.on_release)

    def handle_button_click(self, index):
            
            """
            Maneja los clics en los botones.
            """

            if index == 0:  # Botón "Option 1"
                self.root.destroy()  # Cierra la ventana actual
                from window_2 import window_2  # Importa la clase de la ventana principal
                root = tk.Tk()
                app = window_2(root)  # Crea una instancia de la ventana principal
                root.mainloop()

            elif index == 1:  # Botón "Option 1"
                self.root.destroy()  # Cierra la ventana actual
                from window_3 import window_3  # Importa la clase de la ventana principal
                root = tk.Tk()
                app = window_3(root)  # Crea una instancia de la ventana principal
                root.mainloop()

            elif index == 2:  # Botón "Option 1"
                self.root.destroy()  # Cierra la ventana actual
                from window_4 import window_4  # Importa la clase de la ventana principal
                root = tk.Tk()
                app = window_4(root)  # Crea una instancia de la ventana principal
                root.mainloop()                
                
            elif index == 3:  # Botón "Exit"
                self.root.destroy()  # Cierra la ventana actual
                
            else:
                #print(f"Button {index + 1} clicked")
                pass



if __name__ == "__main__":
    root = tk.Tk()
    app = window_1(root)
    root.mainloop()

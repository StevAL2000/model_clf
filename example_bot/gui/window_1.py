import tkinter as tk
import os
import window_2

class Style:
    """
    Clase padre que define los estilos compartidos.
    """
    ventana_bg = "#b0f6b7"
    boton_bg = "#d7ffbf"
    boton_hover_bg = "#b8fe8e"
    boton_click_bg = "#f9f1e8"
    etiqueta_fg = "Black"
    etiqueta_hover_fg = "#006333"
    tooltip_bg = "white"


class FinanceApp(Style):
    """
    Clase principal que representa la aplicación de la ventana de finance.
    """
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        """
        Configura la ventana principal de la aplicación.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, "..", "..", "images", "icon.ico")

        self.root.title("Finance")
        self.root.geometry("300x275")
        self.root.iconbitmap(icon_path)
        self.root.configure(bg=self.ventana_bg)
        self.root.resizable(False, False)
        self.center_window()

    def center_window(self):
        """
        Centra la ventana en la pantalla.
        """
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        size = tuple(int(_) for _ in self.root.geometry().split('+')[0].split('x'))
        x = (screen_width - size[0]) // 2
        y = (screen_height - size[1]) // 2
        self.root.geometry(f"{size[0]}x{size[1]}+{x}+{y}")

    def create_widgets(self):
        """
        Crea y organiza los widgets de la ventana.
        """
        label = tk.Label(self.root, text="Menu", font=("Arial", 22, "bold"), bg=self.ventana_bg, fg=self.etiqueta_fg)
        label.pack(pady=(20, 0))

        frame = tk.Frame(self.root, bg=self.boton_bg)
        frame.pack(pady=20, side='left', padx=40)

        buttons = ['Real-Time Signals', 'Backtest Create', 'Backtest Visual', 'Exit']
        for i in range(len(buttons)):
            name_b = buttons[i]
            self.create_row(frame, i, name_b)

        label.bind("<Enter>", self.on_enter_label)
        label.bind("<Leave>", self.on_leave_label)

    def create_row(self, parent, index, name_b):
        """
        Crea una fila con una flecha, un botón 
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
                from window_2 import NewWindow  # Importa la clase de la ventana principal
                root = tk.Tk()
                app = NewWindow(root)  # Crea una instancia de la ventana principal
                root.mainloop()
                
            elif index == 3:  # Botón "Exit"
                self.root.destroy()  # Cierra la ventana actual
            else:
                print(f"Button {index + 1} clicked")

    @staticmethod
    def on_enter(event):
        event.widget.config(bg=Style.boton_hover_bg)

    @staticmethod
    def on_leave(event):
        event.widget.config(bg=Style.boton_bg)

    @staticmethod
    def on_release(event):
        event.widget.config(bg=Style.boton_click_bg, relief="flat")

    @staticmethod
    def on_enter_label(event):
        event.widget.config(fg=Style.etiqueta_hover_fg)

    @staticmethod
    def on_leave_label(event):
        event.widget.config(fg=Style.etiqueta_fg)


if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceApp(root)
    root.mainloop()

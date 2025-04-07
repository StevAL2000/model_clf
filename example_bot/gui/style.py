import os

class Style:
    def __init__(self):
        """
        Clase padre que define los estilos compartidos.
        """
        self.ventana_bg = "#b0f6b7"
        self.boton_bg = "#d7ffbf"
        self.boton_hover_bg = "#b8fe8e"
        self.boton_click_bg = "#f9f1e8"
        self.etiqueta_fg = "Black"
        self.etiqueta_hover_fg = "#006333"
        self.tooltip_bg = "white"

    def setup_window(self, geometry="300x275"):
        """
        Configura la ventana principal de la aplicación.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, "..", "..", "images", "icon.ico")

        self.root.title("Finance")
        self.root.geometry(geometry)
        self.root.iconbitmap(icon_path)
        self.root.configure(bg=self.ventana_bg)
        self.root.resizable(False, False)
        self.center_window()

    def on_enter(self,event):
        event.widget.config(bg=self.boton_hover_bg)

    def on_leave(self,event):
        event.widget.config(bg=self.boton_bg)

    def on_release(self,event):
        event.widget.config(bg=self.boton_click_bg, relief="flat")

    def on_enter_label(self, event):
        event.widget.config(fg=self.etiqueta_hover_fg)

    def on_leave_label(self,event):
        event.widget.config(fg=self.etiqueta_fg)

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

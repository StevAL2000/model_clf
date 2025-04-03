'Aqui vamos a colocar la lógica de nuestro bot incluyendo el modelo y el panel visual'

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Hello World App")

    label = tk.Label(root, text="Hello, world!", font=("Arial", 16))
    label.pack(pady=20)

    root.mainloop()
    
def training():
    pass

def inference():
    pass


if __name__ == "__main__":
    main()
    training()
    inference()
    

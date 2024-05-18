import tkinter as tk
import ctypes

# Configurando DPI
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception as e:
    print(e)

# Aplicação

main_screen = tk.Tk()
main_screen.mainloop()

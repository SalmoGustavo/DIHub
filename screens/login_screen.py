import tkinter as tk
import customtkinter as ct

ct.set_appearance_mode('dark')
ct.set_default_color_theme('dark-blue')


class LoginScreen:
    def __init__(self):
        self.window = ct.CTk()
        self.window.geometry('883x520')
        self.set_widgets()

    def set_widgets(self):
        image = tk.PhotoImage(file='images/dihub.png')

        ct.CTkLabel(self.window, text=' ').pack()

        widimage = ct.CTkLabel(self.window, image=image, text=' ')
        widimage.pack()

        entry_username = ct.CTkEntry(self.window, placeholder_text='Insira seu nome de usuário...',
                                     width=280)
        entry_username.pack(padx=10, pady=(self.window.winfo_height() / 2, 10))

        entry_password = ct.CTkEntry(self.window, placeholder_text='Insira sua senha...',
                                     width=280)
        entry_password.pack(padx=10, pady=10)

        login_button = ct.CTkButton(self.window, text='Entrar')
        login_button.pack()

    def run(self):
        self.window.mainloop()


# Criar instância e executar a aplicação
app = LoginScreen()
app.run()

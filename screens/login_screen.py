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

        widimage = ct.CTkLabel(self.window, image=image, text=' ', pady=50)
        widimage.pack()

        self.status = ct.CTkLabel(self.window, text='', font=('default', 20), text_color='red')
        self.status.pack()

        self.entry_username = ct.CTkEntry(self.window, placeholder_text='Insira seu nome de usuário...', width=280)
        self.entry_username.pack(padx=10, pady=10)

        self.entry_password = ct.CTkEntry(self.window, placeholder_text='Insira sua senha...',
                                     width=280)
        self.entry_password.pack(padx=10, pady=10)

        login_button = ct.CTkButton(self.window, text='Entrar', command=self.login)
        login_button.pack()

    def run(self):
        self.window.mainloop()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        print(f'Username: {username}\nPassword: {password}')

        if username != 'salmogustavo' or password != '2808':
            self.status.configure(text_color='red')
            self.status.configure(text='Usuário ou senha incorretos.')
        else:
            self.status.configure(text_color='lightgreen')
            self.status.configure(text='Bem vindo!')

# Criar instância e executar a aplicação
app = LoginScreen()
app.run()

import tkinter as tk
import ctypes
from screens.login_screen import LoginScreen

class App:
    def __init__(self):
        self.screens = {'login': LoginScreen()}
        self.current = 'login'

    def run(self):
        self.screens[self.current].run()


if __name__ == '__main__':
    App().run()

from search_file import Search_number
import tkinter as tk
from tkinter import scrolledtext
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox
from functools import partial
import re

class Window_login_pass:
    def __init__(self):
        # Window
        tkWindow = tk.Tk()
        w = tkWindow.winfo_screenwidth()
        h = tkWindow.winfo_screenheight()
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 300  # смещение от середины
        h = h - 200
        tkWindow.geometry(f'400x150+{w}+{h}')
        tkWindow.title('- Введите логин и пароль учетной записи -')

        # Username label and text entry box
        self.usernameLabel = Label(tkWindow, text="Логин").grid(row=0, column=0)
        self.username = StringVar()
        self.usernameEntry = Entry(tkWindow, textvariable=self.username).grid(row=0, column=1)

        # Password label and password entry box
        self.passwordLabel = Label(tkWindow, text="Пароль").grid(row=1, column=0)
        self.password = StringVar()
        self.passwordEntry = Entry(tkWindow, textvariable=self.password, show='*').grid(row=1, column=1)

        # pass arguments from button
        self.validateLogin = partial(self.validateLogin, self.username, self.password)

        # Login button
        self.loginButton = Button(tkWindow, text="Login", command=self.validateLogin).grid(row=4, column=0)

        tkWindow.mainloop()

    def validateLogin(self, username, password):
        print("username entered :", self.username.get())
        print("password entered :", self.password.get())
        self.showMsg()


        return

    def showMsg(self):
        messagebox.showinfo('Message', 'You clicked the Submit button!')

class Window_search_file:
    def __init__(self, root):


        self.root = root
        self.root.title("Система вывода информации абонента")

        self.input_label = tk.Label(self.root, text="Введите искомый номер:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.submit_button = tk.Button(self.root, text="поиск", command=self.show_output)
        self.submit_button.pack()
        self.output_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)

    def show_output(self):
        input_text = self.input_entry.get()
        search_number = re.sub("[^0-9]", "", input_text)
        enemy = Search_number(search_number)
        enemy.read_path_file()
        result = enemy.output()

        for row in result:
            self.output_text.insert(tk.END, f"{row}\n")
            self.output_text.pack()






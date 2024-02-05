from app import Window_search_file
from app import Window_login_pass
import tkinter as tk

if __name__ == "__main__":

    # Window login
    tkWindow = tk.Tk()
    w = tkWindow.winfo_screenwidth()
    h = tkWindow.winfo_screenheight()
    w = w // 2  # середина экрана
    h = h // 2
    w = w - 300  # смещение от середины
    h = h - 200
    tkWindow.geometry(f'400x150+{w}+{h}')
    tkWindow.title('- Введите логин и пароль учетной записи -')
    app_login = Window_login_pass(tkWindow)
    tkWindow.mainloop()

    # Window programm
    root = tk.Tk()
    w2 = root.winfo_screenwidth()
    h2 = root.winfo_screenheight()
    w2 = w2 // 2  # середина экрана
    h2 = h2 // 2
    w2 = w2 - 300  # смещение от середины
    h2 = h2 - 200
    root.geometry(f'600x400+{w2}+{h2}')
    app = Window_search_file(root)
    root.mainloop()





# 6-27-74
# 5-17-26
# 5-41-81
# 5-14-86
# 5-55-83

# 5-53-83
# 5-46-03

# 777141




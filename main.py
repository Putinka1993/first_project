from app import Graphic_interface
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2  # середина экрана
    h = h // 2
    w = w - 500  # смещение от середины
    h = h - 200
    root.geometry(f'1000x400+{w}+{h}')
    app = Graphic_interface(root)
    root.mainloop()





# 6-27-74
# 5-17-26
# 5-41-81
# 5-14-86
# 5-55-83

# 5-53-83
# 5-46-03

# 777141




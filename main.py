from app import Graphic_interface
import tkinter as tk

def main():

    root = tk.Tk()
    app = Graphic_interface(root)
    root.mainloop()

main()




# 6-27-74
# 5-17-26
# 5-41-81
# 5-14-86
# 5-55-83








# book = openpyxl.open("table.xlsx", read_only=True)


# phone = input("Введите номер телефона:")
# convert = ''
# flag = True
# for num in phone:
#     if flag:
#         convert += num
#         convert += "-"
#         flag = False
#     else:
#         convert += num
#         flag = True
#
# convert = convert.rstrip("-")
# for row in range(1, 708):
#     if sheet[row][1].value == convert:
#         print(f"Строка: {row}")
#
# for row in sheet:
#     if row[0].value == "$":
#         print(row[1].value)
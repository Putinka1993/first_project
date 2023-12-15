import openpyxl
import re
import os
import tkinter as tk


class Search_number:

    def __init__(self, search_number):
        self.search_number = search_number#re.sub("[^0-9]", "", input("Введите номер: "))
        self.data = {}
        print(f"По запросу {self.search_number}")

    def read_path_file(self):
        directory = "/Users/vladislavlipkin/Desktop/data/"

        for file in os.listdir(directory):
            if file.endswith(".xlsx"):
                book = openpyxl.open(f"/Users/vladislavlipkin/Desktop/data/{file}", read_only=True)
                sheet = book.active

                for row in sheet:
                    if row[0].value == "$":
                        key_name = row[1].value
                    left_number = re.sub("[^0-9]", "", str(row[1].value))
                    right_number = re.sub("[^0-9]", "", str(row[6].value))

                    if left_number == self.search_number:
                        self.data[key_name] = str(
                            f"номер телефона {str(row[1].value)}, "
                            f"номер пары {str(row[0].value)}, "
                            f"адрес кросс.параллели {str(row[2].value)}, "
                            f"номер помещения {str(row[3].value)}")
                        # print(file)
                        # print("LEFT")

                    if right_number == self.search_number:
                        self.data[key_name] = str(
                            f"номер телефона {str(row[6].value)}, "
                            f"номер пары {str(row[5].value)}, "
                            f"адрес кросс.параллели {str(row[7].value)}, "
                            f"номер помещения {str(row[8].value)}")
                        # print(file)
                        # print("RIGHT")
    def output(self):
        return self.data



# 6-27-74
# 5-17-26
# 5-41-81
# 5-14-86
# 5-55-83

class Graphic_interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Input Output App")

        self.input_label = tk.Label(self.root, text="Enter Text:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.show_output)
        self.submit_button.pack()

    def show_output(self):
        input_text = self.input_entry.get()
        search_number = re.sub("[^0-9]", "", input_text)
        enemy = Search_number(search_number)
        enemy.read_path_file()
        result = enemy.output()
        for k, v in result.items():
            output_label = tk.Label(self.root, text=f"название оборудования {k} {v}")
            output_label.pack()




def main():

    root = tk.Tk()
    app = Graphic_interface(root)
    root.mainloop()

    # while 1 != 0:
    #     graphic = Graphic_interface()
    #     enemy = Search_number(graphic.search_number)
    #     enemy.read_path_file()
    #     enemy.output()

main()








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
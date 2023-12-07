import openpyxl
import re
import os

# Work main programm
def main():
    #
    enemy = Search_number()
    enemy.read_path_file()

    print(enemy.output())

class Search_number:

    def __init__(self):
        self.search_number = re.sub("[^0-9]", "", input("Введите номер: "))
        self.data = {}
        print(f"По запросу {self.search_number}")

    def read_path_file(self):
        directory = "/Users/vladislavlipkin/Desktop/data/"

        for file in os.listdir(directory):
            if file.endswith(".xlsx"):
                print(file)
                book = openpyxl.open(f"/Users/vladislavlipkin/Desktop/data/{file}", read_only=True)
                sheet = book.active

                for row in sheet:
                    if row[0].value == "$":
                        # print(f"-{row[0].value}-")
                        equipment_name = str(row[1].value)
                    number = re.sub("[^0-9]", "", str(row[1].value))
                    if number == self.search_number:
                        self.data[file] = str(
                            f"оборудование {equipment_name}, номер телефона {str(row[1].value)}, "
                            f"номер пары {str(row[0].value)}, "
                            f"адрес кросс.параллели {str(row[2].value)}, "
                            f"номер помещения {str(row[3].value)}")

    def output(self):
        return self.data



# 6-27-74

class Graphic_interface:
    pass



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
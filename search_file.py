import openpyxl
import re
import os

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
                        self.data[f"имя файла - {file} - оборудование - {key_name}"] = str(
                            f"номер телефона {str(row[1].value)}, "
                            f"номер пары {str(row[0].value)}, "
                            f"адрес кросс.параллели {str(row[2].value)}, "
                            f"номер помещения {str(row[3].value)}")
                        # print(file)
                        # print("LEFT")

                    if right_number == self.search_number:
                        self.data[f"имя файла - {file} - оборудование - {key_name}"] = str(
                            f"название файла {file}"
                            f"номер телефона {str(row[6].value)}, "
                            f"номер пары {str(row[5].value)}, "
                            f"адрес кросс.параллели {str(row[7].value)}, "
                            f"номер помещения {str(row[8].value)}")
                        # print(file)
                        # print("RIGHT")
    def output(self):
        return self.data




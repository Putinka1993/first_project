import openpyxl
import re
import os

class Search_number:

    # initialization
    def __init__(self, search_number):
        self.search_number = search_number
        self.data = []

        # the root folder
        self.DIRECTORY = "/Users/vladislavlipkin/Desktop/data/"

    def read_path_file(self):

        for file in os.listdir(self.DIRECTORY):
            if file.endswith(".xlsx"):
                book = openpyxl.open(f"/Users/vladislavlipkin/Desktop/data/{file}", read_only=True)
                sheet = book.active

                for row in sheet:
                    if row[0].value == "$":
                        key_name = row[1].value
                    left_number = re.sub("[^0-9]", "", str(row[1].value))
                    right_number = re.sub("[^0-9]", "", str(row[6].value))

                    if left_number == self.search_number:
                        self.data.append(str(
                            f"номер телефона {str(row[1].value)} - "#номер 
                            f"расположение {key_name} - "# расположение
                            f"пара {str(row[0].value)} - "# пара 
                            f"адрес кросс.параллели {str(row[2].value)} - "# адресс кросс 
                            f"помещение {str(row[3].value)} - " # помещение 
                            f"( файла {file} )")) # имя файла
                        self.data.append(str(""))

                    if right_number == self.search_number:
                        self.data.append(str(
                            f"номер телефона {str(row[6].value)} - " # номер
                            f"расположение {key_name} - "# расположение
                            f"пара {str(row[5].value)} - "# пара
                            f"адрес кросс.параллели {str(row[7].value)} - " # адресс кросс
                            f"помещение {str(row[8].value)} - "# помещение 
                            f"( файл {file} )")) # имя файла
                        self.data.append(str(""))

    def output(self):
        if len(self.data) == 0:
            self.data.append(f"по запросу {self.search_number} ничего не найдено!")
            self.data.append(str(""))
        return self.data




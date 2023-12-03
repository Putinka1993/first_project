import openpyxl
import re
import os

directory = "/Users/vladislavlipkin/Desktop/data/"
for file in os.listdir(directory):
    if file.endswith(".xlsx"):
        print(file)
        book = openpyxl.open(f"/Users/vladislavlipkin/Desktop/data/{file}", read_only=True)
        sheet = book.active

        search_number = re.sub("[^0-9]", "", input("Введите номер: "))
        for row in sheet:
            if row[0].value == "$":
                equipment_name = str(row[1].value)
            number = re.sub("[^0-9]", "",  str(row[1].value))
            if number == search_number:
                print(f"оборудование {equipment_name}, номер телефона {str(row[1].value)}, номер бокса {str(row[0].value)}, "
                      f"адрес кросс. параллели {str(row[3].value)}")

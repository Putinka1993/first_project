
import openpyxl

# book = openpyxl.open("table.xlsx", read_only=True)
book = openpyxl.open("/Users/vladislavlipkin/Desktop/data/кросс_зд_602,пом_104.xlsx", read_only=True)
sheet = book.active

phone = input("Введите номер телефона:")
convert = ''
flag = True
for num in phone:
    if flag:
        convert += num
        convert += "-"
        flag = False
    else:
        convert += num
        flag = True

convert = convert.rstrip("-")
for row in range(1, 708):
    if sheet[row][1].value == convert:
        print(f"Строка: {row}")

# for row in sheet:
#     print(row[1].value)
from search_file import Search_number
import tkinter as tk
from tkinter import scrolledtext
import re

class Graphic_interface:
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




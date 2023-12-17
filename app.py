from search_file import Search_number
import tkinter as tk
import re

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
        if not result:
            output_label = tk.Label(self.root, text=f"по запросу {search_number} ничего не найдено!")
            output_label.pack()
        else:
            for k, v in result.items():
                output_label = tk.Label(self.root, text=f"{k} {v}")
                output_label.pack()





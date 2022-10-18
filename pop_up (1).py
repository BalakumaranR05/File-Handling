from tkinter import *


class Pop_up:
    def __init__(self, text_value, root):
        self.text_value = text_value
        self.top = Toplevel(root)
        self.top.config(padx=50, pady=50)
        text_label = Label(self.top, text=text_value, font=("Arial", 12, "bold"))
        text_label.grid(column=0, row=0)

        ok_button = Button(self.top, text="OK", command=self.destroy_top)
        ok_button.grid(column=0, row=2)

    def destroy_top(self):
        self.top.destroy()



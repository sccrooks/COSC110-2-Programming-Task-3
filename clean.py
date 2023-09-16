from tkinter import *
import tkinter as tk


class RatingButtons(tk.Frame):
    pass


def button_clicked(rating):
    return


def create_rating_buttons(number_of_buttons, tk_window):
    for i in range(number_of_buttons):
        btn = tk.Button(tk_window, text=str(i), command=button_clicked(i))
        btn.pack()


class Application(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


if __name__ == "__main__":
    root = tk.Tk()

cleanliness_average = 0

window = tk.Tk()

main_title_str = "Rate the cleanliness of this bus:"
cleanliness_average_str = "This bus has an average cleanliness rating of {}"

window.mainloop()

from tkinter import *
import tkinter as tk


class RatingUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class AverageRating(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class Application(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.ratings_ui = RatingUI(self, ...)

        self.ratings_ui.pack(fill="x")


if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(expand=True)
    root.mainloop()

cleanliness_average = 0

main_title_str = "Rate the cleanliness of this bus:"
cleanliness_average_str = "This bus has an average cleanliness rating of {}"

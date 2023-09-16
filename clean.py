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
        self.cleanliness_average_str = "This bus has an average cleanliness rating of {}"


class Application(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.greeting = tk.Label(text="Rate the cleanliness of this bus:")
        self.ratings_ui = RatingUI(self)
        self.average_rating = AverageRating(self)

        self.greeting.pack()
        self.ratings_ui.pack(fill="x")
        self.average_rating.pack()


cleanliness_average = 0

if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(expand=True)
    root.mainloop()





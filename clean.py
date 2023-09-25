from tkinter import *
import tkinter as tk

class RatingSystem:
    def __init__(self):
        self.total_ratings = 0
        self.number_of_ratings = 0
        self.average_rating = self.calculate_average()

    def add_rating(self, value: float) -> None:
        """
        add_rating adds a new rating to the rating system
        :param value: Value of new rating
        """
        self.total_ratings += value
        self.number_of_ratings += 1
        self.average_rating = self.calculate_average()

    def calculate_average(self) -> float:
        """
        calculate_average calculates the average of the total ratings added into
        the rating system.
        :return: average rating (float)
        """
        return self.total_ratings / self.number_of_ratings

class RatingUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        for i in range(1, 6):
            rating_button = Button(self, text=str(i), command=lambda k=i: self.add_rating(k))
            rating_button.grid(row=0, column=i)

    def add_rating(self, value):
        Tk.update(self)


class AverageRating(tk.Frame):
    def __init__(self, parent, average_rating, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.average_rating = average_rating
        self.parent = parent

        self.cleanliness_average_str = "This bus has an average cleanliness rating of {}"
        lbl = tk.Label(text="")
        lbl.config(text="ww")
        lbl.pack()


class Application(tk.Frame):
    """
    Core tk.Frame for this application.

    Attributes:
        parent: Parent of this tk.Frame
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.total_rating = 0

        self.create_widgets()

    def create_widgets(self):
        """
        Inits Application widgets
        """
        tk.Label(text="Rate the cleanliness of this bus:").pack(fill="x")
        RatingUI(self).pack(fill="x")
        AverageRating(self, 0).pack(fill="x")

    def add_rating(self, value):




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bus Cleanliness App")
    Application(root).pack(expand=True)
    root.mainloop()

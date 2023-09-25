from tkinter import *
import tkinter as tk


class RatingSystem:
    """
    Rating System is used for tracking all ratings for a specific bus.
    """

    def __init__(self):
        self.total_ratings = 0
        self.number_of_ratings = 0
        self.average_rating = self.calculate_average()

    def add_rating(self, value: float) -> None:
        """
        add_rating adds a new rating to the rating system.
        :param value: Value of new rating.
        """
        self.total_ratings += value
        self.number_of_ratings += 1
        self.average_rating = self.calculate_average()

    def calculate_average(self) -> float:
        """
        calculate_average calculates the average of the total ratings added into
        the rating system.
        :return: average rating (float).
        """

        # Ensures a division by zero error does not occur.
        if self.number_of_ratings > 0:
            return self.total_ratings / self.number_of_ratings
        else:
            return 0


class RatingUI(tk.Frame):
    """
    tk.Frame widget for creating the rating ui buttons.

    Attributes:
        parent: parent of this tk.Frame.
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.create_buttons()

    def create_buttons(self) -> None:
        """
        create_buttons creates the buttons for this widget.
        """
        for i in range(1, 6):
            rating_button = Button(self, text=str(i), command=lambda k=i: self.parent.add_rating(k), width=10)
            rating_button.grid(row=0, column=i, padx=2)


class Application(tk.Frame):
    """
    Core tk.Frame for this application.

    Attributes:
        parent: Parent of this tk.Frame
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.ratings = RatingSystem()
        self.average_rating_label = Label(text="")
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Inits Application widgets
        """
        tk.Label(text="Rate the cleanliness of this bus:").pack(fill="x")
        RatingUI(self).pack(fill="x")
        self.average_rating_label.config(text=self.create_rating_label_string())
        self.average_rating_label.pack(fill="x")

    def create_rating_label_string(self) -> str:
        """
        Creates and formats the average rating label string.
        :return: Average rating string
        """
        avg_rating = round(self.ratings.average_rating, 2)
        return "This bus has an average cleanliness rating of {}".format(avg_rating)

    def add_rating(self, value: float) -> None:
        """
        Adds a new rating to the rating system AND updates average_rating_label.
        :param value: Value of new rating
        """
        self.ratings.add_rating(value)
        self.average_rating_label.config(text=self.create_rating_label_string())


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bus Cleanliness App")
    Application(root).pack(expand=True)
    root.mainloop()

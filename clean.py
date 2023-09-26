from tkinter import *
import tkinter as tk


class RatingSystem:
    """
    Rating System is used for tracking all ratings for a specific bus.

    Attributes:
        total_ratings: Total of all ratings added together.
        number_of_ratings: Count of ratings inputted into system
        average_rating: Value of average rating (total_ratings / number_of_ratings)
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


class RatingWidget(tk.Frame):
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


class AverageRatingWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.label = Label(text="")
        self.label.pack()
        self.update_average(0)

    def update_average(self, average_rating: float) -> None:
        """
        Updates this widget with a new average rating.
        :param average_rating: New average rating.
        """
        avg_rating = round(average_rating, 2)
        content = "This bus has an average cleanliness rating of {}".format(avg_rating)

        self.label.config(text=content)


class Application(tk.Frame):
    """
    Core tk.Frame for this application.

    Attributes:
        parent: Parent of this tk.Frame
        rating_system: Stores and performs calculations on ratings
        greetings: Greeting label
        rating_widget: Instance of RatingWidget
        average_rating_widget: Instance of AverageRatingWidget
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.rating_system = RatingSystem()

        # Widgets
        self.greetings = tk.Label(text="Rate the cleanliness of this bus:")
        self.rating_widget = RatingWidget(self)
        self.average_rating_widget = AverageRatingWidget(self)

        # Packing
        self.greetings.pack(fill="x")
        self.rating_widget.pack(fill="x")
        self.average_rating_widget.pack(fill="x")

    def add_rating(self, value: float) -> None:
        """
        Adds a new rating to the rating system AND updates average_rating_label.
        :param value: Value of new rating
        """
        self.rating_system.add_rating(value)
        self.average_rating_widget.update_average(self.rating_system.average_rating)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bus Cleanliness App")
    Application(root).pack(expand=True)
    root.mainloop()

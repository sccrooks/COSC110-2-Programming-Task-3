from tkinter import *
import tkinter as tk


class Rating:
    def __init__(self):
        self.num_of_ratings = 0
        self.totalRatings = 0

    def add_ratings(self, rating):
        self.totalRatings += rating
        self.num_of_ratings += 1

    def get_average_rating(self):
        return self.totalRatings / self.num_of_ratings

    def get_num_of_ratings(self):
        return self.num_of_ratings


class RatingUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        global cleanliness_rating

        btn = Button(self, text="1", command=lambda: cleanliness_rating.add_ratings(5))
        btn.pack()


class AverageRating(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        global cleanliness_rating
        self.cleanliness_average_str = "This bus has an average cleanliness rating of {}"

        if cleanliness_rating.get_num_of_ratings() > 0:
            lbl = tk.Label(text=self.cleanliness_average_str.format(cleanliness_rating.get_average_rating()))
            lbl.pack()


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


cleanliness_rating = Rating()

if __name__ == "__main__":
    root = tk.Tk()
    Application(root).pack(expand=True)
    root.mainloop()

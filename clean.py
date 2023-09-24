from tkinter import *
import tkinter as tk


class Rating:
    def __init__(self):
        self.num_of_ratings = 0
        self.totalRatings = 0

    def add_ratings(self, rating):
        self.totalRatings += rating
        self.num_of_ratings += 1
        print(str(self.totalRatings) + "NoR:" + str(self.num_of_ratings))

    def get_average_rating(self):
        return self.totalRatings / self.num_of_ratings

    def get_num_of_ratings(self):
        return self.num_of_ratings


class RatingUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        for i in range(1, 6):
            rating_button = Button(self, text=str(i), command=lambda k=i: self.add_rating(k))
            rating_button.grid(row=0, column=i)

    def add_rating(self, value):
        global cleanliness_rating
        cleanliness_rating.add_ratings(value)
        Tk.update(self)


class AverageRating(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        global cleanliness_rating
        self.cleanliness_average_str = "This bus has an average cleanliness rating of {}"
        lbl = tk.Label(text="")

        if cleanliness_rating.get_num_of_ratings() > 0:
            lbl.config(text=self.cleanliness_average_str.format(cleanliness_rating.get_average_rating()))
            lbl.pack()


class Application(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        tk.Label(text="Rate the cleanliness of this bus:").pack(fill="x")
        RatingUI(self).pack(fill="x")
        AverageRating(self).pack(fill="x")


cleanliness_rating = Rating()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bus Cleanliness App")
    Application(root).pack(expand=True)
    root.mainloop()

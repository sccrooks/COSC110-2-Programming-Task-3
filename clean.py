import tkinter as tk

window = tk.Tk()

main_title_str = "Rate the cleanliness of this bus:"
main_title = tk.Label(text=main_title_str)
main_title.pack()

cleanliness_average = "This bus has an average cleanliness rating of {}"

window.mainloop()

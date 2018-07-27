"""
The front end for the redds gallery app
divider creates a divider for visual purposes
fill_desc fills the description from the database
fill_art fills the artwork from the database
fill_page calls fill_desc and fill_art to create the page

written by: Matthew Lopez
"""

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import back_end


def divider(col, row):
    """
    An easy way to create a header
    :param col: the column you'd like to have it start
    :param row: the row you'd like to have it start
    :return: none
    """
    ttk.Label(mainframe, text="-"*90).grid(column=col, row=row, columnspan=2)


def fill_desc():
    """
    Querying the database to get the description and putting it out
    :return: none
    """
    new_desc = back_end.get_desc(search_title.get().lower())
    # print(new_desc[0][0])
    desc.delete(1.0, END)
    desc.insert(END, new_desc[0][0])


def fill_art():
    """
    Querying the database to get the picture and putting it out
    :return: none
    """
    new_path = back_end.get_pic(search_title.get().lower())
    # print("setup/" + new_path[0][0])
    new_img = ImageTk.PhotoImage(Image.open("setup/" + new_path[0][0]))
    artwork.configure(image=new_img)
    artwork.image = new_img


def fill_page():
    """
    Changing the description and picture to match what you queried
    :return: none
    """
    fill_desc()
    fill_art()


# this creates the window of the application
root = Tk()
root.title("Search Redd's Gallery")
root.configure(background="grey")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# create the header divider
divider(0, 2)

# path = "example.jpg"
path = "example.jpg"

# Create a tkinter-compatible photo image
img = ImageTk.PhotoImage(Image.open(path))

# Labels can be used to display images
artwork = ttk.Label(mainframe, image=img)
artwork.grid(column=0, row=4)

# Labels for what goes where
ttk.Label(mainframe, text="Original Art").grid(column=0, row=3, sticky=W)
ttk.Label(mainframe, text="How to Spot the Fake").grid(column=1, row=3, sticky=W)

# Input box for the search part
ttk.Label(mainframe, text="Enter the art in question").grid(column=0, row=0, sticky=W)
search_title = StringVar()
title_entry = ttk.Entry(mainframe, textvariable=search_title)
title_entry.grid(column=0, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Search", command=fill_page).grid(column=1, row=1, sticky=W)

# this is now an example
# TODO: turn this into finished product by getting from db
ttk.Label(mainframe, text="Great Wave off Kanagawa").grid(column=1, row=4, sticky=(N, W))
desc = Text(mainframe, height=9, width=30)
desc.grid(column=1, row=4, sticky=(N, W))
desc.insert(END, "In the fake, Mt. Fuji is very large and takes up most of the space under the wave. If Mt. Fuji is "
                 "small, it's genuine.")

# put some space between everything
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=1)
root.mainloop()

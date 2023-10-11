# functions used by the UI
# imports
from tkinter import *

# function to open a new window on a button click
def openNewWindow(home):
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(home)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow, text ="This is a new window").pack()
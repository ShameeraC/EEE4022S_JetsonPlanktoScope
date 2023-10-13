#Import the required Libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import math
import UIFunctions as UIF
import sys
sys.path.insert(0, '/home/shameera/Desktop/EEE4022S_JetsonPlanktoScope/Software/Control')
import simple_camera as cam
import pump_control as pump
import lighting as light

def Camera():
    cam.show_camera()

def Pump():
    pump.pumpControl()

def LightOn():
    light.light_on()

def LightOff():
    light.light_off()

# function to open a new window on a button click
# based on https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
def openOpticsWindow():
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(win)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Optics Configuration")
 
    # sets the geometry of toplevel
    newWindow.geometry("400x400")
 
    # A Label widget to show in toplevel
    Label(newWindow, text ="Camera Controls:\n1. ESC or q to quit\n2. j to capture image").pack()

    # buttons to start camera
    camButton = Button(newWindow, text="Start Camera", background='#3A7BB5', foreground='white', command= Camera)
    camButton.pack()

    # button to turn light on and off 
    lightOn = Button(newWindow, text="Start Light", background='#3A7BB5', foreground='white', command= LightOn)
    lightOn.pack()
    lightOff = Button(newWindow, text="Stop Light", background='#3A7BB5', foreground='white', command= LightOff)
    lightOff.pack()

# function to open a new window on a button click
# based on https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
def openFluidicsWindow():
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(win)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Fluidic Acquisition")
 
    # sets the geometry of toplevel
    newWindow.geometry("400x400")
 
    # A Label widget to show in toplevel
    Label(newWindow, text ="Fluidic Acquisition:\n1. q to quit\n2. f to pump forward for 15 seconds\n3. r to pump backwards for 15 seconds\n4. x to stop pump").pack()

    # button to start pump
    pumpButton = Button(newWindow, text="Start Pump", background='#3A7BB5', foreground='white', command= Pump)
    pumpButton.pack()

#Create an instance of Tkinter frame
win = Tk()

#Get the screen width and height
width = win.winfo_screenwidth()
height = win.winfo_screenheight()

#Set the geometry of tkinter frame
win.geometry("%dx%d" % (width/2, height/2))

#Set the Title of Tkinter window
win.title("PlanktoScope Dashboard")

frame = LabelFrame(win, text='Home', bg='#CCCCCC', font=('Helvetica', 35), fg='#749185')
frame.pack(expand=True, fill=BOTH)

# style.configure('TButton', font=('Helvetica', 20), background='#749185', foreground='white', width=20, height=5)
# calculate button size
button_width = math.floor(width / 55)
button_height = math.floor(button_width / 2)

# button objects
button1 = Button(frame, text="Optic Configuration", background='#3A7BB5', foreground='white', width=button_width, height=button_height, command= openOpticsWindow)
button2 = Button(frame, text="Fluidic Acquisition", background='#3A7BB5', foreground='white', width=button_width, height=button_height, command=openFluidicsWindow)
button3 = Button(frame, text="Segmentation", background='#3A7BB5', foreground='white', width=button_width, height=button_height)
button4 = Button(frame, text="Gallery", background='#3A7BB5', foreground='white', width=button_width, height=button_height)

# button layout
button1.grid(row = 1, column = 1, pady = 100, padx = 50, sticky="NSEW")
button2.grid(row = 1, column = 2, pady = 100, padx = 100, sticky="NSEW")
button3.grid(row = 1, column = 3, pady = 100, padx = 100, sticky="NSEW")
button4.grid(row = 1, column = 4, pady = 100, padx = 100, sticky="NSEW")

# logo images
PSPath = "planktoscope_lavender.png"
img = Image.open(PSPath)
imgResized = img.resize((button_width*5, button_height*10), Image.LANCZOS)
PSlogo = ImageTk.PhotoImage(imgResized)
PSlogoImg = Label(frame, image=PSlogo, background='#CCCCCC')
PSlogoImg.photo = PSlogoImg
PSlogoImg.grid(row = 2, column = 1, pady = 300, sticky="NSEW")

UCTPath = "logo.png"
imgUCT = Image.open(UCTPath)
imgUCTResized = imgUCT.resize((button_width*5, button_height*10), Image.LANCZOS)
UCTlogo = ImageTk.PhotoImage(imgUCTResized)
UCTlogoImg = Label(frame, image=UCTlogo, background='#CCCCCC')
UCTlogoImg.photo = UCTlogoImg
UCTlogoImg.grid(row = 2, column = 4, pady = 300, sticky="NSEW")


win.mainloop()
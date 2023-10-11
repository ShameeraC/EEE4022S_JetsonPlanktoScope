# # img_viewer.py from https://realpython.com/pysimplegui-python/#creating-simple-applications

# import PySimpleGUI as sg
# import os.path

# # First the window layout in 2 columns

# file_list_column = [
#     [
#         sg.Text("Image Folder"),
#         sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
#         sg.FolderBrowse(),
#     ],
#     [
#         sg.Listbox(
#             values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
#         )
#     ],
# ]

# # For now will only show the name of the file that was chosen
# image_viewer_column = [
#     [sg.Text("Choose an image from list on left:")],
#     [sg.Text(size=(40, 1), key="-TOUT-")],
#     [sg.Image(key="-IMAGE-")],
# ]

# # ----- Full layout -----
# layout = [
#     [
#         sg.Column(file_list_column),
#         sg.VSeperator(),
#         sg.Column(image_viewer_column),
#     ]
# ]

# window = sg.Window("Image Viewer", layout)

# # Run the Event Loop
# while True:
#     event, values = window.read()
#     if event == "Exit" or event == sg.WIN_CLOSED:
#         break
#     # Folder name was filled in, make a list of files in the folder
#     if event == "-FOLDER-":
#         folder = values["-FOLDER-"]
#         try:
#             # Get list of files in folder
#             file_list = os.listdir(folder)
#         except:
#             file_list = []

#         fnames = [
#             f
#             for f in file_list
#             if os.path.isfile(os.path.join(folder, f))
#             and f.lower().endswith((".png", ".gif"))
#         ]
#         window["-FILE LIST-"].update(fnames)
#     elif event == "-FILE LIST-":  # A file was chosen from the listbox
#         try:
#             filename = os.path.join(
#                 values["-FOLDER-"], values["-FILE LIST-"][0]
#             )
#             window["-TOUT-"].update(filename)
#             window["-IMAGE-"].update(filename=filename)

#         except:
#             pass

# window.close()

# https://stackoverflow.com/questions/23709154/displaying-square-tkinter-buttons

import tkinter as tk

master = tk.Tk()

frame = tk.Frame(master, width=400, height=400) #their units in pixels
button1 = tk.Button(frame, text="btn", bg='#3C8C94', fg='white')


frame.grid_propagate(False) #disables resizing of frame
frame.columnconfigure(0, weight=1) #enables button to fill frame
frame.rowconfigure(0,weight=1) #any positive number would do the trick

frame.grid(row=0, column=1) #put frame where the button should be
button1.grid(sticky="wens") #makes the button expand

tk.mainloop()
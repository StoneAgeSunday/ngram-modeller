from tkinter import *
from tkinter import filedialog

# Create an instance of window
win = Tk()

# Set the geometry of the window
win.geometry("700x300")

#if filesChosen == 0:
label = Label(win, text= "Click the button to select the first corpus", font=('Arial 16 bold'))
label.pack(pady=15)

# Function to open a file in the system
def openFile1():
   filepath = filedialog.askopenfilename(title="Choose first corpus", filetypes=(("text files","*.txt"), ("all files","*.*")))
   print(filepath) 
   label.config(text = "Click the button to select the second file")
   button.config(command = openFile2)

def openFile2():
   filepath = filedialog.askopenfilename(title="Choose second corpus", filetypes=(("text files","*.txt"), ("all files","*.*")))
   print(filepath) 
   close_win()

def shutdown(): 
    close_win()

button = Button(win, text="Open", command=openFile1)
button.pack()

def close_win():
   win.destroy()

win.mainloop()

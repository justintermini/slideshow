# import required modules
from tkinter import *
from PIL import Image
from PIL import ImageTk



# adjust window
root=Tk()
# root.geometry("200x200")
root.attributes('-fullscreen', True)

# loading the images
img=ImageTk.PhotoImage(Image.open("CRmonitor.png"))
img2=ImageTk.PhotoImage(Image.open("NYTmonitor.png"))
img3=ImageTk.PhotoImage(Image.open("WAPOmonitor.png"))
img4=ImageTk.PhotoImage(Image.open("GREATCOURSESmonitor.png"))
img5=ImageTk.PhotoImage(Image.open("WSJmonitor.png"))


l=Label()
l.pack()



# using recursion to slide to next image
x = 1

# function to change to next image
def move():
  global x
  if x == 6:
    x = 1
  if x == 1:
    l.config(image=img)
  elif x == 2:
    l.config(image=img2)
  elif x == 3:
    l.config(image=img3)
  elif x == 4:
    l.config(image=img4)
  elif x == 5:
    l.config(image=img5)
  x = x+1
  root.after(5000, move)

# calling the function
move()



root.mainloop()

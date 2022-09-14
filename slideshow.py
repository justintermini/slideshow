import tkinter as tk
from PIL import Image, ImageTk
import random
import glob


class gui:
    def __init__(self, mainwin):
        
        self.counter = 0
        self.mainwin = mainwin
        self.frame = tk.Frame(mainwin)
        self.img = tk.Label()
        self.img.pack()
        
        self.pic()
        
    
    def pic(self):
        
        self.pic_list = []
        path = r'C:\Users\jtermini\slideshow\imgs\*' # Set path to reflect folder where imgs live 

        for name in glob.glob(path):
            val = name
            self.pic_list.append(val)
            
        if self.counter == len(self.pic_list) - 1:
            self.counter = 0
            
        else:
            self.counter = self.counter + 1
            
        self.file = self.pic_list[self.counter]
        self.load = Image.open(self.file)
        
        self.render = ImageTk.PhotoImage(self.load)
        self.img.config(image = self.render)
        
        self.img.image = self.render
        root.after(3000, self.pic)

def close_escape(event=None):
    print("escaped")
    root.destroy()
        
        
root = tk.Tk()
root.config(cursor="none")
root.attributes('-fullscreen', True) # Use fullscreen to remove bar at top of image
root.bind("<Escape>", close_escape)  # Calls close_escape function to close program when wanted
myprog = gui(root)
root.mainloop()


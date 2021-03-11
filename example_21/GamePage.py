from tkinter import Tk, Frame, Canvas, Label, Entry, Button, PhotoImage
from PIL import Image, ImageTk

class GamePage(Frame):

    def __init__(self, windows, **kargs):
        Frame.__init__(self, windows, **kargs)
        self.windows = windows
        self.createInterface()

    def createInterface(self):
        
        #placer main image
        self.game= Canvas(self.windows, width=1200, height=500, highlightthickness=0)
        self.bg_game = ImageTk.PhotoImage(Image.open('ressources/bg_game.png'))
        self.game.create_image(0,0, image=self.bg_game, anchor='nw')
        self.game.place(x=0,y=0)

        #placer canon
        self.canon_img= PhotoImage(file='ressources/canon.gif')
        self.canon  = self.game.create_image(100, 400, image=self.canon_img)

        # display result
        result_rect = self.game.create_rectangle(10,10,250,120, fill='white')
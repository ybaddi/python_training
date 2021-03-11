from tkinter import Tk, Frame, Canvas, Label, Entry, Button, CENTER
from PIL import Image, ImageTk
# from LoginPage import LoginPage

class LoginFailed(Frame):

    def __init__(self, windows, **kargs):
        Frame.__init__(self, windows, **kargs)
        self.windows = windows
        self.createInterface()

    def createInterface(self):
        self.bg_frame= Canvas(self.windows, width=1200, height=600, highlightthickness=0)
        self.bg_game = ImageTk.PhotoImage(Image.open('ressources/bg_main.png'))
        self.bg_frame.create_image(0,0, image=self.bg_game, anchor='nw')
        self.bg_frame.place(x=0,y=0)

        self.content = Canvas(self.bg_frame, width=400, height=180, highlightthickness=0)
        self.content.place(x=400,y=170)
        # label et pseudo field
        Label(self.content , bg='white', text='Login Failed').place(x=60,y=75)

        # button to submit
        self.submit = Button(self.content , fg='white', bg='#CA994F', text='log gain', command=self.on_click)
        self.submit.place(x=50,y=155)

    def on_click(self):
        print("click")
        self.event_generate('<<LOGIN_PAGE>>')
        # self.call_frame=LoginPage(self.windows)
        # self.call_frame.config(bg='#DDDAC3', padx=5000, pady=5000)
        # self.call_frame.place(relx = 0.5, rely = 0.5, anchor=CENTER)


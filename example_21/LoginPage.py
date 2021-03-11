from tkinter import Tk, Frame, Canvas, Label, Entry, Button
from PIL import Image, ImageTk
from FileVerificator import FileVerificator

class LoginPage(Frame):

    def __init__(self, windows, **kargs):
        Frame.__init__(self, windows, **kargs)
        self.windows = windows
        self.verificator=FileVerificator()
        self.createInterface()

    def createInterface(self):
        self.bg_frame= Canvas(self.windows, width=1200, height=600, highlightthickness=0)
        self.bg_game = ImageTk.PhotoImage(Image.open('ressources/bg_main.png'))
        self.bg_frame.create_image(0,0, image=self.bg_game, anchor='nw')
        self.bg_frame.place(x=0,y=0)

        self.content = Canvas(self.bg_frame, width=400, height=180, highlightthickness=0)
        self.content.place(x=400,y=170)
        # label et pseudo field
        Label(self.content , bg='white', text='Pseudo').place(x=60,y=75)
        self.pseudo = Entry(self.content,  bg='blue')
        self.pseudo.place(x=165,y=70)

        # label et password field
        Label(self.content , bg='white', text='Password').place(x=60,y=110)
        self.password = Entry(self.content , show="*", bg='blue')
        self.password.place(x=165,y=110)

        # button to submit
        self.submit = Button(self.content , fg='white', bg='#CA994F', text='login', command=self.on_login)
        self.submit.place(x=50,y=155)

    def on_login(self):
        if self.verificator.validate(self.pseudo.get(), self.password.get()):
            print(self.pseudo.get(), self.password.get())

            self.event_generate('<<LOGIN_SUCCES>>')
        else:
            self.event_generate('<<LOGIN_FAILED>>')

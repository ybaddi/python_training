from tkinter import Tk, Frame, CENTER
from LoginPage import LoginPage
from LoginFailed import LoginFailed
from GamePage import GamePage

class MyFram(Frame):

    def __init__(self, windows, **kargs):
        Frame.__init__(self, windows, **kargs)
        self.windows = windows

        self.windows.title("ShootGames")
        self.windows.geometry("1200x500")
        self.windows.resizable(width=False, height=False)

        #add multiple windows to

        #login page
        self.placeFrame(LoginPage(self.windows), False)
        # signup page
        # ...

        # manage bind events
        self.call_frame.bind('<<LOGIN_SUCCES>>', self.forward_to_game)
        self.call_frame.bind('<<LOGIN_PAGE>>', self.forward_to_Login_page)
        self.call_frame.bind('<<LOGIN_FAILED>>', self.forward_to_Login_failed)

    def placeFrame(self, page, delete=True):
        if delete: self.call_frame.destroy()
        self.call_frame=page
        self.call_frame.config(bg='#DDDAC3', padx=5000, pady=5000)
        self.call_frame.place(relx = 0.5, rely = 0.5, anchor=CENTER)

    def forward_to_Login_page(self, event):
        print('login')
        self.placeFrame(LoginPage(self.windows))


    def forward_to_game(self, event):
        print('game')
        self.placeFrame(GamePage(self.windows))



    def forward_to_Login_failed(self, event):
        self.placeFrame(LoginFailed(self.windows))


windows = Tk()
MyFram = MyFram(windows)
windows.mainloop()
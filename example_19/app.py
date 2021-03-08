from tkinter import Tk, Button, Label


window = Tk()
window.title("Python Tkinter")


label = Label(window, text='hello')
label.pack()

button = Button(window, text='But')
button.pack()

window.mainloop()
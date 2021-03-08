from tkinter import Tk, Button, Label



class CostumWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        
        self.title("Python Tkinter")
        self.geometry("300x200")
        


        label = Label(self, text='hello')
        label.pack()

        button = Button(self, text='But', command=self.click())
        button.pack()

    def click(self): 
        print("clicked")  

window = CostumWindow()
window.mainloop()
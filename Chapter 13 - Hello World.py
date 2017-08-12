import tkinter

class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text="Hello World!")

        self.label2 = tkinter.Label(self.bottom_frame, text="This is my program!")

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.label1.pack(side="right")

        self.label2.pack(side="bottom")

        tkinter.mainloop()

my_gui = MyGUI()


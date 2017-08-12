import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.my_button = tkinter.Button(self.main_window, text="Hey! Mariel! Click me!", command=self.do_something)

        self.your_button = tkinter.Button(self.main_window, text="Or click me...", command=self.do_something_else)

        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.my_button.pack(side="left")
        self.your_button.pack(side="left")
        self.quit_button.pack(side="left")

        tkinter.mainloop()

    def do_something(self):

        for x in range(10):

            tkinter.messagebox.showinfo("Front", "Sexy and...")
            tkinter.messagebox.showinfo("Back", "Hot and...")

    def do_something_else(self):

        for x in range(10):

            tkinter.messagebox.showinfo("Ack!", "It's a trap!")


my_gui = MyGUI()
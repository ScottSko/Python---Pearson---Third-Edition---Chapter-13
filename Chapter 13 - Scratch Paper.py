import tkinter

def main():

    main_window = tkinter.Tk()

    message = tkinter.Entry(main_window, text="Hi")

    message.pack()

    tkinter.mainloop()

main()
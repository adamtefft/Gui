import tkinter
import tkinter.messagebox


class myGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        # configure the window
        self.main_window.geometry("500x200")
        # This changes the size of the window

        self.main_window.title("Frames and Buttons Demo")
        # This adds a title to the top of the program

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text="John")
        self.label2 = tkinter.Label(self.top_frame, text="James")
        self.label3 = tkinter.Label(self.top_frame, text="Jack")

        self.label1.pack(side="left")
        self.label2.pack(side="left")
        self.label3.pack(side="left")

        self.label4 = tkinter.Label(self.top_frame, text="Jill")
        self.label5 = tkinter.Label(self.top_frame, text="Jenny")
        self.label6 = tkinter.Label(self.top_frame, text="Jennifer")

        self.label4.pack(side="left")
        self.label5.pack(side="left")
        self.label6.pack(side="left")

        self.my_button = tkinter.Button(
            self.main_window, text="Click Me", command=self.do_something)
        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy)

        self.quit_button.pack(side="right")
        self.my_button.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.top_frame.pack

        tkinter.mainloop()
        # This allows the window to be continuously active until the user closes the window
        # Once the window disappears, then it goes on with the rest of the code
        # It will not proceed with the code until the user closes out the window

    def do_something(self):
        tkinter.messagebox.showinfo(
            "Response", "Thanks for clicking the button")


myinstance = myGUI()

print("moving on.......")

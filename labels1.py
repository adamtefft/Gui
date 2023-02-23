import tkinter


class myGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        # configure the window
        self.main_window.geometry("500x200")
        # This changes the size of the window

        self.main_window.title("Label Demo")
        # This adds a title to the top of the program

        self.label1 = tkinter.Label(self.main_window, text="Hello World!")

        self.label2 = tkinter.Label(
            self.main_window, text="This is my GUI Program.")

        self.label1.pack(side="left")
        self.label2.pack(side="right")

        tkinter.mainloop()
        # This allows the window to be continuously active until the user closes the window
        # Once the window disappears, then it goes on with the rest of the code
        # It will not proceed with the code until the user closes out the window


myinstance = myGUI()

print("moving on.......")

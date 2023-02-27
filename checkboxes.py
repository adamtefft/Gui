import tkinter
import tkinter.messagebox

# checkboxes allow you to select multiple buttons at the same time


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

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var2.set(1)
        # This makes box 2 checked by default

        self.cb1 = tkinter.Checkbutton(
            self.top_frame, text='Option 1', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(
            self.top_frame, text='Option 2', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(
            self.top_frame, text='Option 3', variable=self.cb_var3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.my_button = tkinter.Button(
            self.main_window, text="Ok", command=self.show_choice)
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

    def show_choice(self):
        self.message = 'You have selected:\n'

        if self.cb_var1.get() == 1:
            # This is checking to see if the checkbox is checked, if it is not, it would be null
            self.message += '1/n'
        if self.cb_var2.get() == 1:
            self.message += '2/n'
        if self.cb_var3.get() == 1:
            self.message += '3/n'

        tkinter.messagebox.showinfo(
            "Selection", self.message)


myinstance = myGUI()

print("moving on.......")

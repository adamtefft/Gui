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

        self.radio_var = tkinter.IntVar()
        # This is an integer variable

        self.rb1 = tkinter.Radiobutton(
            self.top_frame, text='Option 1', variable=self.radio_var, value=1, command=self.show_choice)
        self.rb2 = tkinter.Radiobutton(
            self.top_frame, text='Option 2', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(
            self.top_frame, text='Option 3', variable=self.radio_var, value=3)
        # The value of the button that is set, is the value that is returned whenever you click the button

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')

        self.my_button = tkinter.Button(
            self.bottom_frame, text="OK", command=self.show_choice)
        self.quit_button = tkinter.Button(
            self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.quit_button.pack(side="right")
        self.my_button.pack(side="left")

        tkinter.mainloop()
        # This allows the window to be continuously active until the user closes the window
        # Once the window disappears, then it goes on with the rest of the code
        # It will not proceed with the code until the user closes out the window

    def show_choice(self):
        tkinter.messagebox.showinfo(
            "Selection", 'You have selected option ' + str(self.radio_var.get()))


myinstance = myGUI()

print("moving on.......")

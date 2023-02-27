import tkinter
import tkinter.messagebox


class KilConverterGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        # configure the window
        self.main_window.geometry("500x200")
        # This changes the size of the window

        self.main_window.title("Kilometers to Miles Converter")
        # This adds a title to the top of the program

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(
            self.top_frame, text="Enter a distance in Kilometers")
        self.label1.pack(side="left")

        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)
        self.kilo_entry.pack(side='left')

        self.calc_button = tkinter.Button(
            self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(
            self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.quit_button.pack(side="bottom")
        self.calc_button.pack(side="top")

        tkinter.mainloop()
        # This allows the window to be continuously active until the user closes the window
        # Once the window disappears, then it goes on with the rest of the code
        # It will not proceed with the code until the user closes out the window

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214

        tkinter.messagebox.showinfo(
            "Result", str(kilo) + 'kilometers is equal to ' + str(miles) + 'miles.')


myinstance = KilConverterGUI()

print("moving on.......")

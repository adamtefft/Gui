import tkinter
import tkinter.messagebox


class KilConverterGUI:
    def __init__(self):
        self.kilo = 0.0
        self.miles = 0.0
        self.main_window = tkinter.Tk()
        # This is just referring to the window

        # configure the window
        self.main_window.geometry("500x200")
        # This changes the size of the window

        self.main_window.title("Kilometers to Miles Converter")
        # This adds a title to the top of the program

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(
            self.top_frame, text="Enter a distance in Kilometers")
        self.label1.pack(side="left")

        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)
        self.kilo_entry.pack(side='left')

        self.desc_label = tkinter.Label(
            self.mid_frame, text="Converted to miles: ")

        self.miles_label_var = tkinter.StringVar()
        # We are creating a string variable which can change dynamically depending on the value assigned to it
        # This is letting the box contain the text of the calculation that has been made

        self.miles_label = tkinter.Label(
            self.mid_frame, textvariable=self.miles_label_var)

        self.desc_label.pack(side='left')
        self.miles_label.pack(side='right')

        self.calc_button = tkinter.Button(
            self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(
            self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        self.quit_button.pack(side="bottom")
        self.calc_button.pack(side="top")

        tkinter.mainloop()
        # This allows the window to be continuously active until the user closes the window
        # Once the window disappears, then it goes on with the rest of the code
        # It will not proceed with the code until the user closes out the window

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = round(self.kilo * 0.6214, 2)

        #tkinter.messagebox.showinfo("Result", str(kilo) + 'kilometers is equal to ' + str(miles) + 'miles.')

        self.miles_label_var.set(self.miles)


myinstance = KilConverterGUI()

print("moving on.......")

print(myinstance.kilo, ',', myinstance.miles)

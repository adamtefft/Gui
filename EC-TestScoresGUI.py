import tkinter
import tkinter.messagebox


class myGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.geometry("300x200")
        self.main_window.title("Average Test Scores")
        self.main_window.config(bg="Green")

        self.top_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack()
        self.top_frame.config(bg="Green")

        self.middle_frame = tkinter.Frame(self.main_window)
        self.middle_frame.pack()
        self.middle_frame.config(bg="Green")

        self.bottom_frame = tkinter.Frame(self.main_window)
        self.bottom_frame.pack()
        self.bottom_frame.config(bg="Green")

        self.average_frame = tkinter.Frame(self.main_window)
        self.average_frame.pack()
        self.average_frame.config(bg="Green")

        self.button_frame = tkinter.Frame(self.main_window)
        self.button_frame.pack()
        self.button_frame.config(bg="Green")

        self.test1_label = tkinter.Label(self.top_frame, text='Enter the score for test 1:')
        self.test1_label.pack(side='left')
        self.test1_label.config(font=("Courier", 10))
        self.test1_label.config(fg="Yellow")
        self.test1_label.config(bg="Green")

        self.test1_entry = tkinter.Entry(self.top_frame, width=10)
        self.test1_entry.pack(side='right')
        self.test1_entry.config(fg="Yellow")
        self.test1_entry.config(bg="Green")
        self.test1_entry.config(highlightbackground="Yellow")

        self.test2_label = tkinter.Label(self.middle_frame, text='Enter the score for test 2:')
        self.test2_label.pack(side='left')
        self.test2_label.config(font=("Courier", 10))
        self.test2_label.config(fg="Yellow")
        self.test2_label.config(bg="Green")

        self.test2_entry = tkinter.Entry(self.middle_frame, width=10)
        self.test2_entry.pack(side='right')
        self.test2_entry.config(fg="Yellow")
        self.test2_entry.config(bg="Green")
        self.test2_entry.config(highlightbackground="Yellow")

        self.test3_label = tkinter.Label(self.bottom_frame, text='Enter the score for test 3:')
        self.test3_label.config(font=("Courier", 10))
        self.test3_label.config(fg="Yellow")
        self.test3_label.config(bg="Green")

        self.test3_label.pack(side='left')

        self.test3_entry = tkinter.Entry(self.bottom_frame, width=10)
        self.test3_entry.pack(side='right')
        self.test3_entry.config(fg="Yellow")
        self.test3_entry.config(bg="Green")
        self.test3_entry.config(highlightbackground="Yellow")

        self.display_average_label = tkinter.Label(self.average_frame, text="Average")
        self.display_average_label.pack(side='left')
        self.display_average_label.config(fg="Yellow")
        self.display_average_label.config(bg="Green")
        self.display_average_label.config(font=("Courier", 10))

        self.display_average = tkinter.StringVar()

        self.average_label = tkinter.Label(self.average_frame, textvariable=self.display_average)
        self.average_label.pack(side='left')
        self.average_label.config(bg="Green")

        self.average_button = tkinter.Button(self.button_frame, text="Average", command=self.average)
        self.average_button.pack(side='left')
        self.average_button.config(fg="Green")
        self.average_button.config(font=("Courier", 10))
        self.average_button.config(bg="Green")
        self.average_button.config(highlightbackground="Green")

        self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.destroy)
        self.quit_button.pack(side='right')
        self.quit_button.config(fg="Green")
        self.quit_button.config(font=("Courier", 10))
        self.quit_button.config(highlightbackground="Green")

        tkinter.mainloop()

    def average(self):
        test1 = float(self.test1_entry.get())
        test2 = float(self.test2_entry.get())
        test3 = float(self.test3_entry.get())
        # These take the entrys from the method above and assigns them to variables in order to calculate the average

        test_total = test1 + test2 + test3


        test_average = round(test_total / 3, 2)

        if test_average < 70:
            self.average_label.config(bg="Red")
        elif test_average < 90:
            self.average_label.config(bg="Yellow")
        else:
            self.average_label.config(bg="Green")

        self.display_average.set(test_average)
        # tkinter.messagebox.showinfo("Title of the messagebox",f"Average: {test_average}")


myinstance = myGUI()

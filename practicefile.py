import tkinter
import tkinter.messagebox


class myGUI:
    def __init__(self):


        self.main_window = tkinter.Tk()
        # Creating the main window that all the widgets are stored in

        self.main_window.geometry("1000x400")
        # Created a method that sets the dimensions of the window

        self.main_window.title("GUI Widgets")
        # This adds a title to the top of the program

        self.top_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack()
        # Creating the Top Frame and Packed it

        self.middle_frame = tkinter.Frame(self.main_window)
        self.middle_frame.pack()

        self.bottom_frame = tkinter.Frame(self.main_window)
        self.bottom_frame.pack()
        # Creating the Bottom Frame and Packed it

        self.main_text = tkinter.Label(self.main_window, text='This is the top of the window')
        self.main_text.pack(side = 'top')
        # Created text at the top of the screen that is stored inside the top frame of the window

        self.sub_text = tkinter.Label(self.main_window, text='This is the bottom of the window')
        self.sub_text.pack(side = 'bottom')
        # Created text at the bottom of the screen that is stored inside the bottom frame of the window

        self.test1_label = tkinter.Label(self.top_frame, text='Test 1 Score:')
        self.test1_label.pack(side='left')

        self.test1_entry = tkinter.Entry(self.top_frame, width=10)
        self.test1_entry.pack(side = 'right')
        # This entry is created in the top frame and allows the user to input test into the top box

        self.test2_label = tkinter.Label(self.middle_frame, text='Test 2 Score:')
        self.test2_label.pack(side='left')

        self.test2_entry = tkinter.Entry(self.middle_frame, width=10)
        self.test2_entry.pack(side = 'right')
        # This entry is created in the top frame and allows the user to input test into the middle box

        self.test3_label = tkinter.Label(self.bottom_frame, text='Test 3 Score:')
        self.test3_label.pack(side='left')

        self.test3_entry = tkinter.Entry(self.bottom_frame, width=10)
        self.test3_entry.pack(side = 'right')
        # This entry is created in the top frame and allows the user to input test into the bottom box

        self.average_button = tkinter.Button(self.main_window, text = "Calculate Average", command=self.average)
        self.average_button.pack(side = 'top')
        # Created a button that is stored inside the bottom frame that will calculate the average of the 3 test scores

        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        # This button will quit the program and close it

        self.radio_var = tkinter.IntVar()
        # This assigns a unique integer to each RadioButton
        # When a RadioButton widget is selected, its unique integer is stored in the IntVar() object

        self.radiobutton1 = tkinter.Radiobutton(self.main_window, variable=self.radio_var, text='Test', value=1, command=self.grade_type)
        self.radiobutton1.pack()

        self.radiobutton2 = tkinter.Radiobutton(self.main_window, variable=self.radio_var, text='Quiz', value=2, command=self.grade_type)
        self.radiobutton2.pack()

        self.radiobutton3 = tkinter.Radiobutton(self.main_window, variable=self.radio_var, text='Homework', value=3, command=self.grade_type)
        self.radiobutton3.pack()
        # The command=self.grade_type replaces the need for a user to click OK before determining which RadioButton has been selected



        # Creating the Checkboxes
        self.check_var1 = tkinter.IntVar()
        self.check_var2 = tkinter.IntVar()
        self.check_var3 = tkinter.IntVar()

        self.checkbutton1 = tkinter.Checkbutton(self.main_window,text = 'Item 1',variable=self.check_var1)
        self.checkbutton1.pack()

        self.checkbutton2 = tkinter.Checkbutton(self.main_window,text = 'Item 2', variable=self.check_var2)
        self.checkbutton2.pack()

        self.checkbutton3 = tkinter.Checkbutton(self.main_window,text = 'Item 3',variable=self.check_var3)
        self.checkbutton3.pack()

        self.confirmationbutton = tkinter.Button(self.main_window, text = "Ok", command=self.checkbox_message)
        self.confirmationbutton.pack()


        tkinter.mainloop()










    # This method is prompted when the average button is clicked by the user
    def average(self):
        test1 = float(self.test1_entry.get())
        test2 = float(self.test2_entry.get())
        test3 = float(self.test3_entry.get())
        # These take the entrys from the method above and assigns them to variables in order to calculate the average

        test_total = test1 + test2 + test3
        test_average = round(test_total / 3,2)

        tkinter.messagebox.showinfo("Title of the messagebox",f"Average: {test_average}")
        # This is how you create a message box, the message box will be displayed after the "Calculate Average" button is clicked by the user
        # "Hello" is the title, and it is displayed in the dialog box's title bar







    # This method is prompted when RadioButton has been clicked
    def grade_type(self):
        tkinter.messagebox.showinfo("Title of the Messagebox", f"You have selected option {self.radio_var.get()}")








    # This method is prompted whenever you click "OK" after selecting the checkboxes
    def checkbox_message(self):
        self.message = "You have selected the following options from the checkboxes:\n"
        if self.check_var1.get() == 1:
            self.message += 'Checkbox 1\n'
        if self.check_var2.get() == 1:
            self.message += 'Checkbox 2\n'
        if self.check_var3.get() == 1:
            self.message += 'Checkbox 3\n'          
        

        tkinter.messagebox.showinfo("Title of the Messagebox",self.message)


myinstance = myGUI()

print("moving on.......")

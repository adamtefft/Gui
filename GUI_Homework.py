import tkinter
import tkinter.messagebox


class myGUI:

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.geometry("350x350")
        self.main_window.title("Responsive Registration Form")

        self.email_frame = tkinter.Frame(self.main_window)
        self.email_frame.pack()

        self.password_frame = tkinter.Frame(self.main_window)
        self.password_frame.pack()

        self.password2_frame = tkinter.Frame(self.main_window)
        self.password2_frame.pack()

        self.name_frame = tkinter.Frame(self.main_window)
        self.name_frame.pack()

        self.rb_frame = tkinter.Frame(self.main_window)
        self.rb_frame.pack()

        self.cb1 = tkinter.Frame(self.main_window)
        self.cb1.pack()

        self.cb2 = tkinter.Frame(self.main_window)
        self.cb2.pack()

        self.main_text = tkinter.Label(
            self.email_frame, text='Responsive Registration\nForm\n', font=("Bold", 22))
        self.main_text.pack(side='top')

        self.email_label = tkinter.Label(self.email_frame, text='Email:')
        self.email_label.pack(side='left')

        self.email_entry = tkinter.Entry(self.email_frame, width=35)
        self.email_entry.pack(side='right')

        self.password_label = tkinter.Label(
            self.password_frame, text='Password:')
        self.password_label.pack(side='left')

        self.password_entry = tkinter.Entry(
            self.password_frame, show="*", width=30)
        self.password_entry.pack(side='right')

        self.password2_label = tkinter.Label(
            self.password2_frame, text='Retype Password:')
        self.password2_label.pack(side='left')

        self.password2_entry = tkinter.Entry(
            self.password2_frame, show="*", width=25)
        self.password2_entry.pack(side='right')

        self.fname_label = tkinter.Label(self.name_frame, text='First Name:')
        self.fname_label.pack(side='left')

        self.fname_entry = tkinter.Entry(self.name_frame, width=10)
        self.fname_entry.pack(side='left')

        self.lname_entry = tkinter.Entry(self.name_frame, width=10)
        self.lname_entry.pack(side='right')

        self.lname_label = tkinter.Label(self.name_frame, text='Last Name:')
        self.lname_label.pack(side='right')

        self.radio_var = tkinter.IntVar()
        self.radiobutton1 = tkinter.Radiobutton(
            self.rb_frame, variable=self.radio_var, text='Male', value='Male')
        self.radiobutton1.pack(side='left')

        self.radiobutton2 = tkinter.Radiobutton(
            self.rb_frame, variable=self.radio_var, text='Female', value='Female')
        self.radiobutton2.pack(side='left')

        self.check_var1 = tkinter.IntVar()
        self.check_var2 = tkinter.IntVar()

        self.checkbutton1 = tkinter.Checkbutton(
            self.cb1, text='I agree with terms and conditions', variable=self.check_var1)
        self.checkbutton1.pack(side='left')

        self.checkbutton2 = tkinter.Checkbutton(
            self.cb2, text='I want to recieve the newsletter', variable=self.check_var2)
        self.checkbutton2.pack(side='left')

        self.confirmationbutton = tkinter.Button(
            self.main_window, text="Register", command=self.check_credentials)
        self.confirmationbutton.pack()

        tkinter.mainloop()

    def check_credentials(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        password2 = self.password2_entry.get()
        # male = self.radiobutton1.get()
        # female = self.radiobutton2.get()

        if len(email) < 3 or len(email) > 30:
            tkinter.messagebox.showinfo(
                "Text Box Title", "Email must be inbetween 3-14 characters")
        if len(password) < 8:
            tkinter.messagebox.showinfo(
                "Text Box Title", "Password must be at least 8 characters long")
        if password != password2:
            tkinter.messagebox.showinfo(
                "Text Box Title", "Passwords do not match")
        # I need to check to make sure either the Male or Female RadioButton is checked
        '''
        if male != True:
            if female != True:
                tkinter.messagebox.showinfo("Text Box Title","You must select a Gender")
        '''
        # I need to figure this out

        if self.check_var1.get() != 1:
            tkinter.messagebox.showinfo(
                "Text Box Title", "Both boxes must be checked")
            if self.check_var2.get() != 1:
                tkinter.messagebox.showinfo(
                    "Text Box Title", "Both boxes must be checked")

        else:
            tkinter.messagebox.showinfo("Text Box Title", "Success!")


myinstance = myGUI()

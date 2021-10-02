#Noah Lindon
#CSCI 290
#4-19-20
from tkinter import *          
from tkinter import messagebox  
from tkinter import ttk         # Needed for combobox and more advanced widgets

class MyGUI:
    def __init__(self):

        # Create the main window widget.
        self.main_window = Tk()

        self.main_window.title("Assign10-LindonN")

        #Create the menubar in tkinter
        self.menubar = Menu(self.main_window)

        #Create frames in ttk
        #Entire grid is in this frame
        self.content_frame = ttk.Frame(self.main_window)
        
        self.label1 = ttk.Label(self.content_frame, text='')

        # Frames
        self.titleFrame = ttk.Frame(self.main_window)
        self.firstnameFrame = ttk.Frame(self.main_window, borderwidth=10, width = 200, height=100)
        self.lastnameFrame = ttk.Frame(self.main_window, borderwidth=10, width = 200, height=100)
        self.ageFrame = ttk.Frame(self.main_window, borderwidth=10, width = 200, height=100)

        self.exitFrame = ttk.Frame(self.main_window)

        # Entry Widgets
        # What is your first name?
        self.firstnameLabel = ttk.Label(self.firstnameFrame, text = "What is your first name?")
        self.pickFirstName = StringVar()
        self.firstname = ttk.Entry(self.firstnameFrame, textvariable = self.pickFirstName, width = 33)

        # What is your last name?
        self.lastnameLabel = ttk.Label(self.lastnameFrame, text = "What is your last name?")
        self.pickLastName = StringVar()
        self.lastname = ttk.Entry(self.lastnameFrame, textvariable = self.pickLastName, width = 33)

        # What is your age?
        self.ageLabel = ttk.Label(self.ageFrame, text = "What is your age?")
        self.pickAge = StringVar()
        self.age = ttk.Entry(self.ageFrame, textvariable = self.pickAge, width = 33)

        # Exit Frame
        self.exitLabel = ttk.Label(self.exitFrame)
      
        self.my_button = ttk.Button(self.exitFrame, \
                                    text='Save', \
                                    command=self.submit_button)

        self.quit_button =ttk.Button(self.exitFrame, \
                                     text='Quit', \
                                     command=self.main_window.destroy)

        self.label1.grid(column = 0, row = 2, columnspan=3)
        self.content_frame.grid(column = 0, row = 0)
        self.firstnameFrame.grid(column = 0, row = 2, columnspan=5, rowspan = 2)
        self.lastnameFrame.grid(column = 0, row = 6, columnspan=5, rowspan = 2)
        self.ageFrame.grid(column = 0, row = 10, columnspan=5, rowspan = 2)
        self.exitFrame.grid(column = 0, row = 14, columnspan=5, rowspan = 2)
        self.firstnameLabel.grid(column = 0, row = 1)
        self.lastnameLabel.grid(column = 0, row = 3)
        self.ageLabel.grid(column = 0, row = 4)
        self.firstname.grid(column = 0, row = 3)
        self.lastname.grid(column = 0, row = 7)
        self.age.grid(column = 0, row = 11)
        self.exitLabel.grid(column = 0, row = 15)

        self.my_button.grid(column = 1, row = 1)
        self.quit_button.grid(column = 2, row = 1)

        # File Tab
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.newtab)
        self.filemenu.add_command(label="Open", command=self.opentab)
        self.filemenu.add_command(label="Save", command=self.writetofile)
        self.submenu = Menu(self.filemenu)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Settings tab
        self.settingsmenu = Menu(self.menubar, tearoff=0)
        self.settingsmenu.add_command(label="Preferences", command=self.dopreferences)
        self.settingsmenu.add_separator()
        self.settingsmenu.add_command(label="Exit", command=self.main_window.destroy)
        self.menubar.add_cascade(label="Settings", menu=self.settingsmenu)

        # Configure the menu
        self.main_window.config(menu=self.menubar)
        # Enter the tkinter main loop.
        mainloop()

    def newtab(self):
        print("opening a new tab")
    def opentab(self):
        print("Error Code: 43\nCan't open the tab")
    def writetofile(self):
        my_file = open("names.txt", "a")
        my_file.write(self.lastname.get() + ', ' + self.firstname.get() + ' ' + self.age.get() + '\n')
        print(self.lastname.get() + ' , ' + self.firstname.get() + ' ' + self.age.get())
    def dopreferences(self):
        # Preferences
        print("There aren't any preferences") 
    def submit_button(self):
        my_file = open("names.txt", "a")
        my_file.write(self.lastname.get() + ', ' + self.firstname.get() + ' ' + self.age.get() + '\n')
        print(self.lastname.get() + ' , ' + self.firstname.get() + ' ' + self.age.get())
# Create an instance of the MyGUI class.
my_gui = MyGUI()


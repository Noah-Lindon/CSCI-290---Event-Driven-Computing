# Noah Lindon
# CSCI 290
# 4/25/20


from tkinter import *           # New - now we do not have to type tkinter all the time
from tkinter import messagebox  # Still need to import messagebox
from tkinter import ttk         # Needed for combobox and more advanced widgets

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = Tk() 

        #Create title for the main window. New!!
        #You will need to make the window bigger to display the title.
        self.main_window.title("Hotel Reservation System")

        #Create first label using ttk
        self.label1 = ttk.Label(self.main_window, text = "Noah's Reservation System")
        self.label2 = ttk.Label(self.main_window, text = "Pick a hotel")
         
        self.myHotel = StringVar()
        self.combobox1 = ttk.Combobox(self.main_window, width = 15 , textvariable = self.myHotel)
        self.combobox1['values'] = ("Hibana Resorts", "Mozzie's Outback", "Maestro's Motel", "Mavericks's Nest", "Lion's Den")
        
        #Create first label using ttk
        self.label3 = ttk.Label(self.main_window, text = "Pick a month")         
        self.myMonth = StringVar()
        self.combobox2 = ttk.Combobox(self.main_window, width = 15 , textvariable = self.myMonth)
        self.combobox2['values'] = ("January", "February", "March", "April", "May", "June", "July",
                                   "August", "September", "October", "November", "December")

        #Create first label using ttk
        self.label4 = ttk.Label(self.main_window, text = "Pick a year")         
        self.myYear = StringVar()
        self.combobox3 = ttk.Combobox(self.main_window, width = 15 , textvariable = self.myYear)
        self.combobox3['values'] = ("2020", "2021", "2022")

        #Create first label using ttk
        self.label5 = ttk.Label(self.main_window, text = "Pick the number of rooms (4 maximum)")         
        self.myRoom = StringVar()
        self.combobox4 = ttk.Combobox(self.main_window, width = 15 , textvariable = self.myRoom)
        self.combobox4['values'] = ("1", "2", "3", "4")

        #Create first label using ttk
        self.label6 = ttk.Label(self.main_window, text = "Pick the number of people (6 maximum)")         
        self.myPeople = StringVar()
        self.combobox5 = ttk.Combobox(self.main_window, width = 15 , textvariable = self.myPeople)
        self.combobox5['values'] = ("1", "2", "3", "4", "5", "6")



        #We will be using this quote below
        quote = """Feel free to add any requests or comments to your room \nreservation.  As always, enjoy your stay"""
        
        #Create second label
        self.label7 = ttk.Label(self.main_window, text = "A message from the hotel staff and team")
        
        #Create a second text box but do not allow the user to modify the contents. 
        self.tbox1 = Text(self.main_window, height = 5, width = 30)
        self.tbox1.insert(END, quote)    #Insert the quote above at the end of the text box.
        self.tbox1['state']='disabled'   #Do not allow entry in this text box  


        #Create third label
        self.label8 = ttk.Label(self.main_window, text = "Enter comments and requests below")
        
        #Create a third text box. 
        self.tbox2 = Text(self.main_window, height = 4, width = 60)
        #self.tbox3.insert(END, quote)

        #Create a vertical scrollbar
        self.vscroll = Scrollbar(self.main_window) #Default is vertical

        #Configure the scrollbars with tbox3
        self.vscroll.config(command=self.tbox2.yview)
        self.tbox2.config(yscrollcommand=self.vscroll.set)







        # Create a Button widget. The text 'Click Me!'
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button = ttk.Button(self.main_window, \
                                        text='Submit', \
                                        command=self.do_something)          
        self.quit_button = ttk.Button(self.main_window,
                                      text='Quit',
                                      command=self.main_window.destroy)

        # Pack the Widgets.
        self.label1.pack()
        self.label2.pack()
        self.combobox1.pack()
        self.label3.pack()
        self.combobox2.pack()
        self.label4.pack()
        self.combobox3.pack()
        self.label5.pack()
        self.combobox4.pack()
        self.label6.pack()
        self.combobox5.pack()
        
        self.label7.pack()
        self.tbox1.pack()
        
        self.label8.pack()
        self.tbox2.pack()
        
        self.my_button.pack()
        self.quit_button.pack()
        
        # Enter the tkinter main loop.
        mainloop()

    # The do_something method is a callback function
    # for the Button widget.
    
    def do_something(self):
        # Display an info dialog box.
        if (self.myHotel.get() == ''): #The user did not choose anything
            messagebox.showinfo('Oops!', \
                                    'You did not choose anything! Try again.')
        else:
            # Display the selected info
            print("Hotel: ", self.myHotel.get())
            print("Month: ", self.myMonth.get())
            print("Year: ", self.myYear.get())
            print("Rooms: ", self.myRoom.get())
            print("People: ", self.myPeople.get())
        
        #Create a new window 
        self.newWindow = Toplevel(self.main_window)
        self.newWindow.title("Your copy of reservation and comment/s and request/s")
        
        self.label10 = Label(self.newWindow, text = "This is your reservation")
        self.label10.pack()
        self.label11 = Label(self.newWindow, text = self.myHotel.get())
        self.label11.pack()
        
        self.label12 = Label(self.newWindow,text = self.myMonth.get())
        self.label12.pack()
        
        self.label13 = Label(self.newWindow, text = self.myYear.get())
        self.label13.pack()
        
        self.label14 = Label(self.newWindow, text = self.myRoom.get())
        self.label14.pack()
        
        self.label15 = Label(self.newWindow, text = self.myPeople.get())
        self.label15.pack()
        
        
        #Put a label in your window
        self.label16 = Label(self.newWindow, text = "\nThis is your comment/s and request/s:")
        self.label16.pack()

        self.label17 = Label(self.newWindow, text = self.tbox2.get('1.0', 'end'))
        self.label17.pack()
        print(self.tbox2.get('1.0', 'end'))

# Create an instance of the MyGUI class.
my_gui = MyGUI()


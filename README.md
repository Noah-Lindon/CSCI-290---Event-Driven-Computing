# CSCI-290---Event-Driven-Computing
The following are descriptions for the assignments uploaded.
Unfortunately due to how the class operated most of the assignments were done in class and weren't submitted online so I don't have access to most of the assignments anymore.

Assignment 1 In Class:
Using the Car class (car.py), write a program in Python that creates an object of this class.
Ask the user initially to enter the make, model, and year of a car. Display the make, model, and year.
Then ask the user for another make and display that make. Ask for another model and display that model.
Finally, ask for another year and display the year. You should use all the methods in the Car class. Make sure your output is descriptive.
You could start with car2.py and modify this program. If you do, remember to change the comments.
In Python, by default, the data is input as a string, so you do not need to convert it to float. Assume all your data are strings.
I want to see several descriptive comments throughout the code.
Name the program Assign1-LastFirstInit where Last is your last name and FirstInit is your first initial. For example: Assign1-OgleD.
At the top of the program add three lines of comments - Your name, the date, and the assignment number. 
Show me the program when you are finished. After you show the program to me, upload the .py file.



Assignment 1-1:
Create an Employee class in Python that contains the following members:
name
idNum
title
salary 
department
All values are strings except for salary which will be a real number.
In the __init__ function, do not accept parameters, just set the strings to " " and set salary to zero.
Write mutator functions (sets) that load the data for each member. You do not need to ask for user input, just send the data to the sets with the call.
Write accessor functions (gets) for each member that retrieve each member. Then display all the values using these get functions.
I want to see several descriptive comments throughout the code. Your output should be descriptive.
Name the program Assign1-1-LastFirstInit where Last is your last name and FirstInit is your first initial. For example: Assign1-1-OgleD.
At the top of the program add three lines of comments - Your name, the date, and the assignment number. 
Upload the program when you are finished. 



Assignment 5-5:
Write a GUI Python program using tkinter to add an image and work with fonts and colors.
Start with Gif Demo.py .
Use the following web page as a reference: https://www.python-course.eu/tkinter_labels.php (Links to an external site.)
Use any gif file, but not the one used in class.
Use frames to make the window look better. Keep the buttons and put in a separate frame.
Use three different labels with 3 different formats. Do not just use the formats in the web page above.
I want to see several descriptive comments throughout the code. If you use an existing program, change the comments as needed.
Name the program Assign5-5-LastFirstInit where Last is your last name and FirstInit is your first initial. For example: Assign5-5-OgleD.py
At the top of the program add three lines of comments - Your name, the date, and the assignment number. 
Note: If I see that you copied someone else's code, you will get a zero on this assignment. Your screen should be unique.
Upload your program and .gif file.




Assignment 7:
Use tkinter and ttk to create the form for a hotel reservation system.
Combobox_demo.py would be a good programs to start. Look at the calendar_demo.py program only for the way it prints to the console.
For the main window, add an appropriate title.
In the window, create a label that says hotel reservation system or create a company name.
Create 5 different comboboxes, each with their own label.
Use a strVar for each combobox. This means even your numbers in the comboboxes will be strings: "1", "2"
Assume that this system has 5 different hotels. Create a combobox with these hotels. Names are up to you.
Create a combobox for the months.
Create a combobox for the year. (Put in about 3 years.)
Create a combobox for number of rooms. (Four max)
Create a combobox field for number of people. (Six max)
Hint: do one combobox at a time. Then you can copy and paste the rest.
Add a Submit button (call it whatever you want) and a Quit button.
When the Submit button is clicked, display the information to the console.
You may use frames if you want but they are not required.
Add three lines of comments at the top: Name, Date, Class
Save the program as: Assign7-LastFinitial
Make sure your comments are descriptive.
Test the program and make sure it works.
Upload your program.
Here is example of output. Do your own thing. Do not copy mine exactly. Be creative
(I have two screen shots. If you cannot see them, please contact me ASAP.)


Assignment 8:
Design a program that includes the following widgets.
At least two labels
At least one entry widget
At least one frame
At least two check buttons
At least two buttons
At least one combobox
You must use a grid, so you might want to start with grid_demo.py.
Make sure some of your widgets span rows and/or columns.
At the end when the user clicks one of the buttons, print out the results of what the user entered.
Make the program cohesive, ie, make the program useful. Do not just put in a random bunch of widgets. For example, make a pizza delivery form or a hotel form. Be creative.
Save the program as: Assign8-LastFinitial
Make sure your comments are descriptive.
Test the program and make sure it works.
Upload your program.



Assignment 9:
Start with menubar_demo.py and do the following:
Design a program that includes the following menu items.
Three "tabs" for the menu. Example: File, Print, Help (But don't use these names!)
At least three menu items per tab. Include at least one separator per tab. All 9 menu items must have different names.
One menu item that will cause the program to quit or exit
Insert an image on the window.
Insert a label on the window.
You cannot use ANY of the same menu names that I did in menubar_demo
When you click on the menu item, you must do something.
One will exit the program.
At least 2 will open a dialog box
At least 2 will print something
Here is the hard part: all 9 of your menu items must do something different.
 They cannot all use the same function, ie, donothing. Each menu item must do something. Hey, nobody said event driven programming was easy!
Save the program as: Assign9-LastFinitial
Make sure your comments are descriptive.
This program is not hard. There are just a lot of steps to it. Plan ahead!!
Test the program and make sure it works.
Upload your program.



Assignment 10:
Start with file_demo.py and do the following:
Keep all the menu items as they are.
You will have three labels and three entry widgets on the screen.
The entry widgets will use:
firstName StringVar()
lastName StringVar()
age IntVar()
When the File, Save menu is chosen, you will write these variable to the same line to the file with a \n at the end. 
For example, if the user enters Mickey for the first name, Mouse for the last name, and 91 for the age:
You will display: Mouse, Mickey 91
Use the + to add the comma and spaces.
You will need the str() function to convert age to text.
You will also display in the same format on the console. 
See the output below.
Also add 2 buttons (Note: in the sample output, I do not show any buttons.) 
A Quit button that will end the program
A Save button that will transfer control to the same function that File, Save uses above.
Save the program as: Assign10-LastFinitial
Make sure your comments are descriptive.
Test the program and make sure it works.
Upload your program.
Sample output:



Assignment 11:
Start with one of your previous programs  such as the pizza delivery program or a hotel reservation system and do the following:
Modify the program to add a comments section (or call it whatever makes sense). Allow the user to enter information. 
Use a text box widget
Add a scrollbar.
Add a label describing what should be entered in the text box.
Add a second text box with or without the scrollbar and display something that the user cannot update.
Create a button that when clicked, instead of opening a dialog box, it opens a new window and displays the pizza order or whatever you are displaying.
Also display the contents of the entry text box.
At the same time, display everything to the console.
Add a Quit button that will end the program
Save the program as: Assign11-LastFinitial
Make sure your comments are descriptive.
Test the program and make sure it works.
Upload your program.



Assignment 12:
Start with your program from Assignment 11:
Modify the theme of your program.
Modify the program to add styles as follows: 
3 different styles for labels.
Do not just change the color. Try something I did not do. Do not use the same styles that I did.
Create a style for some of your other widgets.
A style for a button. Use for all buttons on your screen. Change for 'pressed' and 'active';
Save the program as: Assign12-LastFinitial
Make sure your comments are descriptive.
Test the program and make sure it works.
Upload your program.



Assignment 13:
This program will take some time to do, so do not wait until the last minute!!:
Now is your chance to do a real example. 
Make your program as close to the admissions page at Rockford University as possible. Here is the link: https://rnl.secure.force.com/form?formid=217724 (Links to an external site.)
Be sure to do the following:
See thetemplate below. (Note that this does no contain a Rockford logo. Also, this is not in Python format.)
See the output of my program down below. Your output does not need to be exactly like mine, but it should be close to the original.
You do not need the smaller text under the boxes. For example: no need to add "No Dashes" nor "MM/DD/YYYY"
Add any Rockford University logo at the top of the screen. Remember, the image must be in .gif format. Be sure to upload this file, also.
You do not need to add the background of the Burpee Student Center as shown in the website.
Use grids, not pack.
Create a style for most of the labels. You cannot use the same style for all. 
The official Rockford University purple text color is:  #522E91
Do not display the values for the Birth Date or Social Security Number when entered. Display asterisks.
Create the button that when pushed, displays the selections in a new window.
Do not just name your variables label1, label2, etc. Make the variable names descriptive: fname, mname, etc.
Your window will not look exactly like this, but try to get as close as you can.
Save the program as: Assign13-LastFinitial
Make sure your comments are descriptive.
Test the program and make sure it works.
Upload your program and your gif logo.
Template:

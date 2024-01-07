# Homework 4

# Searching for the largest number among 3 values program

# Need to ask user to input 3 numbers.
# Find and print the biggest number using if-else statement.
# Record the demo presenting the programs (less than 2 mins only)
# Submit the demo directly to Sir Danilo's messenger
# Deadline: BEFORE JAN 13, 2024!!!

import tkinter
from tkinter import Button

# Pseudo Code

# Proceeds into searching for the biggest number among the 3 given values by the user
def open():
    # Destroy Main Tab
    Main_Tab.destroy()

    # Creating 2nd Tab
    Next_Tab = tkinter.Tk()
    Next_Tab.title ("Input the Numbers")
    Next_Tab.geometry ("350x450")

    Input_Num_Frame = tkinter.Frame(Next_Tab)
    Input_Num_Frame.pack(expand=True, fill="both", padx=10, pady=10)
    Input_Num_Frame_Label = tkinter.Label(Next_Tab, text="Please enter 3 Numbers", font=('Figtree', 16, 'bold'))
    Input_Num_Frame_Label.place(relx=0.5, rely=0.1, anchor= "center")


    # Adding entry widgets
    First_Number_Entry = tkinter.Entry(Next_Tab)
    First_Number_Entry.place(relx=0.5, rely=0.2, anchor="center")

    Second_Number_Entry = tkinter.Entry(Next_Tab)
    Second_Number_Entry.place(relx=0.5, rely=0.3, anchor="center")

    Third_Number_Entry = tkinter.Entry(Next_Tab)
    Third_Number_Entry.place(relx=0.5, rely=0.4, anchor="center")

    Results_Frame = tkinter.Frame(Next_Tab)
    Results_Frame.pack(expand=True, fill="both", padx=10, pady=10)
    Results_Frame_Label = tkinter.Label(Next_Tab, text="Results:", font=('Figtree', 16, 'bold'))
    Results_Frame_Label.place(relx=0.5, rely=0.58, anchor= "center")


# Creating the main tab
Main_Tab = tkinter.Tk()
Main_Tab.title ("Biggest Number?") 
Main_Tab.geometry ("350x200")

# Creating the frame for main tab
Main_Frame = tkinter.Frame(Main_Tab)
Main_Frame.pack(expand=True, fill="both", padx=10, pady=10)
Main_Frame_Label = tkinter.Label(Main_Tab, text="Finding the biggest number", font=('Figtree', 16, 'bold'))
Main_Frame_Label.place(relx=0.5, rely=0.3, anchor= "center")

# Adding buttons to proceed and cancel
Proceed_Button = Button(Main_Tab, text="Proceed", command=open, font=('Figtree', 12, 'bold'))
Proceed_Button.place(relx=0.35, rely=0.6, anchor="center")

Cancel_Button = Button(Main_Tab, text="Cancel", command=exit, font=('Figtree', 12, 'bold'))
Cancel_Button.place(relx=0.65, rely=0.6, anchor="center")

# Can't resize the main tab
Main_Tab.resizable (False, False)

# Looping
Main_Tab.mainloop()
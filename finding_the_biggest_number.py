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
    Next_Tab.geometry ("500x350")

    # Adding a results frame
    Results_Frame = tkinter.Frame(Next_Tab)
    Results_Frame.pack(expand=True, fill="both", padx=10, pady=10)
    Results_Frame_Label = tkinter.Label(Next_Tab, text="Results:", font=('Figtree', 20, 'bold'))
    Results_Frame_Label.place(relx=0.5, rely=0.12, anchor= "center")

    #Finding out what number is the biggest among the 3
    Biggest_Num_Text = tkinter.Label(Results_Frame, text="The biggest number is:", font=('Figtree', 15, 'bold'))
    Biggest_Num_Text.place(relx=0.5, rely=0.3, anchor= "center")

    # Adding an exit button
    Exit_Button = Button(Next_Tab, text="Done", command=exit, font=('Figtree', 15, 'bold'))
    Exit_Button.place(relx=0.5, rely=0.86, anchor="center")

    # Getting the numbers
    First_Num = First_Number_Entry.get()
    Second_Num = Second_Number_Entry.get()
    Third_Num = Third_Number_Entry.get()

    def Which_One(First_Num, Second_Num, Third_Num):
        if (First_Num > Second_Num) and (First_Num > Third_Num):
            return First_Num
        elif (Second_Num > First_Num) and (Second_Num > Third_Num):
            return Second_Num
        else:
            return Third_Num
    
    Biggest_Num = Which_One(First_Num, Second_Num, Third_Num)
    Biggest_Num = tkinter.Label(Next_Tab)
    Biggest_Num.place(relx=0.5, rely=0.4, anchor= "center")


# Creating the main tab
Main_Tab = tkinter.Tk()
Main_Tab.title ("Biggest Number?") 
Main_Tab.geometry ("350x300")

# Creating the frame for main tab
Main_Frame = tkinter.Frame(Main_Tab)
Main_Frame.pack(expand=True, fill="both", padx=10, pady=10)
Main_Frame_Label = tkinter.Label(Main_Tab, text="Finding the Biggest Number", font=('Figtree', 16, 'bold'))
Main_Frame_Label.place(relx=0.5, rely=0.15, anchor= "center")

# Adding entry widgets
First_Number_Entry = tkinter.Entry(Main_Tab)
First_Number_Entry.place(relx=0.5, rely=0.33, anchor="center")

Second_Number_Entry = tkinter.Entry(Main_Tab)
Second_Number_Entry.place(relx=0.5, rely=0.48, anchor="center")

Third_Number_Entry = tkinter.Entry(Main_Tab)
Third_Number_Entry.place(relx=0.5, rely=0.63, anchor="center")

# Adding buttons to proceed and cancel
Proceed_Button = Button(Main_Tab, text="Proceed", command=open, font=('Figtree', 12, 'bold'))
Proceed_Button.place(relx=0.35, rely=0.83, anchor="center")

Cancel_Button = Button(Main_Tab, text="Cancel", command=exit, font=('Figtree', 12, 'bold'))
Cancel_Button.place(relx=0.65, rely=0.83, anchor="center")

# Can't resize the main tab
Main_Tab.resizable (False, False)

# Looping
Main_Tab.mainloop()
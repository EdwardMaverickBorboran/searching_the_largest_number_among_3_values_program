#Homework 4

#Searching for the largest number among 3 values program

#Need to ask user to input 3 numbers.
#Find and print the biggest number using if-else statement.
#Record the demo presenting the programs (less than 2 mins only)
#Submit the demo directly to Sir Danilo's messenger
#Deadline: BEFORE JAN 13, 2024!!!

import tkinter
from tkinter import Button

#Pseudo Code

#Creating the main tab
Main_Tab = tkinter.Tk()
Main_Tab.title ("Biggest Number?")
Main_Tab.geometry ("350x500")

#Creating the frame for main tab
Main_Frame = tkinter.Frame(Main_Tab)
Main_Frame.pack(expand=True, fill="both", padx=10, pady=10)
Main_Frame_Label = tkinter.Label(Main_Tab, text="Which is the biggest number?", font=('Figtree', 16, 'bold'))
Main_Frame_Label.place(relx=0.5, rely=0.085, anchor= "center")

#Adding entry widgets
First_Num_Entry = tkinter.Entry(Main_Tab)
First_Num_Entry.place(relx=0.5, rely=0.2, anchor="center")

Second_Num_Entry = tkinter.Entry(Main_Tab)
Second_Num_Entry.place(relx=0.5, rely=0.3, anchor="center")

Third_Number_Entry = tkinter.Entry(Main_Tab)
Third_Number_Entry.place(relx=0.5, rely=0.4, anchor="center")

#Adding button to proceed
Proceed_Button= Button(Main_Tab, text="Proceed", command=open,font=('Figtree', 12, 'bold'))
Proceed_Button.place(relx=0.5, rely=0.52, anchor="center")

#Can't resize the main tab
Main_Tab.resizable (False, False)

#Looping
Main_Tab.mainloop()
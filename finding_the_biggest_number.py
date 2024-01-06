#Homework 4

#Searching for the largest number among 3 values program

#Need to ask user to input 3 numbers.
#Find and print the biggest number using if-else statement.

import tkinter


#Creating the main tab
Main_Tab = tkinter.Tk()
Main_Tab.title ("Biggest Number?")
Main_Tab.geometry ("350x400")

#Creating the frame for main tab
Main_Frame = tkinter.Frame(Main_Tab)
Main_Frame.pack(expand=True, fill="both", padx=10, pady=10)
Main_Frame_Label = tkinter.Label(Main_Tab, text="Which is the biggest number?", font=('Figtree', 15, 'bold'))
Main_Frame_Label.place(relx=0.5, rely=0.09, anchor= "center")

#Can't resize the main tab
Main_Tab.resizable (False, False)

#Looping
Main_Tab.mainloop()
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
    first_num = float(first_number_entry.get())
    second_num = float(second_number_entry.get())
    third_num = float(third_number_entry.get())

    # Destroy Main Tab
    main_tab.destroy()

    # Creating 2nd Tab
    next_tab = tkinter.Tk()
    next_tab.title ("Input the Numbers")
    next_tab.geometry ("500x350")

    # Adding a results frame
    results_frame = tkinter.Frame(next_tab)
    results_frame.pack(expand=True, fill="both", padx=10, pady=10)
    results_frame_label = tkinter.Label(next_tab, text="Results:", font=('Figtree', 20, 'bold'))
    results_frame_label.place(relx=0.5, rely=0.12, anchor= "center")

    # Title text for the biggest number
    biggest_num_text = tkinter.Label(results_frame, text="The biggest number is:", font=('Figtree', 15, 'bold'))
    biggest_num_text.place(relx=0.5, rely=0.3, anchor= "center")

    # Adding an exit button
    exit_button = Button(next_tab, text="Done", command=exit, font=('Figtree', 15, 'bold'))
    exit_button.place(relx=0.5, rely=0.86, anchor="center")

    # Getting the numbers
    def which_one(first_num, second_num, third_num):
        if (first_num >= second_num) and (first_num >= third_num):
            return first_num
        elif (second_num >= first_num) and (second_num >= third_num):
            return second_num
        else:
            return third_num
        
    # Finding out what is the biggest number among the 3
    biggest_num = which_one(first_num, second_num, third_num)
    biggest_number = tkinter.Label(next_tab, text= biggest_num)
    biggest_number.place(relx=0.5, rely=0.4, anchor= "center")


# Creating the main tab
main_tab = tkinter.Tk()
main_tab.title ("Biggest Number?") 
main_tab.geometry ("350x300")

# Creating the frame for main tab
main_frame = tkinter.Frame(main_tab)
main_frame.pack(expand=True, fill="both", padx=10, pady=10)
main_frame_label = tkinter.Label(main_tab, text="Finding the Biggest Number", font=('Figtree', 16, 'bold'))
main_frame_label.place(relx=0.5, rely=0.15, anchor= "center")

# Adding entry widgets
first_number_entry = tkinter.Entry(main_tab)
first_number_entry.place(relx=0.5, rely=0.33, anchor="center")

second_number_entry = tkinter.Entry(main_tab)
second_number_entry.place(relx=0.5, rely=0.48, anchor="center")

third_number_entry = tkinter.Entry(main_tab)
third_number_entry.place(relx=0.5, rely=0.63, anchor="center")

# Adding buttons to proceed and cancel
proceed_button = Button(main_tab, text="Proceed", command=open, font=('Figtree', 12, 'bold'))
proceed_button.place(relx=0.35, rely=0.83, anchor="center")

cancel_button = Button(main_tab, text="Cancel", command=exit, font=('Figtree', 12, 'bold'))
cancel_button.place(relx=0.65, rely=0.83, anchor="center")

# Can't resize the main tab
main_tab.resizable (False, False)

# Looping
main_tab.mainloop()
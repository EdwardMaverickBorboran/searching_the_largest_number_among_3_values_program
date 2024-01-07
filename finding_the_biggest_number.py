# Homework 4

# Searching for the largest number among 3 values program

# Need to ask user to input 3 numbers.
# Find and print the biggest number using if-else statement.
# Record the demo presenting the programs (less than 2 mins only)
# Submit the demo directly to Sir Danilo's messenger

# Deadline: BEFORE JAN 13, 2024!!!

import customtkinter
from tkinter import messagebox

# Pseudo Code

# Proceeds into searching for the biggest number among the 3 given values by the user
def open():
    # Validation for the numbers
    if input_first_digit.get() and input_second_digit.get() and input_third_digit.get():

        all_number = (input_first_digit.get() + input_second_digit.get() + input_third_digit.get())
        if all_number.isdigit():

            first_digit = float(input_first_digit.get())
            second_digit = float(input_second_digit.get())
            third_digit = float(input_third_digit.get())

            # Destroy Main Tab
            global main_tab
            main_tab.destroy() 

            # Creating 2nd Tab
            next_tab = customtkinter.CTk()
            next_tab.title ("Input the Numbers")
            next_tab.geometry ("500x350")

            # Adding a results frame
            results_frame = customtkinter.CTkFrame(next_tab)
            results_frame.pack(expand=True, fill="both", padx=10, pady=10)
            results_frame_label = customtkinter.CTkLabel(next_tab, text="Results:", font=('Figtree', 30, 'bold'))
            results_frame_label.place(relx=0.5, rely=0.15, anchor= "center")

            # Title text for the biggest number
            biggest_num_text = customtkinter.CTkLabel(results_frame, text="The biggest number is:", font=('Figtree', 18, 'bold'))
            biggest_num_text.place(relx=0.5, rely=0.36, anchor= "center")

            # Adding an exit button
            exit_button = customtkinter.CTkButton(next_tab, text="Done", command=exit, font=('Figtree', 15, 'bold'))
            exit_button.place(relx=0.5, rely=0.86, anchor="center")

            # Main funtion in finding the biggest number
            if (first_digit >= second_digit) and (first_digit >= third_digit):
                biggest = first_digit
            elif (second_digit >= first_digit) and (second_digit >= third_digit):
                biggest = second_digit
            else:
                biggest = third_digit

            # Finding out what is the biggest number among the 3
            biggest_number_results = customtkinter.CTkLabel(next_tab, text= biggest, font=('Figtree', 30, 'bold'))
            biggest_number_results.place(relx=0.5, rely=0.575, anchor= "center")

        else:
            messagebox.showerror(title="Invalid", message="Please input numbers only.")  
    else:
        messagebox.showerror(title="Error", message="Please fill out the blanks.")  
    
    next_tab.mainloop()


# Setting up the appearance 
customtkinter.set_appearance_mode("light")

# Creating the main tab
main_tab = customtkinter.CTk()
main_tab.title ("Biggest Number?") 
main_tab.geometry ("350x300")

# Creating the main frame for main tab
main_frame = customtkinter.CTkFrame(main_tab)
main_frame.pack(expand=True, fill="both", padx=10, pady=10)
main_frame_label = customtkinter.CTkLabel(main_tab, text="Finding the Biggest Number", font=('Figtree', 16, 'bold'))
main_frame_label.place(relx=0.5, rely=0.15, anchor= "center")

# Adding entry widgets and its placements
input_first_digit = customtkinter.CTkEntry(main_frame)
input_first_digit.place(relx=0.5, rely=0.33, anchor="center")

input_second_digit = customtkinter.CTkEntry(main_frame)
input_second_digit.place(relx=0.5, rely=0.48, anchor="center")

input_third_digit = customtkinter.CTkEntry(main_frame)
input_third_digit.place(relx=0.5, rely=0.63, anchor="center")

# Adding buttons to proceed and cancel
proceed_button = customtkinter.CTkButton(main_tab, text="Proceed", command=open, font=('Figtree', 12, 'bold'))
proceed_button.place(relx=0.35, rely=0.83, anchor="center")

cancel_button = customtkinter.CTkButton(main_tab, text="Cancel", command=exit, font=('Figtree', 12, 'bold'))
cancel_button.place(relx=0.65, rely=0.83, anchor="center")

# Can't resize the main tab
main_tab.resizable (False, False)

# Looping
main_tab.mainloop()
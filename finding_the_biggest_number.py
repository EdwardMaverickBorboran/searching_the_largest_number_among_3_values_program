# Homework 4

# Searching for the largest number among 3 values program

# Need to ask user to input 3 numbers.
# Find and print the biggest number using if-else statement.
# Record the demo presenting the programs (less than 2 mins only)
# Submit the demo directly to Sir Danilo's messenger

# Deadline: BEFORE JAN 13, 2024!!!

import customtkinter
from tkinter import messagebox
from PIL import Image

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

            # Destroy Main Frame
            global main_frame
            main_frame.destroy() 

            # Adding a results frame
            results_frame = customtkinter.CTkFrame(main_tab, fg_color='snow')
            results_frame.pack(expand=True, fill="both", padx=10, pady=10)
            results_frame_label = customtkinter.CTkLabel(results_frame, text="Outcome", font=('Consolas', 50, 'bold'))
            results_frame_label.place(relx=0.757, rely=0.19, anchor= "center")

            # Adding 2nd image
            dc_image_2 = customtkinter.CTkImage(Image.open("Conan2.png"), size=(350, 500))
            dc_image_2_input = customtkinter.CTkLabel(results_frame, text="", image=dc_image_2)
            dc_image_2_input.place(relx=0.25, rely=0.499, anchor= "center")

            # Title text for the biggest number
            biggest_num_text = customtkinter.CTkLabel(results_frame, text="The biggest number is:", font=('Consolas', 25, 'bold'), fg_color='snow')
            biggest_num_text.place(relx=0.756, rely=0.43, anchor= "center")

            # Adding an exit button
            exit_button = customtkinter.CTkButton(main_tab, text="Done", command=exit, font=('Consolas', 15, 'bold'), fg_color="red3", bg_color='snow')
            exit_button.place(relx=0.755, rely=0.88, anchor="center")

            # Main funtion in finding the biggest number
            if (first_digit >= second_digit) and (first_digit >= third_digit):
                biggest = first_digit
            elif (second_digit >= first_digit) and (second_digit >= third_digit):
                biggest = second_digit
            else:
                biggest = third_digit

            # Finding out what is the biggest number among the 3
            biggest_number_results = customtkinter.CTkLabel(results_frame, text= biggest, font=('Consolas', 55, 'bold'), text_color=('midnight blue'), fg_color='snow')
            biggest_number_results.place(relx=0.756, rely=0.58, anchor= "center")

        else:
            messagebox.showerror(title="Invalid", message="Please input numbers only.")  
    else:
        messagebox.showerror(title="Error", message="Please fill out the blanks.") 


# Setting up the appearance 
customtkinter.set_appearance_mode("light")

# Creating the main tab
main_tab = customtkinter.CTk(fg_color='sienna4')
main_tab.title ("Biggest Number?") 
main_tab.geometry ("700x500")

# Creating the main frame for main tab
main_frame = customtkinter.CTkFrame(main_tab, fg_color='snow')
main_frame.pack(expand=True, fill="both", padx=10, pady=10)
main_frame_label = customtkinter.CTkLabel(main_frame, text="Detective Conan", font=('Calibri', 42, 'bold'), text_color="black")
main_frame_label.place(relx=0.756, rely=0.1, anchor= "center")
main_frame_label_2 = customtkinter.CTkLabel(main_frame, text="ADVENTURES", font=('Calibri', 50, 'bold'), text_color="black")
main_frame_label_2.place(relx=0.756, rely=0.2, anchor= "center")

# Adding image
dc_image = customtkinter.CTkImage(Image.open("Conan.png"), size=(350, 500))
dc_image_input = customtkinter.CTkLabel(main_frame, text="", image=dc_image)
dc_image_input.place(relx=0.25, rely=0.499, anchor= "center")

# Adding entry widgets and its placements
input_first_digit = customtkinter.CTkEntry(main_frame, placeholder_text="Input the 1st number here..",placeholder_text_color="black", width=260, corner_radius=8, font=('Consolas', 12.5, 'bold'), fg_color='white')
input_first_digit.place(relx=0.756, rely=0.35, anchor="center")

input_second_digit = customtkinter.CTkEntry(main_frame, placeholder_text="Input the 2nd number here..",placeholder_text_color="black", width=260, corner_radius=8, font=('Consolas', 12.5, 'bold'), fg_color='white')
input_second_digit.place(relx=0.756, rely=0.49, anchor="center")

input_third_digit = customtkinter.CTkEntry(main_frame, placeholder_text="Input the 3rd number here..",placeholder_text_color="black", width=260, corner_radius=8, font=('Consolas', 12.5, 'bold'), fg_color='white')
input_third_digit.place(relx=0.756, rely=0.63, anchor="center")

# Adding buttons to proceed and cancel
proceed_button = customtkinter.CTkButton(main_tab, text="Proceed", command=open, font=('Calibri', 15, 'bold'), fg_color="forest green", bg_color='snow')
proceed_button.place(relx=0.755, rely=0.77, anchor="center")

cancel_button = customtkinter.CTkButton(main_tab, text="Cancel", command=exit, font=('Calibri', 15, 'bold'), fg_color="red3", bg_color='snow')
cancel_button.place(relx=0.755, rely=0.87, anchor="center")

# Can't resize the main tab
main_tab.resizable (False, False)

# Looping
main_tab.mainloop()
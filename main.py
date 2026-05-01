"""
survival caluclator 
this gane will calculate if you are paying for your phone plan,
paying for monthly groceries, paying rent,and then it will calculate the total payment 
for the month.
"""

# Import tinker for GUI making 
import tkinter as tk 
# Set up the root window 
root = tk.Tk()
root.title("Survival Calculator")

# function for doing the calulation 
def calculate_payment():

    phone_plan = float(entry_phone_plan.get()) # get payment for phone 

    rent  = float(entry_rent.get())  # Get rent payment 

    grocery = float(entry_grocery.get())  # Get grocery payment
    
    calculate_payment = round(phone_plan + rent + grocery, 2)  # Calculates the total payment
    
# create and place GUI widgets on a grid 
label_phone_plan = tk.Label(root, text="Mass: ")  # phone plan label 
label_phone_plan.grid(column=0, row=1)

entry_phone_plan = tk.Entry(root)  # phone plan entry
entry_phone_plan.grid(column=1, row=0) 

label_rent = tk.Label(root, text="Height: ") # rent label
label_rent.grid(column=0, row=2)

entry_rent = tk.Entry(root)
entry_rent.grid(column=1, row=2) # rent entry 

label_grocery = tk.Label(root, text="Mass: ")  # grocery label 
label_grocery.grid(column=0, row=3)

entry_grocery = tk.Entry(root)  # grocery entry
entry_grocery.grid(column=1, row=0) 

# this is where I added check button for the groceries so then the user can comferm that they 
# payed for there groceries 
check_grocery = tk.Checkbutton(root, text="Include Groceries", variable=include_grocery)
check_grocery.grid(column=0, row=3, columnspan=2)

button_calculate = tk.Button(root, text="calculate",  # Button
                             command= caluculate_payment) 
button_calculate.grid(column=0, row=2)

# this is the code for the message wiget
label_result = tk.Label(root, text="Total Monthly Payment: $0.00")
label_result.grid(column=1, row=3)

# This is the code for the text box wiget
text_box = tk.Text(root, height=5, width=40)
text_box.grid(column=0, row=4, columnspan=2, pady=10)

#  result label 
label_calculate = tk.Label(root, text="Caluculate: ")
label_calculate.grid(column=1, row=2)

# event loop 
root.mainloop()



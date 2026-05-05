import tkinter as tk
("""
survival caluclator 
this gane will calculate if you are paying for your phone plan,
paying for monthly groceries, paying rent,and then it will calculate the total payment 
for the month.
""")


root = tk.Tk()
root.title("Survival Calculator")

include_grocery = tk.BooleanVar()



def calculate_payment():
    phone_plan = float(entry_phone_plan.get())
    rent = float(entry_rent.get())

    grocery = 0
    if include_grocery.get():
        grocery = float(entry_grocery.get())

    total_payment = round(phone_plan + rent + grocery, 2)
    label_result.config(text=f"Total Monthly Payment: ${total_payment:.2f}")



# -------------------------
# FRAME FOR INPUT WIDGETS
# -------------------------
input_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
input_frame.grid(row=0, column=0, columnspan=2, pady=10)

# Labels + Entries INSIDE THE FRAME
label_phone_plan = tk.Label(input_frame, text="Phone Plan ($):")
label_phone_plan.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_phone_plan = tk.Entry(input_frame, width=20)
entry_phone_plan.grid(row=0, column=1, padx=10, pady=5)

label_rent = tk.Label(input_frame, text="Rent ($):")
label_rent.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_rent = tk.Entry(input_frame, width=20)
entry_rent.grid(row=1, column=1, padx=10, pady=5)

label_grocery = tk.Label(input_frame, text="Groceries ($):")
label_grocery.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_grocery = tk.Entry(input_frame, width=20)
entry_grocery.grid(row=2, column=1, padx=10, pady=5)

check_grocery = tk.Checkbutton(input_frame, text="Include Groceries", variable=include_grocery)
check_grocery.grid(row=3, column=0, columnspan=2, pady=5)


# Checkbox
check_grocery = tk.Checkbutton(
    root, text="Include Groceries", variable=include_grocery)
check_grocery.grid(row=3, column=0, columnspan=2, pady=5)

# Button (centered)
button_calculate = tk.Button(root, text="Calculate", command=calculate_payment)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# Result label
label_result = tk.Label(root, text="Total Monthly Payment: $0.00")
label_result.grid(row=5, column=0, columnspan=2, pady=5)

# Text box (bottom)
text_box = tk.Text(root, height=5, width=40)
text_box.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()

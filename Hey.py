import tkinter as tk
import random

# Function to calculate the total amount
def calculating_the_total_amount():
    try:
        # Placeholder for Converted_Cubic_Meter (to be replaced with actual logic)
        Converted_Cubic_Meter = float(cubic_meter_entry.get())  # Assume user inputs this value
        VAT = Converted_Cubic_Meter * 0.12
        Arrears = float(arrears_entry.get())
        Total_Amount = VAT + Arrears + Converted_Cubic_Meter

        # Update result label with the calculated total
        result_label.config(
            text=f"Converted Cubic Meter: {Converted_Cubic_Meter:.2f} PHP\n"
                 f"VAT (12%): {VAT:.2f} PHP\n"
                 f"Arrears: {Arrears:.2f} PHP\n"
                 f"Total Amount: {Total_Amount:.2f} PHP"
        )
    except ValueError:
        result_label.config(text="Please enter valid numeric inputs.")

# Function to generate and display the WIN number
def generate_win():
    WIN = random.randint(100000, 999999)
    win_label.config(text=f"WIN Number: {WIN}")

# Initialize Tkinter window
root = tk.Tk()
root.title("Water Bill Calculator")
root.geometry("400x400")

# Input for cubic meter
tk.Label(root, text="Enter Cubic Meter (in Peso):").pack(pady=5)
cubic_meter_entry = tk.Entry(root)
cubic_meter_entry.pack()

# Input for arrears
tk.Label(root, text="Enter Past Accumulated Debts (Arrears):").pack(pady=5)
arrears_entry = tk.Entry(root)
arrears_entry.pack()

# Button to calculate the total amount
calculate_button = tk.Button(root, text="Calculate Total Amount", command=calculating_the_total_amount)
calculate_button.pack(pady=10)

# Button to generate WIN number
win_button = tk.Button(root, text="Generate WIN Number", command=generate_win)
win_button.pack(pady=10)

# Labels to display results
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

win_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
win_label.pack(pady=10)

# Run the application
root.mainloop()
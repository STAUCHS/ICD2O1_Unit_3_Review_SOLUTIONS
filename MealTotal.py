#-------------------------------------------------------------------------
# Name:         Meal Total
# Purpose:      Calculates the tax, tips, and total amount of a meal
# Author:       Chen. C
# Created:      26/03/2024
#-------------------------------------------------------------------------

# Get the meal total, tax %, and tip % from user
meal_charge = float(input("Enter the charge of the meal: "))
tax_percent = int(input("Enter the sales tax rate (%): "))
tip_percent = int(input("Enter the percentage of the tips (%): "))

# Calculate the tax amount, tip amount, and total amount after tax and tips
tax_amount = round(meal_charge * tax_percent / 100, 2)
tip_amount = round(meal_charge * tip_percent / 100, 2)
total_amount = meal_charge + tax_amount + tip_amount

# Output results
print(f"\nThe total charge is ${meal_charge}")
print(f"The taxes amount is ${tax_amount}")
print(f"The tip amount is ${tip_amount}")
print(f"The total amount of the bill including taxes and tips is ${total_amount}")
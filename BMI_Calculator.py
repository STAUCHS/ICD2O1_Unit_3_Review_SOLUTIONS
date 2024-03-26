#-------------------------------------------------------------------------
# Name:         BMI Calculator
# Purpose:      Calculate the user's BMI based on their height in meters and weight in kg
# Author:       Chen. C
# Created:      26/03/2024
#-------------------------------------------------------------------------

# Get height and weight from user
height_m = float(input("Height (in m): "))
weight_kg = float(input("Weight (in kg): "))

# Calculate the BMI
bmi = round(weight_kg / height_m**2, 1)

# Output results
print(f"Your BMI is {bmi}.")
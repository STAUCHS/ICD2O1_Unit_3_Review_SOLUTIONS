#-------------------------------------------------------------------------
# Name:         Age in Five Years
# Purpose:      Calculates the age of the user in five years
# Author:       Chen. C
# Created:      26/03/2024
#-------------------------------------------------------------------------

# Get user's name and age
name = input("Hello. What is your name? ")
age = int(input(f"\nHi, {name}!\nHow old are you? "))

# Calculate user's age five years ago and in five years
previous_age = age - 5
future_age = age + 5

# Output information
print(f"\nDid you know that in five years you will be {future_age} years old?")
print(f"And five years ago you were {previous_age}! Imagine that!")
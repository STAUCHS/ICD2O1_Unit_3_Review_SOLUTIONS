#-------------------------------------------------------------------------
# Name:         Volume and Surface Area of a Sphere
# Purpose:      Calculates the volume and surface area of a sphere given radius
# Author:       Last Name. First Initial
# Created:      dd/mm/yyyy
#-------------------------------------------------------------------------

import math

# Output title
print("** Volume and Surface Area of Sphere Calculator **")

# Get radius from user
radius = float(input("Enter the radius of the sphere: "))

# Calculate volume and surface area
volume = round((4/3) * math.pi * radius**3, 2)
surface_area = round(4 * math.pi * radius**2, 2)

# Output information
print(f"\nRadius = {radius} units")
print(f"Volume = {volume} cubic units")
print(f"Surface Area = {surface_area} square units")
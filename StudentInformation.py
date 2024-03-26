#-------------------------------------------------------------------------
# Name:         
# Purpose:      
# Author:       Last Name. First Initial
# Created:      dd/mm/yyyy
#-------------------------------------------------------------------------

# Output title
print("Please enter the following information:")

# Get info from user
first_name = input("\nFirst name: ")
last_name = input("Last name: ")
grade = input("Grade (9-12): ")
student_ID_number = input("Student ID: ")
email_login = input("Email/Login: ")
average = float(input("Average: "))

# Output user information
print("Your information:")
print(f"\tEmail/Login: {email_login}")
print(f"\tStudent ID: {student_ID_number}")
print(f"\tName: {first_name} {last_name}")
print(f"\tAverage: {average}%")
print(f"\tGrade: {grade}")

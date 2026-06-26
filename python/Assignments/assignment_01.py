#Student Admission Eligibility Checker
Student_Name = input("Enter a student name:")
Age = int(input('Enter Student Age:'))
Degree = input('Enter a Degree:')
Percentage = float(input('Enter Percentage:'))
print('Student Name:',Student_Name)
print('Student_Age',Age)
print('Student_Degree',Degree)
print('Percentage',Percentage)


# inputs
student_name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
degree = input("Enter Degree: ")
percentage = float(input("Enter Percentage: "))

# Details
print("\n--- Student Details ---")
print("Name:", student_name)
print("Age:", age)
print("Degree:", degree)
print("Percentage:", percentage)

#eligibility checker
if percentage >= 60:
    eligibility = "Eligible"
else:
    eligibility = "Not Eligible"

print("Admission Status:", eligibility)

# Calculations
years_remaining = 30 - age
percentage_required = 100 - percentage

print("Years remaining to reach age 30:", years_remaining)
print("Percentage required to reach 100:", percentage_required)

# Employee Attendance Monitoring System

excellent_count = 0
good_count = 0
improvement_count = 0
total_processed = 0

for emp in range(1, 11):

    attendance = float(input(f"Employee {emp} Attendance: "))

    # Part C - break
    if attendance == -1:
        print("Data entry stopped by user.")
        break

    # Part D - continue
    if attendance == 0:
        print(f"Employee {emp}: Record Skipped")
        continue

    # Part E - pass
    if attendance > 100:
        pass
       

    # Part A - Classification
    if attendance >= 90:
        category = "Excellent"
        excellent_count += 1

    elif attendance >= 75:
        category = "Good"
        good_count += 1

    else:
        category = "Improvement Required"
        improvement_count += 1

    print(f"Employee {emp}: {category}")

    total_processed += 1

# Part B - Summary
print("\nAttendance Summary")
print("-------------------")
print("Total Employees Processed :", total_processed)
print("Excellent :", excellent_count)
print("Good :", good_count)
print("Improvement Required :", improvement_count)


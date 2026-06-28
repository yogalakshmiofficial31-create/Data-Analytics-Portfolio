import os
print(os.getcwd())

file = open("python/Assignments/assignment_05_customer_feedback_processing/company_notice.txt", "r")
content = file.read()
print(content)
file.close()

file = open("python/Assignments/assignment_05_customer_feedback_processing/feedback.csv", "r")
for line in file:
    print(line.strip())
file.close()



total_customers = 5
valid_ratings = 3
invalid_ratings = 2
average_rating = 4.0


file = open("feedback_summary.txt", "w")


file.write("Customer Feedback Summary\n\n")
file.write(f"Total Customers : {total_customers}\n")
file.write(f"Valid Ratings : {valid_ratings}\n")
file.write(f"Invalid Ratings : {invalid_ratings}\n")
file.write(f"Average Rating : {average_rating}\n")


file.close()

print("feedback_summary.txt created successfully.")


#exception handling
try:
    file = open("feedback.csv", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Feedback file not found.")

try:
    rating = int("abc")
    print(rating)

except ValueError:
    print("Invalid rating found.")

rating = ""

if rating == "":
    print("Empty rating found.")
else:
    print("Rating:", rating)

try:
    file = open("python/Assignments/assignment_05_customer_feedback_processing/feedback.csv", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Feedback file not found.")

finally:
    print("Processing Completed")

import csv

total_customers = 0
valid_ratings = 0
invalid_ratings = 0
ratings = []

with open("python/Assignments/assignment_05_customer_feedback_processing/feedback.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_customers += 1

        try:
            rating = int(row["Rating"])

            if 1 <= rating <= 5:
                ratings.append(rating)
                valid_ratings += 1
            else:
                invalid_ratings += 1

        except ValueError:
            invalid_ratings += 1

average_rating = sum(ratings) / len(ratings)
highest_rating = max(ratings)
lowest_rating = min(ratings)

print("Customer Feedback Processing Report\n")
print("Total Customers :", total_customers)
print("Valid Ratings :", valid_ratings)
print("Invalid Ratings :", invalid_ratings)
print("Average Rating :", average_rating)
print("Highest Rating :", highest_rating)
print("Lowest Rating :", lowest_rating)


import csv

with open("python/Assignments/assignment_05_customer_feedback_processing/feedback.csv", "r") as infile, open("python/Assignments/assignment_05_customer_feedback_processing/clean_feedback.csv", "w", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write header
    header = next(reader)
    writer.writerow(header)

    # Process records
    for row in reader:
        try:
            rating = int(row[2])

            if 1 <= rating <= 5:
                writer.writerow(row)

        except ValueError:
            continue

print("Valid records saved successfully.")

















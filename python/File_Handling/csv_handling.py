import csv
with open("data.csv",'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
'''import csv
with open("data.csv",'w',newline=' ') as file:
    writer = csv.writer(file)
    writer.writerow(['Ink','25'])
    writer.writerow(['Ballpen',10])'''

#This stored as dictionary reader
import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    totalSales = 0
    for row in reader:
        # Capital S to match your actual file header
        totalSales = totalSales + int(row['Sales'])
        
print(totalSales)




    



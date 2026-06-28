from sales_utils import (
    calculate_total_sales,
    calculate_average_sales,
    highest_sale,
    lowest_sale,
    sales_growth
    
)

sales = [12000, 15000, 18000, 9000, 21000, 17000]

print("Total Sales:", calculate_total_sales(sales))
print("Average Sales:", calculate_average_sales(sales))
print("Highest Sale:", highest_sale(sales))
print("Lowest Sale:", lowest_sale(sales))
from datetime import datetime
now = datetime.now()
print("current Date=",now.strftime('%d-%m-%y'))
print("Sales growth", sales_growth(25000,20000))
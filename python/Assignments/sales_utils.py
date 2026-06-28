def calculate_total_sales(sales):
    return sum(sales)

def calculate_average_sales(sales):
    return sum(sales) / len(sales)

def highest_sale(sales):
    return max(sales)

def lowest_sale(sales):
    return min(sales)

def sales_growth(current_month,previous_month):
    growth = ((current_month - previous_month) / previous_month) * 100
    return growth

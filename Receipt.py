# Lovely Loveseats for Neat Suites on Fleet Street catalog

# Loveseat Description
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on 
wood. 32 inches high x 40 inches wide x 30 
inches deep. Red or white.
"""
lovely_loveseat_price = 254.00

# Settee Description
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 
inches high x 54.75 inches wide x 28 inches 
deep. Black.
"""
stylish_settee_price = 180.50

# Lamp Description
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches 
tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15


# Sales Tax
sales_tax = 0.88

# Customer One Receipt
customer_one_total = 0
customer_one_itemization = ""

# Customer Purchases Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Customer Purchases Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Calculate Sales Tax and Add to Total
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Print Receipt with Item Descriptions
print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(customer_one_total)

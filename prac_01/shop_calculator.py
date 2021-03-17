"""
Program to calculate the total price for a number of items, each of a different price
If the total price is more than $100, a discount of 10% is applied before displaying the total price
"""

number_of_items = int(input("Number of items: "))
total_price = 0
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Price of item: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: $"))
    total_price = total_price + price_of_item  # Add item prices
if total_price > 100:
    discount = total_price / 10
    total_price = total_price - discount # Apply the 10% discount
# String formatting to display result to 2 decimal places
print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))

# Title: Total Purchase
# Author: Andrew Bittner
# Date: 9/13/2024

def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.

    item1 = input("Please enter the price of item one: ")
    item2 = input("Please enter the price of item two: ")
    item3 = input("Please enter the price of item three: ")
    item4 = input("Please enter the price of item four: ")
    item5 = input("Please enter the price of item five: ")

    subtotal = item1 + item2 + item3 +item4 +item5
    tax = 0.07
    total = subtotal * (1 + 0.07)

print("Alright, that comes to a subtotal of ", subtotal, "plus " int(tax * 10) "% tax, which comes to a total of ", total "$." sep ='')

calculate_total_purchase()
# Assignment 1 - Part 1: Data Quality Checker
# Author: Shashank Gautam
# Date: February 7, 2026

# This program collects numeric data from the user, validates entries,
# identifies outliers, and generates summary statistics.

values = []
negative_count = 0
print("")
print("")
print("=== Data Quality Checker ===")
print("")

while True:
    user_input = input("Enter a number (or 'done' to finish): ")

    # Checks if user wants to stop
    if user_input == "done":
       break

    # Changes input into floating value
    number = float(user_input)

    # Add new inputs at last
    values.append(number)
    
     # Check for negative value
    if number < 0:
        print("< ⚠ Warning, Negative value detected.>")
        negative_count = negative_count + 1



 # Displays how many inputs/values are collected.
print("")
print("Data collection complete.",len(values),"values recorded.")
print("")

# Displays Negative count

#just use simple logic of inequality(<,>,=)
if negative_count > 0:
    print("⚠ ",negative_count,"Negative values were flagged!")

else:
    print("No negative values detected.")
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



print("")
print("")
print("=== Outlier Detection ===")
print("")


threshold = float(input("Enter threshold for outlier detection: "))
print("")
outlier_count = 0

# Displays Outliers in the list(values)

# For finding out the outliers , a for loop runs through 
# the list(values) and check each entry if it is greater than 
# threshold and if yes, it will count each outlier and prints them

for value in values:
    if value > threshold:
       if outlier_count == 0:
          print("Outliers detected (values > ",threshold,"):")
       outlier_count = outlier_count + 1
       print(" - ",value)

print("")
if outlier_count > 0:
    print("Total outliers: ",outlier_count)    
else:
        print("No outliers detected.")



print("")
print("")
print("=== Summary Statistics ===")
print("")

count_values = len(values)  # Counts number of entries in list (values)
min_values = round(min(values),2)  # Shows smallest entry/value in list (values)
max_values = round(max(values),2)  # Shows largest entry/value in list (values)
average_values = sum(values)/len(values)  # Calculates average of all entries in list (values) 

print("Count:  ",count_values)    
print("Minimum:  ",min_values)
print("Maximum:  ",max_values)
print("Average:  ",average_values)
print("")
print("")
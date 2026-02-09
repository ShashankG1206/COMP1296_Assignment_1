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
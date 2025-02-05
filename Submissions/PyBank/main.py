# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis_VHR.txt")  # Output file path

# Define variables to track the financial data
total_months = 0 # Counter for total months in dataset
total_net = 0 # Track the total net amount of "Profit/Losses"


# Add more variables to track other necessary financial data
net_change_list = [] # List to store changes in "Profit/Losses" between months
month_list = []
max_increase = ['', 0] # Store month and value of greatest profit increase
max_decrease = ['', 0] # Store month and value of greatest loss decrease


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1]) # Add the first month's profit/loss
    previous_net = int(first_row[1]) # Store the first month's profit/loss for comparison


    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1 # Increment the total month count
        total_net += int(row[1]) # Add the current month's profit/loss to the total

        # Track the net change
        net_change = int(row[1]) - previous_net # Calculate month-over-month change
        previous_net = int(row[1]) # Update previous month's profit/loss for the next iteration
        net_change_list.append(net_change) # Add this month's change to the list
        month_list.append(row[0]) # Add the month to the change list

        # Calculate the greatest increase in profits (month and amount)
        if net_change > max_increase[1]:
            max_increase = [row[0], net_change]
        
        # Calculate the greatest decrease in losses (month and amount)
        if net_change < max_decrease[1]:
            max_decrease = [row[0], net_change]

# Calculate the average net change across the months
if len(net_change_list) > 0:
    average_change = sum(net_change_list) / len(net_change_list)
else:
    average_change = 0 # Handle case with no changes

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n"
    f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

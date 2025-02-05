# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import os # Incorporated the csv module to work with CSV files
import csv

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis_VHR.txt")  # Output file path

# Initialize variables to track election data
total_votes = 0 # Track the total number of votes cast
candidates = {} # Dictionary to track candidates and votes

# Winning candidates and winning count tracker
winner = ""
max_votes = 0

# Read the CSV file
with open(file_to_load, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:

        # Increment the total vote count for each row
        total_votes += 1
        candidate = row[2]  # Candidate name is in the third column

        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Prepare the election results
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")


# Loop through the candidates to determine vote percentages and identify the winner
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Determine the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Generate and print the winning candidate summary
results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Print to console
for line in results:
    print(line)
# Export, Write and save results to a text file of 
# the total vote count and winning candidate summary to the text file
with open(file_to_output, "w") as txt_file:
    for line in results:
        txt_file.write(line + "\n")




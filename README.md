# Python Challenge Module 3 (Week 3)
# python-challenge

Part 1 - PyBank 

The Challenge is to create a Python script to analyze the financial records of a company. A financial dataset called budget_data.csv is given. The dataset is composed of two columns: "Date" and "Profit/Losses".

The task is to create a Python script that analyzes the records to calculate the following values:

The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The changes in "Profit/Losses" over the entire period, and then the average of those changes
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in profits (date and amount) over the entire period
The script should also save and output the analysis results to terminal and txt file.]

PyBank Script explanation(main.py):

main.py is the python script to do our work. . The loop will calculate the profit and loss, it will load, read (and loop thorugh to calculate) and save an output text file with all the results.
List Variables were defined to keep count of the calculations done through the loop.
They tracked total months, total net amount of "Profit/Losses. and additional variables to hold list to store "Profit/Losses" between months, store month and value of greatest profit increase and store month and value of greatest loss decrease

Process each row of data
    
Track the total, track the net change, calculate the greatest increase in profits (month and amount), calculate the greatest decrease in losses (month and amount) and calculate the average net change across the months. Generate the output summary Print the output Write the results to a text file


Part 2 PyPoll

In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote

PyPoll Script Explanation (main.py):
Initialize variables to track rack the total number of votes cast, a dictionary of candidates and votes each recvieved. Read the CSV file and count votes for each candidate
Prepare the election results
Loop thorugh candidates and count the votes and determine the winner. Generate and print to console, export, write and save results to a text file of total vote count and winning candidate summary.


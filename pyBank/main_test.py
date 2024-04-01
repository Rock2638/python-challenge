# First import the os module to create file paths across operating sytems
import os

#import the module for reading the csv files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 

    #skip the header row
    next (csvreader)
    
    #count the total number of rows
    row_count = len(list(csvreader))

    # Reset the reader for the second iteration
    csvfile.seek(0)
    csvreader = csv.reader(csvfile, delimiter=',') 
    next (csvreader)

    #sum up the values in the second column (index 1)
    net_total = sum(int(row[1]) for row in csvreader)

    
print(f"The total number of months is: {row_count}")
print(f"The net total amount of Profit/Losses over the entire period: ${net_total}")

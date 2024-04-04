#First import the os module to create file paths across operating sytems
import os

#import the module for reading the csv files
import csv

#set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

#initialize variables to track the rows a
row_count = 0

#The column name to extract the names from
column_name = 2

#variable to track the name with the highest percentage and its percentage
highest_name = None
highest_percentage = 0

# Specify the file to write to
output_path = os.path.join("analysis", "pyPolloutputs.txt")

#open the csv
with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 

    #skip the header row
    next (csvreader)

    #Initialise a dictionary to hold the names and counts
    namelist = {}

    #for each row in the csv file after the header row
    for row in csvreader:
        #count the rows to obtain the total number of votes
        row_count = row_count+1

        #Extract the name from the current row and append it to the dictionary 
        name = (row[column_name])

        #check if name exists and if it does then increase the counter else set to 1
        if name in namelist:
            namelist[name] +=1
        else:
            namelist[name]=1

#Open the file using "write" mode. Specify the file variable to hold the contents
with open(output_path, 'w') as outfile:

    #print to terminal output and text file
    print("Election Results")
    print("Election Results", file=outfile)

    print("------------------------------")
    print("------------------------------", file=outfile)

    print(f"Total Votes: {row_count}")
    print(f"Total Votes: {row_count}", file=outfile )

    print("------------------------------")
    print("------------------------------", file=outfile)

    print(f"The candidates who received votes are: ")
    print(f"The candidates who received votes are:", file=outfile)

    #calculate the precentage of each candidate
    for name, count in namelist.items():
        percentage = (count/row_count) * 100

        #print each name with their percentage and total number of votes won to terminal output and text file
        print(f"{name}: {percentage:.3f}% ({count})") 
        print(f"{name}: {percentage:.3f}% ({count})", file=outfile) 

        #compare the current to the previous highest percentage
        if percentage>highest_percentage:
            highest_name = name
            highest_percentage = percentage


    #print to the terminal output and to the text file
    print("------------------------------")
    print("------------------------------", file=outfile)

    print(f"Winner: {highest_name}")
    print(f"Winner: {highest_name}", file=outfile)

    print("------------------------------")
    print("------------------------------", file=outfile)



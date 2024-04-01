# First import the os module to create file paths across operating sytems
import os

#import the module for reading the csv files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

row_count = 0
net_total= 0


with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 

    #skip the header row
    next (csvreader)
    
    profit_losslist = []

    for row in csvreader:
        row_count = row_count+1
        net_total = net_total + int(row[1])
        profit_losslist.append(int(row[1]))


profitloss_changes = [(profit_losslist[i+1] - profit_losslist[i]) for i in range(len(profit_losslist)-1)]

average_changes = round(sum(profitloss_changes)/(row_count-1),2)

print(f"The total number of months is: {row_count}")
print(f"The net total amount of Profit/Losses over the entire period: ${net_total}")

print(f"The average of profit/loss changes is: ${average_changes}")
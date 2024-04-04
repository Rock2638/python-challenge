#First import the os module to create file paths across operating sytems
import os

#import the module for reading the csv files
import csv

#set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')


#initialize variables to track the rows and the net total amount
row_count = 0
net_total= 0

#initialize variables to track the changes and the dates
greatest_increase = None
greatest_decrease = None
greatest_increase_date = ''
greatest_decrease_date = ''
change = None


#initialize variables to store the previous month's profit
prev_month_profit = None

#open the csv
with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 

    #skip the header row
    next (csvreader)
    
    #initialise variable to store the list of profit and loss
    profit_losslist = []

    #for each row in the csv file after the header row
    for row in csvreader:
        #count the rows to obtain the total number of months
        row_count = row_count+1

        #do a running total of the profits/losses in column 1
        net_total = net_total + int(row[1])

        #add profits/losses to a list needed to calculate the changes
        profit_losslist.append(int(row[1]))

        #store the content of colunm 0 in the date variable 
        date = row[0] 

        #store the content of colunm 1 in the profit variable 
        profit = int(row[1])
    
        #check for the previous profit/loss
        if prev_month_profit is not None:
            # Calculate the change from the previous month if the previous month has a value
            change = profit - prev_month_profit
            

        #Update the greatest change and date if this month's change is greater
        if greatest_increase is None or change > greatest_increase:
            #the change will become the new greatest increase if it is bigger than the previous greatest increase
            greatest_increase = change
            #pick up the date corresponding to the new greatest increase
            greatest_increase_date = date
            

        # Update the tracking variables if this is the greatest decrease
        if greatest_decrease is None or change < greatest_decrease:
            #the change will become the new greatest decrease if it is smaller than the previous greatest decrease
            greatest_decrease = change
            #pick up the date corresponding to the new greatest decrease
            greatest_decrease_date = date

            
        #Update the previous month's profit for the next iteration
        prev_month_profit = profit

#Finding difference between the current profit/loss value and previous profitloss value using all values in list created
profitloss_changes = [(profit_losslist[i+1] - profit_losslist[i]) for i in range(len(profit_losslist)-1)]

#adding the changes then diving by number of months and rounding the answer to two decimal places
average_changes = round(sum(profitloss_changes)/(row_count-1),2)

print("Financial Analysis")
print("------------------------------")

print(f"The total number of months is: {row_count}")
print(f"The net total amount of Profit/Losses over the entire period: ${net_total}")

print(f"The average of profit/loss changes is: ${average_changes}")
print(f"The greatest increase in Profits was in {greatest_increase_date} with an amount of ${greatest_increase}.")
print(f"The greatest decrease in profits was in {greatest_decrease_date} with an amount of ${greatest_decrease}.")


# Specify the file to write to
output_path = os.path.join("analysis", "pyBankoutputs.txt")

# Open the file using "write" mode. Specify the file variable to hold the contents
with open(output_path, 'w') as outfile:

    #output the results onto the textfile
    outfile.write("Financial Analysis"+'\n')
    outfile.write("------------------------------"+'\n')
    outfile.write("Total months: "+ str(row_count)+'\n')
    outfile.write("Total : $"+ str(net_total)+'\n')
    outfile.write("Average change : $"+ str(average_changes)+'\n')
    outfile.write("Greatest increase in profits: "+ greatest_increase_date + " ($" + str(greatest_increase) + ")"+'\n')
    outfile.write("Greatest decrease in profits: "+ greatest_decrease_date + " ($" + str(greatest_decrease) + ")"+'\n')

print("------------------------------")
print("Financial analysis outputs printed to text file as required: "+ output_path )
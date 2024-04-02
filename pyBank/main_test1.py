# First import the os module to create file paths across operating sytems
import os

#import the module for reading the csv files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

# Initialize variables to track the rows and the net total amount
row_count = 0
net_total= 0

# Initialize variables to track the chances and its date
greatest_increase = None
greatest_decrease = None
greatest_increase_date = ''
change = 0


# Initialize variables to store the previous month's profit
prev_month_profit = None


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

        date = row[0] 
        profit = int(row[1])
    
        
        if prev_month_profit is not None:
            # Calculate the change from the previous month
            change = profit - prev_month_profit
            

    # Update the greatest change and date if this month's change is greater
        if greatest_increase is None or change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = date
            

    # Update the tracking variables if this is the greatest decrease
        if greatest_decrease is None or change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = date

            
    #Update the previous month's profit for the next iteration
        prev_month_profit = profit


profitloss_changes = [(profit_losslist[i+1] - profit_losslist[i]) for i in range(len(profit_losslist)-1)]
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

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as outfile:

    outfile.write("Financial Analysis"+'\n')
    outfile.write("------------------------------"+'\n')
    outfile.write("Total months: "+ str(row_count)+'\n')
    outfile.write("Total : $"+ str(net_total)+'\n')
    outfile.write("Average change : $"+ str(average_changes)+'\n')
    outfile.write("Greatest increase in profits: "+ greatest_increase_date + " ($" + str(greatest_increase) + ")"+'\n')
    outfile.write("Greatest decrease in profits: "+ greatest_decrease_date + " ($" + str(greatest_decrease) + ")"+'\n')


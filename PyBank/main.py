#PyBank


# Instrucions: 

#Your task is to create a Python script that analyzes the records to calculate each of the following values:

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period


#First, import the necessary modules
import os
import csv

#Create empty lists to store the data
months = []
profit_losses = []
change_profit_losses = []
change_data = []
previous_revenue = 0
headers = []
change_int = []

#create path to the file
budget_path = os.path.join("Resources", "budget_data.csv")

#open the csv file
with open(budget_path) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')
         # loop to iterate through the rows of csv
    for row in budget_reader:
 
        # adding the header row
        headers.append(row)
 
        # breaking the loop after the first iteration
        break

    #add columns to created lists
    for row in budget_reader:
        #Add dates to months list
        months.append(row[0])
        #Add profits and losses to list
        profit_losses.append(int(row[1]))
    #find changes in  profits and losses, add to changes list
        revenue = int(row[1])
        change_profit_losses.append([row[0], revenue - previous_revenue])
        change_int.append(revenue-previous_revenue)
        previous_revenue = revenue
    
#find total number of months included in the dataset
total_months = len(months)

#find the total sum of profits and losses over the dataset
total_profit_losses = sum(profit_losses)

#Eliminate the first value in our change lists, which are not really changes but the starting values. 
change_profit_losses.pop(0)
change_int.pop(0)

#find maximum profits value
max_profit_int = max(change_int)
#find maximum losses value
max_loss_int = min(change_int)
#find the average change of profit and losses over the dataset
average_change = (sum(change_int))/(len(change_int))
#round the average
round_average = round(average_change, 2)

#get date with value of maximum profits and losses
max_profit = change_profit_losses[change_int.index(max_profit_int)]
max_loss = change_profit_losses[change_int.index(max_loss_int)]

#print results
print()
print("Financial Analysis")
print()
print("----------------------------")
print()
print(f"Total Months: {total_months}")
print()
print(f"Total: ${total_profit_losses}")
print()
print(f"Average Change: ${round_average}")
print()
print(f"Greatest Increase in Profits: {max_profit[0]} (${max_profit[1]})")
print()
print(f"Greatest Decrease in Profits: {max_loss[0]} (${max_loss[1]})")
print()


#write results to text file
text_path = os.path.join("analysis", "pybank_analysis.txt")
with open(text_path, "w") as f:
    f.write("Financial Analysis \n")
    f.write("\n")
    f.write("----------------------------\n")
    f.write("\n")
    f.write(f"Total Months: {total_months}\n")
    f.write("\n")
    f.write(f"Total: ${total_profit_losses}\n")
    f.write("\n")
    f.write(f"Average Change: ${round_average}\n")
    f.write("\n")
    f.write(f"Greatest Increase in Profits: {max_profit[0]} (${max_profit[1]})\n")
    f.write("\n")
    f.write(f"Greatest Decrease in Profits: {max_loss[0]} (${max_loss[1]})\n")
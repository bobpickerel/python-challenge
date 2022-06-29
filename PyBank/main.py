# import os module that allows for us to use file pathing
from importlib import resources
import os
#import the csv module that will allow for us to handle .csv file
import csv

# create a path to the csv file
# use os.path.join() to create a path as well
filePath = os.path.join("Resources", "budget_data.csv")

# zero out variables
totalProfit = 0
monthCounter = 0
maxChange = 0
maxChangeMonth = ""
negChange = 0
negChangeMonth = ""
prevValue = 0
currentChange = 0
monthlyChanges = []


# open the file using the file path above
with open(filePath, 'r') as file:

    csvReader = csv.reader(file, delimiter=',')

    # read the header row
    header = next(csvReader)
    
    # identify first row of data after header
    firstRow = next(csvReader)
    
    # mounthCounter for first row
    monthCounter += 1

    # totalProfit for first row
    totalProfit = totalProfit + float(firstRow[1])

    # set prevValue for first row
    prevValue = float(firstRow[1])

    # set firstRow as max and min
    maxChange = float(firstRow[1])
    maxChangeMonth = firstRow[0]
    negChange = float(firstRow[1])
    negChangeMonth = firstRow[0]   

    #read the remaining rows in the csv file
    for row in csvReader:
                
        # increase the counter for number of months
        monthCounter += 1

        # add total profit to existing profit
        totalProfit = totalProfit + float(row[1])

        # identify change from previous value
        currentChange = float(row[1]) - prevValue
        
        # add this change to the list of all changes
        monthlyChanges.append(currentChange)
        
        #reset previous value for the next time through the loop
        prevValue = float(row[1])
                       
        # test to see if the change is great then or less then previous changes
        if float(row[1]) > maxChange:
            maxChange = float(row[1])
            maxChangeMonth = row[0]
        elif float(row[1]) < negChange:
            negChange = float(row[1])
            negChangeMonth = row[0]

# calculate the average change by summing all changes and dividing by length of list

avgChange = sum(monthlyChanges)/ len(monthlyChanges)

# Print results to terminal
print("\nFinancial Analysis\n---------------------------------------------------")
print(f"Total Months: \t\t\t{monthCounter}")
print(f"Total: \t\t\t\t${totalProfit:,.2f}")
print(f"Average Change: \t\t${avgChange:,.2f}")
print(f"Greatest Increase in Profits: \t{maxChangeMonth} ${maxChange:,.2f}")
print(f"Greatest Decrease in Profits: \t{negChangeMonth} ${negChange:,.2f}")
print("---------------------------------------------------\n")


# Print results to file
# Specify the file to write to
output_path = os.path.join("financial_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    # Write text to the text file
    txtfile.write("Financial Analysis\n---------------------------------------------------\n")
    txtfile.write(f"Total Months: \t\t\t\t\t{monthCounter}\n")
    txtfile.write(f"Total: \t\t\t\t\t\t${totalProfit:,.2f}\n")
    txtfile.write(f"Average Change: \t\t\t\t${avgChange:,.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: \t{maxChangeMonth} ${maxChange:,.2f}\n")
    txtfile.write(f"Greatest Decrease in Profits: \t{negChangeMonth} ${negChange:,.2f}\n")



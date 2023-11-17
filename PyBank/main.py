#Imports the necessary libraries
import os
import csv
from pathlib import Path
import numpy as np

#Declare our paths for the read and write files
csv_path = Path(r"PyBank\Resources\budget_data.csv")
Financial_Analysis = Path(r"PyBank\analysis\Financial Analysis")

#Reads our .csv file of our budget data
with open(csv_path, 'r' ) as csvfile:

    budget_data = csv.reader(csvfile, delimiter = ',')

    header_row = next(budget_data)

    #Declaring variables
    month_count = 0
    net_total = 0

    prev_row = 0
    greatest_increase = 0
    greatest_decrease = 0
    date_great = ""
    date_not = ""
    change = 0
    total_change = 0

    #loops through data
    for row in budget_data:
        change = int(row[1]) - prev_row
        total_change += change
  
        month_count += 1
        net_total += int(row[1])
        prev_row = int(row[1])  
 

        if  change > greatest_increase:
            greatest_increase = change
            date_great = row[0]
        
        elif change < greatest_decrease:
            greatest_decrease = change
            date_not = row[0]
    
    average_change = round(total_change/month_count)

    output = ["Financial Analysis\n" + #list of output text for the Election_Result.txt
    "\n-------------------------------------\n " +
    f"\nTotal Months: {month_count}\n" +
    f"\nTotal: ${net_total}\n" +  
    f"\nAverage Change: ${average_change}\n"+
    f"\nGreatest Increase in Profits: {date_great} (${greatest_increase})\n" +
    f"\nGreatest Decrease in Profits: {date_not} (${greatest_decrease})"]


    print("Financial Analysis\n" + #print statement of the Election_Result.txt
    "\n-------------------------------------\n " +
    f"\nTotal Months: {month_count}\n" +
    f"\nTotal: ${net_total}\n" +  
    f"\nAverage Change: ${average_change}\n" +
    f"\nGreatest Increase in Profits: {date_great} (${greatest_increase})\n" +
    f"\nGreatest Decrease in Profits: {date_not} (${greatest_decrease})")    

#Writes the output to a .txt file
with open(Financial_Analysis, 'w') as csvfile:

    writer = csv.writer(csvfile, delimiter = ',')

    writer.writerow(output)
import os
import csv

from numpy import average

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

date = []
profit = []
change_list = []
change = 0
total_profit = 0
greatest_inc = ['', 0]
greatest_dec = ['', 9999999999999999999]


with open(csvpath, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #header
    csv_header = next(csvreader)
    #first row
    first_row = next(csvreader)


    #change += int(first_row[1])
    prev_row = int(first_row[1])
    
    for row in csvreader:

        date.append(row[0])
        profit.append(row[1])

        #Calculate sum of profits
        row1 = int(row[1])
        total_profit += row1 

        #calculate change
        change = int(row[1]) - prev_row
        prev_row = int(row[1])
        change_list += [change]

        if change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = change 

        if change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = change


    average_change = sum(change_list) / len(change_list)
    
    export = list(zip(date, profit))
    #print(export[1])

    #Calculating count of months
    total_months = 0

    for row in export:
        total_months += 1
    

    #Summary Table
    results = (
    f'Financial Analysis\n'
    f'--------------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${total_profit}\n'
    f'Average Change: ${round(average_change, 2)}\n'
    f'Greatest Increase in Profits: {greatest_inc}\n'
    f'Greatest Decrease in Profits: {greatest_dec}')

    print(results)

export_file = os.path.join("..", "solution", "HW3_results.txt")
with open (export_file, 'w') as txt_file:
    txt_file.write(results)

        

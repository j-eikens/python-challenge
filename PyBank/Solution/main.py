import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

date = []
profit = []
change_list = []
change = 0
total_profit = 0
#first_row = []
average_change = 0


with open(csvpath, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    #first row
    first_row = next(csvreader)
    #change += int(first_row[1])
    prev_row = int(first_row[1])
    print(first_row)
    
    for row in csvreader:

        date.append(row[0])
        profit.append(row[1])

        #Calculate sum of profits
        sum = int(row[1])
        total_profit = sum + total_profit

        #calculate change
        change = int(row[1])- prev_row
        change_list = sum(change)

        print(change_list)

        #calculate average change
        # average_change += change / len(row)
        # print(average_change)


        
    

    export = list(zip(date, profit))
    #print(export[1])
 

    for row in change_list:
        print(row)

    #Calculating count of months
    total_months = 0

    for row in export:
        total_months += 1
    

    #Summary Table
    print('Financial Analysis')
    print('--------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_profit}')

        

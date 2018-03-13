#import
import csv
import os

# prints results for the dataset
def printResults():
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ', total_months)
    print('Total Revenue: $', total_revenue)
    print('Average Revenue Change: $', round(abs(total_revenue_change) / (len(rowsArray) - 1), 2))
    print('Greatest Increase in Revenue: ', greatest_increase_month +  ' ($' + str (greatest_increase) + ')')
    print('Greatest Decrease in Revenue: ', greatest_decrease_month +  ' ($-' + str (greatest_decrease) + ')')

#outputting results to a text file called Financial Analysis
def writeResults():
    output_file = "Financial_Analysis.txt"

    #open the output file
    file = open(output_file, 'w')

    #writing the rows to print in text file
    file.write('Financial Analysis\n')
    file.write('----------------------------\n')
    file.write('Total_Months: ' + str(total_months) + '\n')
    file.write('Total_Revenue: ' + str(total_revenue) + '\n')
    file.write('Average Revenue Change: $ ' + str(round(abs(total_revenue_change) / (len(rowsArray) - 1), 2)) + '\n')
    file.write('Greatest Increase in Revenue: ' + str(greatest_increase_month +  ' ($' + str (greatest_increase) + ')') + '\n')
    file.write('Greatest Decrease in Revenue: ' + str(greatest_decrease_month +  ' ($-' + str (greatest_decrease) + ')') + '\n')

total_months = 0
total_revenue = 0
greatest_increase = 0
greatest_increase_month = ''
greatest_decrease = 0
greatest_decrease_month = ''
total_revenue_change = 0

#file to open
csvpath = os.path.join('raw_data', 'budget_data_1.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # converts csvreader to array
    rowsArray = list(csvreader)

    #  for every row in a dataset
    for i in range(1, len(rowsArray)):
        # add 1 to total_months
        total_months = total_months + 1

        # add the revenue in each row to the total_revenue
        total_revenue = total_revenue + int(rowsArray[i][1])

        # calculate whether current row is max
        max_length_not_reached = i != len(rowsArray) - 1

        if max_length_not_reached:
            total_revenue_change = total_revenue_change + int(rowsArray[i + 1][1]) - int(rowsArray[i][1])

            # increase
            if (greatest_increase < int(rowsArray[i + 1][1]) - int(rowsArray[i][1])):
                greatest_increase = int(rowsArray[i + 1][1]) - int(rowsArray[i][1])
                greatest_increase_month = rowsArray[i + 1][0]

            # decrease
            if (greatest_decrease < int(rowsArray[i][1]) - int(rowsArray[i + 1][1])):
                greatest_decrease = int(rowsArray[i + 1][1]) - int(rowsArray[i][1])
                greatest_decrease_month = rowsArray[i][0]


printResults()
writeResults()

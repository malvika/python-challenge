# Your task is to create a Python script that analyzes the records to calculate each of the following:
#
# * The total number of months included in the dataset
#
# * The total amount of revenue gained over the entire period
#
# * The average change in revenue between months over the entire period
#
# * The greatest increase in revenue (date and amount) over the entire period
#
# * The greatest decrease in revenue (date and amount) over the entire period
#
# As an example, your analysis should look similar to the one below:
#
# ```
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)
# ```

# Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# * The total number of months included in the dataset
import csv
import os

# prints results for the dataset
def printResults():
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ', total_months)
    print('Total Revenue: $', total_revenue)
    print('Greatest Increase in Revenue: $', greatest_increase)


csvpath = os.path.join('raw_data', 'budget_data_1.csv')

total_months = 0
total_revenue = 0
greatest_increase = 0

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

        if (i != len(rowsArray) - 1 and greatest_increase < int(rowsArray[i + 1][1]) - int(rowsArray[i][1])):
            greatest_increase = int(rowsArray[i + 1][1]) - int(rowsArray[i][1])


printResults()

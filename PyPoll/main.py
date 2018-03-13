
import csv
import os

#outputting results to a text file called Poll results
output_file = "Poll_Results.txt"
   #open the output file
file = open(output_file, 'w')

candidates = []
all_votes = []

def printResults():
    winner_count = 0
    total_votes = len(rowsArray) - 1

    print('Election Results')
    print('----------------------------')
    print('Total Votes: ', total_votes)
    print('----------------------------')
    file.write('Election Results\n')
    file.write('----------------------------\n')


    for can in candidates:
        candidate_count = all_votes.count(can)
        print(can + ': ' + str( round((candidate_count / total_votes) * 100, 1) ) + '% (' + str(candidate_count) + ')')
        file.write(can + ': '  + str( round((candidate_count / total_votes) * 100, 1) ) + '% (' + str(candidate_count) + ')' + '\n')

        if candidate_count > winner_count:
            winner_count = candidate_count
            winner = can

    print('----------------------------')
    print('Winner : ' + winner)
    print('----------------------------')    
    file.write("Total Votes: " + str(total_votes) + '\n')
    file.write('----------------------------\n')
    file.write('Winner : ' + winner + '\n')
    file.write('----------------------------\n')


csvpath = os.path.join('raw_data', 'election_data_1.csv')
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # converts csvreader to array
    rowsArray = list(csvreader)

    # A complete list of candidates who received votes: get the list of voters in col 3, position 2
    # Print the contents of each row
    for i in range(1, len(rowsArray)):
        # if candidate no in candidates array
        if rowsArray[i][2] not in candidates:
            # add candidate to candidates array
            candidates.append(rowsArray[i][2])

        # add each candidate to all_votes array
        all_votes.append(rowsArray[i][2])

printResults()

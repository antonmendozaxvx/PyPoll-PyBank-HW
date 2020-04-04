#PyPoll
import os
import csv

# set csv file path for data
poll_csv = os.path.join('PyPoll', 'election_data.csv')

#define function
def get_results(data):

    # define variables
    vote_count = 0
    votes = []
    candidate_count = []
    uniqueCandidates = []
    percent = []

    #start loop
    for row in data:

        #total number of votes
        vote_count +=1

        #append names to the candidates list
        if row[2] not in uniqueCandidates:
            uniqueCandidates.append(row[2])

        #make a list of all votes
        votes.append(row[2])

    # start a loop to populate the candidate count with each vote
    for candidate in uniqueCandidates:
        candidate_count.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/vote_count*100,3))

    #fine winner using index positioning of the max count in candidate_count
    winner = uniqueCandidates[candidate_count.index(max(candidate_count))]

    #print results, use a loop for the number of unique candidates
    print('Election Results')
    print('------------------------')
    print(f'Total Votes: {vote_count}')
    print('------------------------')
    for i in range(len(uniqueCandidates)):
        print(f'{uniqueCandidates[i]}: {percent[i]}% {candidate_count[i]}')
    print('------------------------')
    print(f'Winner: {winner}')
    print('------------------------')

    #set exit path
    poll_output = os.path.join("PyPollResults.txt")

    #write out results to text file
    with open(poll_output, "w'") as txtfile:
        txtfile.write('Election Results')
        txtfile.write('\n------------------------')
        txtfile.write(f'\nTotal Votes: {vote_count}')
        txtfile.write('\n------------------------')
        for i in range (len(uniqueCandidates)):
            txtfile.write(f'\n{uniqueCandidates[i]}: {percent[i]}% {candidate_count[i]}')
        txtfile.write('\n------------------------')
        txtfile.write(f'\nWinner" {winner}')
        txtfile.write('\n------------------------')


#read in the CSV file
with open(poll_csv, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #adjust for header
    csv_header = next(csvfile)

    #use function
    get_results(csvreader)
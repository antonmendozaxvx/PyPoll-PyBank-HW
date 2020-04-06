import os
import csv

# set path for data
poll_csv = os.path.join('election_data.csv')

# function
def get_results(data):

    # define variables
    totalVotesCount = 0
    votes = []
    candidateCount = []
    Candidates = []
    percent = []
     
    # start loop
    for row in data:

        # total number of votes
        totalVotesCount += 1

        # candidates
        if row[2] not in Candidates:
            Candidates.append(row[2])

        # make a list of all the votes
        votes.append(row[2])

    # count the number of votes each candidate won
    for candidate in Candidates:
        candidateCount.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/totalVotesCount*100,3))

    # calculate winner
    winner = Candidates[candidateCount.index(max(candidateCount))]
    
    # print results
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {totalVotesCount}')
    print('--------------------------------')
    for i in range(len(Candidates)):
        print(f'{Candidates[i]}: {percent[i]}% {candidateCount[i]}')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')

    # set exit path
    poll_output = os.path.join("PyPollResults.txt")

    # write results as a text file
    with open(poll_output, "w") as txtfile:
        txtfile.write('Election Results')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Votes: {totalVotesCount}')
        txtfile.write('\n------------------------------------')
        for i in range (len(Candidates)):
            txtfile.write(f'\n{Candidates[i]}: {percent[i]}% {candidateCount[i]}')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nWinner: {winner}')
        txtfile.write('\n------------------------------------')


with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # adjust for header
    csv_header = next(csvfile)
    
    # use function
    get_results(csvreader)

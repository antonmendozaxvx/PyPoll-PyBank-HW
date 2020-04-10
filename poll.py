import os
import csv

poll_csv = os.path.join('election_data.csv')

with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    get_results(csvreader)


    # define variables
    total_votes = 0
    votes = []
    candidate_count = []
    Candidates = []
    percent = []
     
    # start loop
    for row in data:

        # total number of votes
        total_votes += 1

        # candidates
        if row[2] not in Candidates:
            Candidates.append(row[2])

        # make a list of all the votes
        votes.append(row[2])

    # count the number of votes each candidate won
    for candidate in Candidates:
        candidateCount.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/total_votes*100,3))

    # calculate winner
    winner = Candidates[candidate_count.index(max(candidate_count))]
    
    # print results
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {total_votes}')
    print('--------------------------------')
    for i in range(len(Candidates)):
        print(f'{Candidates[i]}: {percent[i]}% {candidate_count[i]}')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')

    # set exit path
    poll_output = os.path.join("PyPollResults.txt")

    # write results
    with open(poll_output, "w") as txtfile:
        txtfile.write('Election Results')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Votes: {total_votes}')
        txtfile.write('\n------------------------------------')
        for i in range (len(Candidates)):
            txtfile.write(f'\n{Candidates[i]}: {percent[i]}% {candidate_count[i]}')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nWinner: {winner}')
        txtfile.write('\n------------------------------------')

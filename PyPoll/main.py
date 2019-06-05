import os
import csv
csvpath = os.path.join('PyPoll/election_data.csv')

with open(csvpath, newline='') as csvfile:

    #split data into columns
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    header = next(csvreader)
    #print(f"CSV Header: {header}")

    count = 0 
    canidate_1 = "Khan"
    canidate_2 = "Correy"
    canidate_3 = "Li"
    canidate_4 = "O'Tooley"

    vote_1 = 0
    vote_2 = 0
    vote_3 = 0
    vote_4 = 0

    for row in csvreader:
        count = count + 1

        if canidate_1 == row[2]:
            vote_1 = vote_1 + 1
        elif canidate_2 == row[2]:
            vote_2 = vote_2 + 1
        elif canidate_3 == row[2]:
            vote_3 = vote_3 + 1
        elif canidate_4 == row[2]:
            vote_4 = vote_4 + 1

     
    percent_1 = round(vote_1/count,2)*100
    percent_2 = round(vote_2/count,2)*100
    percent_3 = round(vote_3/count,2)*100
    percent_4 = round(vote_4/count,2)*100
    
    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: ({count})")
    print("---------------------------")
    print(f"Khan: {percent_1}%  ({vote_1})")
    print(f"Correy: {percent_2}%  ({vote_2})")
    print(f"Li: {percent_3}%  ({vote_3})")
    print(f"O'Tooley: {percent_4}%  ({vote_4})")
    print("---------------------------")
    print(f"Winner: ")

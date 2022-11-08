import os 

import csv

candidates = []
unique = []

csvPyPollpath = os.path.join('PyPoll','Resources','election_data.csv')
with open(csvPyPollpath) as csvPyPollfile:
    csvreader = csv.reader(csvPyPollfile, delimiter=',')
    # skip first row/header row
    next(csvreader)
    
    #list of all condidates from column 0
    candidates = [x[2] for x in csvreader]
    #total number of votes = total number of data points/row minus header
    num_of_votes = len(candidates)
    
    #find unique list of candidates
    unique_list = []
    for x in candidates:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)

    #total votes for all the unique cadidates
    unique_total_votes = []
    unique_total_votes = [candidates.count(x) for x in unique_list]

    #percent of each vote
    percent_list = [(x / num_of_votes)*100 for x in unique_total_votes]
    percent_list = [round(x,3) for x in percent_list]


    #index max number of votes
    max_value = max(unique_total_votes)
    indexmax = unique_total_votes.index(max_value)
    #use index to list winner   
    winner = unique_list[indexmax]

           
#print(num_of_votes)
#print(unique_list)
#print(unique_total_votes)
#print(winner)
#print(percent_list)



print(' Election Results \n -------------------------- \n Total Votes: {} \n ------------------------- \n {}: {}% ({}) \n {}: {}% ({}) \n {}: {}% ({}) \n Winner: {} \n -------------------------'.format(num_of_votes,unique_list[0],percent_list[0],unique_total_votes[0],unique_list[1],percent_list[1],unique_total_votes[1],unique_list[2],percent_list[2],unique_total_votes[2],winner))

#TODO: WRITE CSV TO FILE

# import os module that allows for us to use file pathing
from importlib import resources
import os
#import the csv module that will allow for us to handle .csv file
import csv

# create a path to the csv file
# use os.path.join() to create a path as well
filePath = os.path.join("Resources", "election_data.csv")

# Zero out Variables
totalVotes = 0
voteStockham = 0
voteDeGette = 0
voteDoane = 0
winnerElection = ""
candidateList = []
voteCount = {}
voteOutput = ""

# open the file using the file path above
with open(filePath, 'r') as file:

    csvReader = csv.reader(file, delimiter=',')

    # read the header row 
    header = next(csvReader)
    
    # read the remaining rows in the csv file
    for row in csvReader:
                
        # increase the counter for number of months
        totalVotes += 1

        # test to determine all candidates
        if row[2] not in candidateList:
            # add to candiateList
            candidateList.append(row[2])
            # add to the voteCount
            voteCount[row[2]] = 1
        else:
            # if candidates already in the list then add to the vote count
            voteCount[row[2]] += 1
            
# determine total votes per candidate 
# voteCount is dictionary containing key: candidate value: # of votes
for candidate in voteCount:
    # votes is number of votes per candidate
    votes = voteCount.get(candidate)
    # votePct is the percenatage of votes per candidate
    votePct = (float(votes)/float(totalVotes)) * 100

    # create output state for each candidate including name, percentage of votes and total votes
    # test length of candidate name to apply tabs to line up output
    if len(candidate) > 20:
        voteOutput += f"{candidate}:\t{votePct:.2f}%\t({votes:,})\n"
    elif len(candidate) > 15:
        voteOutput += f"{candidate}:\t\t{votePct:.2f}%\t({votes:,})\n"
    else:
        voteOutput += f"{candidate}:\t\t\t{votePct:.2f}%\t({votes:,})\n"

# test voteCount dictionary to determine which candidate had the highest vote count
winnerElection = max(voteCount, key=voteCount.get)


# print results to the terminal
print("\nElection Results\n---------------------------------------------------")
print(f"Total Votes: \t\t\t\t{totalVotes:,}")
print("---------------------------------------------------")
print(voteOutput)
print("---------------------------------------------------\n")
print(f"Winner:  {winnerElection}")
print("---------------------------------------------------\n")

# Print results to file
# Specify the file to write to
output_path = os.path.join("poll_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    # Write text to the textfile
    txtfile.write("\nElection Results\n---------------------------------------------------\n")
    txtfile.write(f"Total Votes: \t\t\t\t{totalVotes:,}\n")
    txtfile.write("---------------------------------------------------\n")
    txtfile.write(voteOutput)
    txtfile.write("---------------------------------------------------\n")
    txtfile.write(f"Winner:  {winnerElection}\n")
    txtfile.write("---------------------------------------------------\n")

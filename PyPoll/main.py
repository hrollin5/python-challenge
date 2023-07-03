#Pypoll

# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following values:

    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote


#first, import the necessary modules
import os
import csv

#make empty list for votes
votes = []
headers = []
candidates = []

#create path for vote file
vote_path = os.path.join("Resources", "election_data.csv")

#open the vote file
with open(vote_path) as csvfile:
    vote_reader = csv.reader(csvfile, delimiter=",")

        # loop to iterate through the rows of csv
    for row in vote_reader:
 
        # adding the header row
        headers.append(row)
 
        # breaking the loop after the first iteration
        break

    #add votes to the empty list
    for row in vote_reader:
        votes.append(row[2])

#get a list of candidates
for i in votes:
    if i not in candidates:
        candidates.append(i)
#create a variable for each candidate
candidate_1 = candidates[0]
candidate_2 = candidates[1]
candidate_3 = candidates[2]

#count total number of votes
total_votes = len(votes)

#calculate votes and percentage of votes for each candidate
    #candidate 1
candidate_1_votes = votes.count(candidate_1)
candidate_1_percent = round(((candidate_1_votes / total_votes) * 100), 3)

    #candidate 2
candidate_2_votes = votes.count(candidate_2)
candidate_2_percent = round(((candidate_2_votes / total_votes) * 100), 3)

    #candidate 3
candidate_3_votes = votes.count(candidate_3)
candidate_3_percent = round(((candidate_3_votes / total_votes) * 100), 3)

#determine the winner
if candidate_1_percent > candidate_2_percent and candidate_1_percent > candidate_3_percent:
    winner = candidate_1
elif candidate_2_percent > candidate_3_percent and candidate_2_percent > candidate_1_percent:
    winner = candidate_2
else:
    winner = candidate_3

#print results
print()
print("Election Results")
print()
print("-------------------------")
print()
print(f"Total Votes: {total_votes}")
print()
print("-------------------------")
print()
print(f"{candidate_1}: {candidate_1_percent}% ({candidate_1_votes})")
print()
print(f"{candidate_2}: {candidate_2_percent}% ({candidate_2_votes})")
print()
print(f"{candidate_3}: {candidate_3_percent}% ({candidate_3_votes})")
print()
print("-------------------------")
print()
print(f"Winner: {winner}")
print()
print("-------------------------")

#write results to a text file
text_path = os.path.join("analysis", "pypoll_analysis.txt")
with open(text_path, "w") as f:
    f.write("Election Results\n")
    f.write("\n")
    f.write("-------------------------\n")
    f.write("\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("\n")
    f.write("-------------------------\n")
    f.write("\n")
    f.write(f"{candidate_1}: {candidate_1_percent}% ({candidate_1_votes})\n")
    f.write("\n")
    f.write(f"{candidate_2}: {candidate_2_percent}% ({candidate_2_votes})\n")
    f.write("\n")
    f.write(f"{candidate_3}: {candidate_3_percent}% ({candidate_3_votes})\n")
    f.write("\n")
    f.write("-------------------------\n")
    f.write("\n")
    f.write(f"Winner: {winner}\n")
    f.write("\n")
    f.write("-------------------------")




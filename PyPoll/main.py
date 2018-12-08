# Dependencies
import csv
import os
import pandas as pd

election_data = os.path.join("Resources/election_data.csv")

candidates = []
total_votes = 0
vote_count = []
percent_votes = []


with open(election_data) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        total_votes = total_votes + 1
        total_candidates = row["Candidate"]        

#Add candidates name to list, if not in the list, and add votes. 

        if row["Candidate"] not in candidates:
            
            candidates.append(row["Candidate"])
            index = candidates.index(row["Candidate"])
            vote_count.append(1)

#If the name exists in the list, add votes to that person's name.
        else:
            index = candidates.index(row["Candidate"])
            vote_count[index] +=1

#Determine the % vote for each Candidate on the list
    for votes in vote_count:
        percentage = (votes/total_votes)
        percentage = "{:.1%}".format(percentage)
        percent_votes.append(percentage)

#print(candidates)
#print(vote_count)
#print(percent_votes)

#Find the winner
candidate_df = {"Candidate_names": candidates,"Votes Per Candidate":vote_count}
candidate_df2=pd.DataFrame(candidate_df)
candidate_df3 = candidate_df2.sort_values("Votes Per Candidate", ascending = False)
winner = candidate_df3.head(1)

#Print
#Print Financial Analysis info
print("Election Results")
print("---------------------")
print(f"Total Votes: {str(total_votes)}")
print("---------------------")
line1 = "Election Results"
line2 = "---------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = "---------------------"
line5 = ""
for x in range (4):
    print(f"{str(candidates[x])}: {str(percent_votes[x])} ({str((vote_count[x]))})")
    line5 += str(f"{str(candidates[x])}: {str(percent_votes[x])} ({str((vote_count[x]))})\n")
line6 = "---------------------"
line7 = str(f"Winner: {winner['Candidate_names'].values}")

output = open("output.txt", "w")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

print("---------------------")
#print(f"Winner: {str(winner)}")
print(f"Winner: {winner['Candidate_names'].values}")
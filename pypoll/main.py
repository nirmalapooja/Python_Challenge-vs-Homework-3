# Import the files of election_data.csv from the main folder
import os
import csv
# create an object to link up to csv file to  be read 
poll_data = os.path.join('Resources','election_data.csv')
# lists to store data
candidates = []
num_of_votes = []
percent_vts_won = []
# to count total votes
total_votes = 0
# with open statement to read the imported data as csv file
with open(poll_data, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# next option helps to skip the header and read the values from the next line
    csv_header = next(csvreader)
# loop through the data
    for row in csvreader:
# adding to the total vote counter
        total_votes += 1
#by using not in condition a vote will added if the person is in the list,
# if not both name and a vote will added
        if row[2] not in candidates :
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_of_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_of_votes [index] += 1

# find the percentage of votes won and append to percent_vts_won list
for votes in num_of_votes:

        percentage = (votes/total_votes)* 100
        percentage = "%.3f%%" % percentage
        percent_vts_won.append(percentage)


# find the winning canididate
winner = max(num_of_votes)
index = num_of_votes.index(winner)
winner_candidate = candidates[index]

# finally print the results
print("Election Results")
print('----------------------------')
print(f"Total votes : {str(total_votes)}")
print("----------------------------")
for i in range(len(candidates)):
        print(f"{candidates[i]} : {str(percent_vts_won[i])} ({str(num_of_votes[i])})")
print('----------------------------')
print(f"Winner : {winner_candidate}")
print('----------------------------')

# Exporting the files to .txt file
txtoutput = open("txtoutput.txt", "w")
line1 = "Election Results"
line2 = "------------------------------"
line3 = str(f"Total Votes : {str(total_votes)}")
line4 = "------------------------------"
txtoutput.write('{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]} : {str(percent_vts_won[i])} ({str(num_of_votes[i])})")
    txtoutput.write('{}\n'.format(line))
line5 = "------------------------------"
line6 = str(f"Winner : {winner_candidate}")
line7 = "------------------------------"
txtoutput.write('{}\n{}\n{}\n'.format(line5,line6,line7))
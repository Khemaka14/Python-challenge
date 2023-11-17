#Imports the necessary libraries
import os
import csv
from pathlib import Path

#Declare our paths for the read and write files
csv_path = Path(r"PyPoll\Resources\election_data.csv")
Election_Results = Path(r"PyPoll\analysis\Election Results")

#Reads our .csv file of our budget data
with open(csv_path, 'r' ) as csvfile:

    election_data = csv.reader(csvfile, delimiter = ',')

    header_row = next(election_data)

    #Declaring variables
    vote_count = 0    
    Charles = 0
    Diana = 0
    Raymon = 0
    winner = ""
    most_votes = 0

    #loops through data and tallies the votes
    for row in election_data:
        vote_count += 1
        if row[2] == "Charles Casper Stockham":
            Charles += 1
        
        elif row[2] == "Diana DeGette":
            Diana += 1
        
        else:
            Raymon += 1
    
    #Calculates the percentage of votes for each candidate
    Charles_percent = round((Charles/vote_count)*100,3)
    Diana_percent = round((Diana/vote_count)*100,3)
    Raymon_percent = round((Raymon/vote_count)*100,3)


    
    
    
    #Calculates the winner
    most_votes = max(Charles,Diana,Raymon)

    if most_votes == Charles:
        winner = "Charles Casper Stockham"
    
    
    elif most_votes == Diana:
        winner = "Diana DeGette"
    
    else:
        winner = "Raymon Anthony Doane"
    

    output = ["Election Results\n" + #list of output text for the Election_Result.txt
    "\n-------------------------------------\n" +
    f"\nTotal Votes: {vote_count} \n" +
    "\n-------------------------------------\n" +
    f"\nCharles Casper Stockham: {Charles_percent}% ({Charles})\n" +
    f"\nDiana DeGette: {Diana_percent}% ({Diana})\n" +
    f"\nRaymon Anthony Doane: {Raymon_percent}% ({Raymon})\n" +
    "\n-------------------------------------\n" +
    f"\nWinner: {winner}\n"
    "\n-------------------------------------"]


    print("Election Results\n" + #print statement of the Election_Result.txt
    "\n-------------------------------------\n" +
    f"\nTotal Votes: {vote_count} \n" +
    "\n-------------------------------------\n" +
    f"\nCharles Casper Stockham: {Charles_percent}% ({Charles})\n" +
    f"\nDiana DeGette: {Diana_percent}% ({Diana})\n" +
    f"\nRaymon Anthony Doane: {Raymon_percent}% ({Raymon})\n" +
    "\n-------------------------------------\n" +
    f"Winner: {winner}"
    "\n------------------------------------- ")

#Writes the output to a .txt file
with open(Election_Results, 'w') as csvfile:

    writer = csv.writer(csvfile, delimiter = ',')

    writer.writerow(output)
    
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
pathoutput=os.path.join('Resources','election_results.txt')
votes = []
candidates = []

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter = ',')
   csv_header = next(csvreader)
   
   for row in csvreader:
       votes.append(row[0])
       candidates.append(row[2])

   Total_Votes = (len(votes))
   (f"Total Votes: {Total_Votes}")
   Khan = int(candidates.count("Khan"))
   Correy = int(candidates.count("Correy"))
   Li = int(candidates.count("Li"))
   O_Tooley = int(candidates.count("O'Tooley"))
   
   #Get a percentage of each candidates vote total
   Khan_percentage = (Khan/Total_Votes) * 100
   Correy_percentage = (Correy/Total_Votes) * 100
   Li_percentage = (Li/Total_Votes) * 100
   O_Tooley_percentage = (O_Tooley/Total_Votes) * 100
   
    #Compare Votes and pick winner with the most votes
   if Khan > Correy > Li > O_Tooley:
       Winner = "Khan"
   elif Correy > Khan > Li > O_Tooley:
       Winner = "Correy"
   elif Li > Khan > Correy > O_Tooley:
       Winner = "Li"
   elif O_Tooley > Khan > Correy > Li:
       Winner = "O'Tooley"
   
   #Print each candidate's name, vote percentage, and raw number of votes
   output= (
        f"\nElection Results\n"
        f"__________________\n"
        f"Khan: {Khan_percentage}% ({Khan})\n"
        f"Correy: {Correy_percentage}% ({Correy})\n"
        f"Li: {Li_percentage}% ({Li})\n"
        f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley})\n"
        f"Winner: {Winner}\n")
   
   #print output to terminal
   print(output)
   
   #store to text file
with open('output') as textfile:
    textfile.write(output)


import csv 
import os

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print ("Election Results")
    print ("------------------------")
    total = sum(1 for _ in csvfile)
    print("Total Votes: " + str(total))
    print ("------------------------")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    

#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#As an example, your analysis should look similar to the one below:
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.


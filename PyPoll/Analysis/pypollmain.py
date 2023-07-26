# Import the os module. This allows to create file paths
import os
#import module for reading csv files
import csv

#Initialize lists to store data.  Don't need the voterid row[0] and county row [1] columns from the source file. 
candidates=[]
winning_candidate = ""

#for dictionary Keys: Candidates are Names, Vote_percent is percentage of votes each candidate won, votes is the number of votes each candidate won. Dictionary can be denoted with either dict() or ={}
#candidate_votes= dict(). #dictionaries can hold lists as values. Keys are strings. Values can be added.
candidate_votes={}

#Counter set up
total_votes = 0  # total of all the votes in the file. 

#store the file path associated with the csv file election_data.csv. getting the path from cvspath = os.path.join("PyPoll","Resources", "election_data.csv") did not work for me. 
#This method worked. 
csvpath = os.path.join("python_challenge/PyPoll/Resources/election_data.csv")
print(csvpath)

#read csv file as csv file Read only operation
with open (csvpath) as csvfile:
    datafile = csv.reader(csvfile, delimiter = ",")
    #print(csvreader) to test.

    #read header row first, and after that just read the row begining with after the header row with the next(csvfile) function.
    csv_header = next(datafile)
    
    #Read through each row after the header row
    for row in datafile:
        #count the rows after the header to get the Total Votes. All the rows after the header are with candidate names each with voterid. each voterid represents 1 vote. 
        # There are no blanks or missing values in voterid. Verified this by looking at the datafile.   
        total_votes = total_votes + 1

        #complete list of candidates 
        names = row[2]

        #Add the name to the Candidates list in dictionary if it is not in there. Do not add duplicate names. 
        if names not in candidates:
            candidates.append(names)

            # start counting votes for the name
            candidate_votes[names]=0

        #Add the 1 to this candidates Votes_count
        candidate_votes[names]=candidate_votes[names] + 1
                
    # print Analysis Report to Terminal, the Titles for analysis report
    print("---------------------")         
    print("  Election Results ")
    print("---------------------")
           
    #print(Total_Votes) to test that it skips the header and reads all the rows.  #Yay! got the right answer 369711. This is the total number of votes all candidates won.
    print("Total Votes: "+ str(total_votes))

    #find the highest vote count which is the winner
    winning_count=max(candidate_votes.values())
      
    #print to check if the counter worked
    #print(candidate_votes) 

    #calculations for each candidate
    #create a dictionary called candidate_percent
    candidate_percent={}
    for candidate in candidates: 
        #get the vote count for each candidate won.
        votes=candidate_votes[candidate]
        
        #calculate the percentage of votes each candidate won
        vote_percentage = float(votes) / float(total_votes) * 100

        # convert percentage number to 3 decimal places 
        vote_percentage=round(vote_percentage,3)

        #add the candidate's vote percentage dictionary to the candidate Key that is in the candidate_votes dictionary. Nested dictionary.
        candidate_percent[candidate]=vote_percentage

#print each candidate's Name, their vote_percentage of total votes with the % sign, and in parenthesis their total votes count.  vote_percentage with % symbol #print (str(vote_percentage) +("%"))
for Name, Percentage in candidate_percent.items():
   # for votes in candidate_votes.items():
    print (Name + " " + str(Percentage) + "%" + " (" + str(candidate_votes[Name])+ " )") # +"%"+"("str(votes)+")")


#find the winner. winner has the highest number of vote count
if votes >= winning_count:
        winning_count = votes
        winning_candidate = candidate 
        #print(winning_count)  Test to see if correct Winner. Winner is candidate Diana DeGette with the winning _count of 272892
        #print(winning_candidate) could not figure out how to get this to print Diana DeGette. 
print("------------------")              
print("Winner: " + str(winning_count)) # got it to print the corrent winning_count but I couldn't get the winning_candidate to print. 
print("------------------")

#create an output txt file named 'mypypollAnalysis.txt' in folder PyPoll from python code. Yay, code did create the file! WooHoo! 
output_path=os.path.join("python_challenge/PyPoll/Analysis/mypypollAnalysis.txt")
file=open(output_path, "w")  #'w' will rewrite over file if it finds a file with the same name; 'x' doesn't rewrite if same file name

#write lines of analysis report in txt file 
file.write("---------------------")         
file.write("  Election Results ")
file.write("---------------------")
file.write("Total Votes: "+ str(total_votes))
file.write(Name + " " + str(Percentage) + "%" + " (" + str(candidate_votes[Name])+ " )")
file.write ("------------------")              
file.write ("Winner: "+ str(winning_count))
file.write ("------------------")
#close txt file after writing to it completed
file.close
  
#_______________________________________________________________________________________________________   
#PyPoll Assignment Instructions and expected results. #given a set of poll data called election_data.csv. 
# #The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

#Your analysis should align with the following results:
#Election Results
#_____________
# Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------
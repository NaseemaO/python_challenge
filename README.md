# python_challenge
Challenge 3 Assignment is OF two parts: Pybank and PyPoll each with their respective resource input csv files. Objective: Create python scripts that run and print the generated Reports to Terminal and produce text files with the Reports written in the text files.   

Worked in VSC on the Python scripts for this assignment. 

Details on instructions and expected results are pasted below. 

Credits/ Resources: To my Instructor, TAs, Tutors. Class recordings that I watched many many times. Received information and guidance for understanding and troubleshooting from the World Wild Web! Google and YouTube and posts on GitHub.   

I have comments in the python scrips for both Pybank and Pypoll scripts.  I want to be sure I can read my own code; it kept getting so confusing... would work..would break..would fix.. would work..etc etc.. until I got to the final results. 
One break that I unfortunately could not recall / fix that worked fine initially was getting the Winning Candidates name to print to the report in the Winner field, so I just printed her winning vote count in there instead!
Please do give me your feedback on fixing that issue as it is driving me nuts! Thank you!

I have pasted the resulting Reports from the runs of my codes below.   
_______________________________________________________________________________________________________________
Pybank INSTRUCTIONS: In this Challenge: tasked with creating a Python script to analyze the financial records of your company using a financial dataset called budget_data.csv. 
The dataset is composed of two columns: "Date" and "Profit/Losses".
Create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The changes in "Profit/Losses" over the entire period, and then the average of those changes
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in profits (date and amount) over the entire period

EXPECTED RESULTS TO COMPARE AGAINST:

Financial Analysis
------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
In addition, final script should both print the analysis to the terminal and export a text file with the results.

PyPoll INSTRUCTIONS: In this Challenge,tasked with helping a small, rural town modernize its vote-counting process.
Given is a set of poll data called election_data.csv. 
The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
Create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote

EXPECTED RESULTS:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
________________________________________________________________________________________________________

My Results: 

Pybank: My python file "mypybankmain.py" with code that printed the Report to Terminal, created output text file 'mypybankAnalysis.txt" and wrote the report in the text file.

Here is a paste of the report that printed to my Terminal when I ran the code, and it generated the expected text file with data written to it. 

PS C:\Users\Owner\Documents\GitHub> & "C:/Users/Owner/anaconda python/envs/dev/python.exe" c:/Users/Owner/Documents/GitHub/python_challenge/Pybank/Analysis/pybankmain.py
python_challenge/Pybank/Resources/budget_data.csv
---------------------
 Finanacial Analysis
---------------------
Total Months:  86
Total Profit / Loss: $ 22564198
Average Change: $ -8311.11
Greatest Increase in Profits: $ Aug-16 (1862002)
Greatest Decrease in Profits: $ Feb-14 (-1825558)
---------------------
PS C:\Users\Owner\Documents\GitHub>
------------------------------------------------------------------------------------------------------------
PyPoll: My Python file called my "mypypollmain.py" with code ran to print the Election Results report to the Terminal and producted a text file with print to text file. 
I got the winning votes count and the associated candidate with the winning number of votes, but could not figure out how to get the Winner's name to print in the report 
so instead I have the total number of the Winner the winning_candidates vote count in the report. 
here is a paste of what I got to print to Terminal when I ran the code. 

PS C:\Users\Owner\Documents\GitHub> & "C:/Users/Owner/anaconda python/envs/dev/python.exe" c:/Users/Owner/Documents/GitHub/python_challenge/PyPoll/Analysis/pypollmain.py
python_challenge/PyPoll/Resources/election_data.csv
---------------------
  Election Results 
---------------------
Total Votes: 369711
Charles Casper Stockham 23.049% (85213 )
Diana DeGette 73.812% (272892 )
Raymon Anthony Doane 3.139% (11606 )    
------------------
Winner: 272892
------------------
PS C:\Users\Owner\Documents\GitHub>     

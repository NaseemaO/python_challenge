#Import Modules for functions
# Import the os module. This allows to create file paths
import os
#import module for reading csv files
import csv

#store the file path associated with the csv file. 
#csvpath = os.path.join("Pybank","Resources", "budget_data.csv")
csvpath = os.path.join("python_challenge/Pybank/Resources/budget_data.csv")
print(csvpath)

#Initialize Lists to store data 
Months = []
Profit_Loss = []
Changes= []
Dates=[]

#read csv file as csv file 
with open (csvpath) as csv_file:
    datafile = csv.reader (csv_file, delimiter = ",")
    #print(datafile)  print to check code.

    #read header row first, and print Header
    csv_header=next(datafile)
    #print(csv_header) print to check code.

    # Read each row of data after the header
    for row in datafile:
        
        #The month date is in index 0. 
        current_date = row[0]
        #print(row[0]) print to check code.

        #The current profit loss is in index 1
        current_profit_loss = float(row[1])
        #print(current_profit_loss)

        #separate the string of month and day. .split splits the data by the separator '-'
        separated_date_array = current_date.split("-")
        #print(separated_date_array)

        #Put the separated data from index 1 of the separated_data_array into a list called Current_Month
        Current_Month = separated_date_array[0]
        #print(Current_Month)

        #append the current_months to the variable Months to get only the months in the Tuple Current_Month. Data doesn't change in the Tuple.
        Months.append(Current_Month)
        #print to check
        #print(Months)
        Dates.append(current_date) #storing all dates also

        #Put the data of current_profit_loss into a Tuple Profit_Loss
        Profit_Loss.append(float(current_profit_loss))
#print Analysis Report on Python Terminal code runs on
print ("---------------------")        
print (" Finanacial Analysis")
print ("---------------------")

#Get the total months in Months using len for length of indexes which are months in Months
Total_Months = len(Months)
print("Total Months: ", + Total_Months)    

Total_Profit_Loss=sum(Profit_Loss)
#print(Profit_Loss)
#print Profit_Loss with the '$' sign.  And to make the Total_Profit_Loss an integer no decimal places. 
print("Total Profit / Loss: $",+ int(Total_Profit_Loss))

# x is the current month's profit loss. It doesn't have a previous month's profit loss to compare it to.  Set the Profit loss with 0 in index 0 as the starting profit loss. 
Last_Profit_Loss = Profit_Loss[0]
for x in Profit_Loss[1:]:       
    current_diff = x-Last_Profit_Loss
    #print(current_diff)

    # all the changes in profit_loss from one month to another over entire period is in the current_diff 
    #put the current_diff values in Changes tuple. #Need to float values in current_diff for calculations in string with numbers. 
    Changes.append(float(current_diff))  #if I had this line after the line Last_Profit_Loss=x, it was only saving the x for the Last_Profit_Loss. 
    Last_Profit_Loss = x    
#print(Changes)

#find the mean of values in Changes. This is the average of values in the Changes. 
average =(sum(Changes)/len(Changes))
# need to round to 2 decimal points
average=round(average,2)
#print (average)  or sentence with value
print ("Average Change: $",+ average)   


#find the max of values in Changes. This is the greatest increase in profits.  Get the Date and Amount.  Find the zero index in flie which is month date for this value.
Greatest_Increase = max(Changes)
#use index to find the row associated with the Greatest Increase to get the Month and Date. 
Greatest_Increase_index = 0
i = 1
for x in Changes:
    if x == Greatest_Increase:
        Greatest_Increase_index=i  #searching for the greatest increase row. 
    i = i + 1
#print(Dates[Greatest_Increase_index]) test aganist expected result
Greatest_Increase = round(Greatest_Increase,2)
# or print(max(Changes))  Make the number an integer
print ("Greatest Increase in Profits: $ "+ Dates[Greatest_Increase_index] + " (" + str(int(Greatest_Increase)) + ")")   

#find the min of values in Changes. This is the greatest decrease in profits. Get the Date and Amount. Find the zero index in file which is the month and date for this value.
Greatest_Decrease = min(Changes)
Greatest_Decrease_index = 0
i = 1
for x in Changes:
    if x == Greatest_Decrease:
        Greatest_Decrease_index=i  #searching for the greatest decrease row. 
    i = i + 1
Greatest_Decrease=round(Greatest_Decrease,2)
Greatest_Decrease_Date = Dates[ Greatest_Decrease_index]
# print (min(Changes)) and make the number an integer
print ("Greatest Decrease in Profits: $ "+ Dates[Greatest_Decrease_index] + " (" + str(int(Greatest_Decrease)) +')') 
print("---------------------")

#the highest change, and the lowest change values for testing.  Change values = 1862002.00 and -1825558.00 


#create an output txt file named 'mypybankAnalysis.txt' in folder Pybank from python code. Yay, code did create the file! WooHoo! 
output_path=os.path.join("python_challenge/Pybank/Analysis/mypybankAnalysis.txt")
file=open(output_path, "w")  #'w' will rewrite over file if it finds a file with the same name; 'x' doesn't rewrite if same file name
#write lines of analysis report in txt file 
file.write("---------------------")         
file.write(" Finanacial Analysis")
file.write("---------------------")
file.write("Total Months: "+ str(Total_Months))   
file.write("Total Profit / Loss: "+ str(Total_Profit_Loss)) 
file.write("Average Change: " + str(average))     
file.write("Greatest Increase in Profits: $ "+ Dates[Greatest_Increase_index] + " (" + str(int(Greatest_Increase)) + ")")  
file.write("Greatest Decrease in Profits: $ "+ Dates[Greatest_Decrease_index] + " (" + str(int(Greatest_Decrease)) +')') 
file.write("---------------------")
#close txt file after writing to it completed
file.close

#___________________________________________________________________________________________________________________
#Assignment Challenge 3 Python: In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#	The total number of months included in the dataset
#	The net total amount of "Profit/Losses" over the entire period
#	The changes in "Profit/Losses" over the entire period, and then the average of those changes
#	The greatest increase in profits (date and amount) over the entire period
#	The greatest decrease in profits (date and amount) over the entire period
#Your analysis should align with the following results:
#Financial Analysis
#------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.


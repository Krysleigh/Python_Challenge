import os
import csv

#path to collect data from the Resources folder
budget_data= os.path.join("Resources","budget_data.csv")

#Represents the total number of months
#Represents the total profit or loss
#Represents the net change.
total_month= 0
total_profitloss= 0
value= 0
net_change= 0

#Loop through dates
#Loop through profits
dates= []
profits= []

# Variables to track greatest increase and decrease
greatest_increase= 0
greatest_decrease= 0
gi_date= ""
gd_date= ""

# Open the CSV file named 'budget_data' and create a file object.
# Create a CSV reader object, specifying the delimiter as ",".
with open(budget_data) as csv_file:
	csv_reader=csv.reader(csv_file, delimiter=",")
	
	# Read and store the header row of the CSV file.
	csv_header= next(csv_reader)

#Iterate through each row in the CSV file.
	for row in csv_reader:
		date= row[0]
		total_month+= 1
		profitloss = int(row[1])
		total_profitloss+= profitloss
		
		#Check if total months is greater than 1.
		if total_month>1:
			net_change+= profitloss - profits[-1]
		
		#Append the date the dates lis and profit/loss value to profits list.
		dates.append(date)
		profits.append(profitloss)
		
		# Check for greatest increase
		if profitloss > greatest_increase:
			greatest_increase= profitloss
			greatest_increase_date= date

			# Check for greatest decrease
		if profitloss < greatest_decrease:
			greatest_decrease= profitloss
			greatest_decrease_date= date

# Calculate average change
avg_profit_change= net_change / (total_month -1)

#Print Financial Analysis
print(f"Financial Analysis")
print(f"------------------------------------------")
print(f"Total Months: {total_month}")
print(f"Total: (${total_profitloss})")
print(f"Average Change {avg_profit_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# writing multiple lines in a Text File
import os

#Create an output path and text document
analysis_output = os.path.join('analysis', 'PyBankAnaysis.txt')

# Open the file specified by analysis_output
with open(analysis_output, 'w') as f:
	f.write("Financial Analysis\n")
	f.write("--------------------------------------\n")
	f.write(f"Total Months: {total_month}\n")
	f.write(f"Total: (${total_profitloss})\n")
	f.write(f"Average Change {avg_profit_change:.2f}\n")
	f.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
	f.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

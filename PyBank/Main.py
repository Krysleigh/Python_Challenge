import os
import csv

budget_data= os.path.join("Resources","budget_data.csv")
total_month= 0
total_profitloss= 0
value= 0
net_change= 0
dates= []
profits= []

# Variables to track greatest increase and decrease
greatest_increase= 0
greatest_decrease= 0
gi_date= ""
gd_date= ""

with open(budget_data) as csv_file:
	csv_reader=csv.reader(csv_file, delimiter=",")

	csv_header= next(csv_reader)


	for row in csv_reader:
		date= row[0]
		total_month+= 1
		profitloss = int(row[1])
		total_profitloss+= profitloss
		
		if total_month>1:
			net_change+= profitloss - profits[-1]
		
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

print(f"Financial Analysis")
print(f"------------------------------------------")
print(f"Total Months: {total_month}")
print(f"Total: (${total_profitloss})")
print(f"Average Change {avg_profit_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# writing multiple lines in a Text File
import os

analysis_output = os.path.join('analysis', 'PyBankAnaysis.txt')

with open(analysis_output, 'w') as f:
	f.write("Financial Analysis\n")
	f.write("--------------------------------------\n")
	f.write(f"Total Months: {total_month}\n")
	f.write(f"Total: (${total_profitloss})\n")
	f.write(f"Average Change {avg_profit_change:.2f}\n")
	f.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
	f.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

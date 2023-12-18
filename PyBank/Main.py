import os
import csv

budget_data= os.path.join("Resources", "budget_data.csv")
	total_month= 0
	total_profitloss= 0
	value= 0
	change= 0
	dates= []
	profits= []

with open("budget_data") as csvfile:
	csvreader=csv.reader(csvfile)
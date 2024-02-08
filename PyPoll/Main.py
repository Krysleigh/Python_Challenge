import os
import csv

csv_file_path = "Resources/election_data.csv"

total_votes = 0
ballot_id = []
county = []
candidate = []

# Counting total votes and setting candidate votes to zero
charles = 0
diana = 0
raymon = 0

with open(csv_file_path) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")

    # Count total votes
	total_votes = sum(1 for row in csv_reader)

# Resetting the file pointer to the beginning of the file
with open(csv_file_path) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")

	for row in csv_reader:
       
		# votes for candidates
		if row[2] == "Charles Casper Stockham":
			charles += 1
		elif row[2] == "Diana DeGette":
			diana += 1
		else:
			raymon += 1
		ballot_id.append(row[0]) 

# percentages of votes per candidate
percent_charles = round(charles / len(ballot_id) * 100, 3)
percent_diana = round(diana / len(ballot_id) * 100, 3)
percent_raymon = round(raymon / len(ballot_id) * 100, 3)

# printing election results
print("Election Results")

# printing separating line
print("---------------------------")

# printing total number of votes
print("Total Votes:", total_votes)

# printing separating line
print("---------------------------")

# printing the votes for each candidate
print("Charles Casper Stockham: " + str(percent_charles) + "%  (" + str(charles) + ")")
print("Diana DeGette: " + str(percent_diana) + "%  (" + str(diana) + ")")
print("Raymon Anthony Doane: " + str(percent_raymon) + "%  (" + str(raymon) + ")")

# printing separating line
print("---------------------------")
# printing the winning candidate
if charles > diana and charles > raymon:
    print("Winner: Charles Casper Stockham")
elif diana > charles and diana > raymon:
    print("Winner: Diana DeGette")
else:
    print("Winner: Raymon Anthony Doane")
print("---------------------------")

# writing multiple lines in a Text File
import os

analysis_output = os.path.join('analysis', 'PypollAnaysis.txt')

with open(analysis_output, 'w') as f:
	f.write("Election Results\n")
	f.write("--------------------------------------\n")
	f.write(f"Total Votes: {total_votes}\n")
	f.write("--------------------------------------\n")
	f.write(f"Charles Casper Stockham: {percent_charles}%  ({charles})\n")
	f.write(f"Diana DeGette: {percent_diana}%  ({diana})\n")
	f.write(f"Raymon Anthony Doane: {percent_raymon}%  ({raymon})\n")
	f.write("--------------------------------------\n")
	if charles > diana and charles > raymon:
		f.write("Winner: Charles Casper Stockham\n")
	elif diana > charles and diana > raymon:
		f.write("Winner: Diana DeGette\n")
	else:
		f.write("Winner: Raymon Anthony Doane\n")
	f.write("--------------------------------------\n")


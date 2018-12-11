# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

csvfile = 'Resources/election_data.csv'

candidates = {}
each_candidate_vote = 0
candidates_percent = {}

with open(csvfile) as data:
#  headerline = data()
    reader = csv.reader(data)
    next(reader, None)
    row_count = 0

    for row in csv.reader(data):
        row_count += 1


        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

for key, value in candidates.items():
   candidates_percent[key] = round((value/row_count) * 100, 2)

print(" ====================== \n")
print("  Voting Analysis  \n")
print(" ====================== \n")
print("Total Votes: " + str(row_count) + "\n")
print("===========================\n")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
print("============================ \n")

# creating new text file
analysis = open("Resources/voting_analysis_jatin.txt", "w")

# writing the new file
analysis.write(" ====================== \n")
analysis.write("|  Voting Analysis  |\n")
analysis.write(" ====================== \n")
analysis.write("Total Votes: " + str(row_count) + "\n")
analysis.write("===========================\n")
for key, value in candidates.items():
    analysis.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
analysis.write("============================ \n")
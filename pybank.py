# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

csvfile = 'Resources/budget_data.csv'

# Open the CSV
# with open(csvpath, newline="") as csvfile:
#    csvreader = csv.reader(csvfile, delimiter=",")

# Count number of lines
# value = len(list(csvreader)
# print("# of lines" + str(value))

# row_count = sum(1 for row in csv.reader( open(csvfile) ) )
# print(str(row_count - 1))

print("csvfile" + csvfile)

with open(csvfile) as data:
#  headerline = data()
    reader = csv.reader(data)
    next(reader, None)
    row_count = 0
    total = 0
    biggest_increase = 0
    biggest_increase_date = ""
    biggest_decrease = 0
    biggest_decrease_date = ""
    monthly_difference = 0
    first_row = next(reader)
    prev_row = int(first_row[1])
    total_difference = 0

    for row in csv.reader(data):
        row_count += 1
        total += int(row[1])


        
        monthly_difference = int(row[1]) - prev_row
        prev_row = int(row[1])
        print(monthly_difference)
        total_difference = monthly_difference + total_difference 
      
        if int(row[1]) >= biggest_increase:
            biggest_increase = int(row[1])
            biggest_increase_date = row[0]
        if int(row[1]) <= biggest_decrease:
            biggest_decrease = int(row[1])
            biggest_decrease_date = row[0]

average = total_difference/row_count
print(average)

print(" ====================== ")
print("|  Financial Analysis  |")
print(" ====================== ")
print("Total # of Rows:  " + str(row_count))
print("Total Revenue:  $" + str(total))
print("Average Monthly Difference  $    TBD")
print("Biggest Increase in Revenue: " + biggest_increase_date + " and ($" + str(biggest_increase) + ") over the entire period.")
print("Biggest Decrease in Revenue: " + biggest_decrease_date + " and ($" + str(biggest_decrease) + ") over the entire period.")


# creating new text file
analysis = open("Resources/financial_analysis_jatin.txt", "w")

# writing the new file
analysis.write(" ====================== \n")
analysis.write("|  Financial Analysis  |\n")
analysis.write(" ====================== \n")
analysis.write("Total # of Rows:  " + str(row_count) + "\n")
analysis.write("Total Revenue:  $" + str(total) + "\n")
analysis.write("Average Monthly Difference  $    TBD \n")
analysis.write("Biggest Increase in Revenue: " + biggest_increase_date + " and ($" + str(biggest_increase) + ") over the entire period. \n")
analysis.write("Biggest Decrease in Revenue: " + biggest_decrease_date + " and ($" + str(biggest_decrease) + ") over the entire period. \n")

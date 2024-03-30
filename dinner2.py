import csv
with open('dinner.csv', newline='') as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        print(row)

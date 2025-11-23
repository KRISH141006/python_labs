import csv

with open("data-1.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

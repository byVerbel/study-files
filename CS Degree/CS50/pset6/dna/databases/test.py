import csv

with open("small.csv", "r") as file:
    reader = csv.DictReader(file)
    for i in reader:
        print(i)

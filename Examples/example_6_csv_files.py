import csv

with open('data/input.csv', 'r') as file:
    reader = csv.DictReader(file)  # convert csv file list of dictionary we can loop over it

    for person in reader:
        print(f'{person["Name"]} is {person["Age"]}')

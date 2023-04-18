import csv
import os

sum=0

filename = os.getcwd() + '/2023hours.csv'

rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

people = dict()

for row in rows:
    if row[1] in people:
        people[row[1]] += float(row[5])
    else:
        people[row[1]] = float(row[5])
print(people,"\n")

for row in rows:
    sum += float(row[5])

print("We are required to get 828 service hours")
print("We have {} hours".format(sum))
need=828-sum
print("We still need {} hours".format(need))
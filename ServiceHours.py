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
sorted_tuples = sorted(people.items())
sorted_people = dict(sorted_tuples)
for key in sorted_people:
    print(key, ' : ', people[key])


for row in rows:
    sum += float(row[5])

need=828-sum

print("")
print("We are required to get 828 service hours")
print("We have {} hours".format(sum))

if need<1:
    print("We have met our service hour requirement. Hurray!")
else:
    print("We still need {} hours".format(need))

# Reading csv Files

import csv
with open("Resources/Employee.csv", "r") as fh:
    ereader = csv.reader(fh)
    print("File Employee.csv contains :")
    for rec in ereader:
        print(rec)

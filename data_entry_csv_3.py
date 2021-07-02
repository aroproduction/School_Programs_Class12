# Entering data in csv files
import csv
fh = open("Resources/Employee.csv", "w", newline="")
ewriter = csv.writer(fh)
empdata = [
    ['Empno', 'Name', 'Designation', 'Salary'],
    [1001, 'Trupti', 'Manager', 56000],
    [1002, 'Raziya', 'Analyst', 35000],
    [1004, 'Silviya', 'Clerk', 25000],
    [1005, 'Suji', 'PR Officer', 31000]
    ]
ewriter.writerows(empdata)
print("File successfully created")
fh.close()

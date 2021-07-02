# Entering data in csv files
import csv
fh = open("../Resources/Student.csv", "w")
stuwriter = csv.writer(fh)
rec = ['Rollno', 'Name', 'Marks']
stuwriter.writerow(rec)

for i in range(2):
    print("Student record", (i+1))
    name = input("Enter Name: ")
    rollno = int(input("Enter Roll Number: "))
    marks = float(input("Enter Marks: "))
    # sturec = [name, rollno, marks]
    stuwriter.writerow([name, rollno, marks])

fh.close()

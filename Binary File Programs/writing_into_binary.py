import pickle
stu = {}
stufile = open('../Resources/Stu.dat', 'wb')
ans = 'y'
while ans == 'y':
    rno = int(input("Enter Roll No.: "))
    name = input("Enter Name: ")
    marks = float(input("Enter marks: "))
    stu['Rollno'] = rno
    stu['Name'] = name
    stu['Marks'] = marks
    pickle.dump(stu, stufile)
    ans = input("Want to enter more records? (y/n)...")

stufile.close()

stufile = open("../Resources/Stu.dat", "rb")
try:
    while True:
        print(pickle.load(stufile))
except EOFError:
    stufile.close()

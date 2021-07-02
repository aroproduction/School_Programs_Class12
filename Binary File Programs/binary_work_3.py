# Searching in Binary Files
import pickle
stu = {}
found = False
fin = open('../Resources/Stu.dat', 'rb')
searchkeys = [1, 3]

try:
    print("Searching in File Stu.dat...")
    while True:
        stu = pickle.load(fin)
        if stu['Rollno'] in searchkeys:
            print(stu)
            found = True
except EOFError:
    if not found:
        print("No such records found in the file")
    else:
        print("Search Successful.")
    fin.close()

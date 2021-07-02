# Searching in Binary Files
import pickle
stu = {}
found = False
print("Searching in file Stu.dat...")

with open("../Resources/Stu.dat", "rb") as fin:
    stu = pickle.load(fin)
    if stu['Marks'] > 81:
        print(stu)
        found = True

if not found:
    print("No records with Marks > 81")
else:
    print("Search Successful.")

# Updating name in existing binary file
import pickle
stu = {}
found = False
fin = open('../Resources/Stu.dat', "rb+")

try:
    while True:
        rpos = fin.tell()
        stu = pickle.load(fin)
        if stu['Rollno'] == 5:
            stu['Name'] = 'Gurnam'
            fin.seek(rpos)
            pickle.dump(stu, fin)
            found = True

except EOFError:
    if found == False:
        print("Sorry, no matching record found")
    else:
        print("\n"+"Record(s) successfully updated.\n")
    fin.close()

with open('../Resources/Stu.dat', 'rb') as file:
    print('Updated Records:')
    try:
        while True:
            updated = pickle.load(file)
            if updated['Rollno'] == 5:
                print(updated)
    except EOFError:
        pass

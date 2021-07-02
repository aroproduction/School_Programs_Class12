# Updating marks in existing binary file

import pickle
stu = {}
found = False
fin = open('../Resources/Stu.dat', 'rb+')

try:
    while True:
        rpos = fin.tell()
        stu = pickle.load(fin)

        if stu['Marks'] > 81:
            stu['Marks'] += 2
            fin.seek(rpos)
            pickle.dump(stu, fin)
            found = True
except EOFError:
    if found == False:
        print("Sorry, no matching record found")
    else:
        print("\n"+"Record(s) successfully updated."+"\n")
    fin.close()
   
with open('../Resources/Stu.dat', 'rb') as file:
    updated_records = {}
    print("Updated Records:")
    try:
        while True:
            updated_records = pickle.load(file)
            if updated_records['Marks'] > 83:
                print(updated_records)
            else:
                pass
    except EOFError:
        pass

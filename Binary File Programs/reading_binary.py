# Reading Binary Files

import pickle
stu = {}
fin = open('../Resources/Stu.dat', 'rb')
try:
    print("\n"+"File Stu.dat stores these records")
    while True:
        stu = pickle.load(fin)
        print(stu)
except EOFError:
    fin.close()

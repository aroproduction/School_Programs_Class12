# Reading Binary Files
import pickle
emp = {}
empfile = open('Resources/empfile.dat', 'rb')
try:
    while True:
        emp = pickle.load(empfile)
        print(emp)
except EOFError:
    empfile.close()

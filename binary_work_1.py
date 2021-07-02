# Binary Files
import pickle
str1 = "This is my first line. This is second line."

with open("Resources/myfile.info", "ab") as fh:
    pickle.dump(str1, fh)

print("File successfully created.")

with open("Resources/myfile.info", "rb") as rh:
    print(pickle.load(rh))

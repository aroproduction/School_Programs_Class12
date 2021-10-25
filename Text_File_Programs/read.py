# reading from a text file
myfile = open(r'./poem.txt', 'r')
str1 = myfile.read()
print(str1)
myfile.close()

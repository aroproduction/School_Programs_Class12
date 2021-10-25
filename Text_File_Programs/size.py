file = open(r'./poem.txt', 'r')
str1 = ' '
size = 0
tsize = 0
while str1:
    str1 = file.readline()
    tsize += len(str1)
    size += len(str1.strip())

print("Size of file after removing all EOL characters & blank lines:", size)
print("The total size of the file:", tsize)
file.close()

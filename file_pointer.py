# Inro to File Pointer

fh = open("Resources/Marks.txt", "r")
print('\n', end='')
print(fh.read())
print("File-pointer is now at byte :", fh.tell(), '\n')

fh = open("Resources/Marks.txt", "r")
fh.seek(0, 1)
str1 = fh.read(15)
print("Last 15 bytes of file contain :", str1)

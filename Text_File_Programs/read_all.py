file = open(r'./poem.txt', 'r')
ch = ' '
while ch:
    ch = file.readline()
    print(ch, end=' ')

# Entering data in csv files
import csv
fh = open("Resources/compresult.csv", "w")
cwriter = csv.writer(fh)
compdata = [
    ['Name', 'Points', 'Rank'],
    ['Shradha', 4500, 23],
    ['Nischay', 4800, 31],
    ['Ali', 4500, 25],
    ['Adi', 5100, 14]
    ]

cwriter.writerows(compdata)
fh.close()

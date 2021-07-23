"""
write a program in python to read lines from a text file "india.txt" to find and display
the occurnce of the word "India".
"""

file = open("../Resources/india.txt", "r")
file_content = file.readlines()
india_count = 0
for i in file_content:
    if "India" in i:
        c = i.count("India")
        india_count += c
        

print("The number count of 'India' in 'india.txt' is", india_count)
file.close()

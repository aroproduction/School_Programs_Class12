# Program to count the number of "the" in a given file

file = open("../Resources/file.txt", "r")
file_content = file.read()
the_counts = file_content.count("the")
print("The number count of 'the' in 'file.txt' is", the_counts)
file.close()

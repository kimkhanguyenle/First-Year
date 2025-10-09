"""
Student Name: Kim Kha Nguyen
Student ID: s8199557

"""

f = open("student.txt", "r")

for line in f:
    words = line.split()
    fName = words[0]
    sName = words[1]
    fee = float(words[3])
    advance = float(words[4])
    #calculate fees due
    due = fee - advance
    print(f"{(fName + ' ' + sName):<20} {due:>10.2f}")

"""
Student Name: Kim Kha Nguyen
Student ID: s8199557

"""


def read_data(filename):
    student_data = []  # list to store all students’ records

    # open the file in read mode
    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            # extract data from each line
            fName = words[0]
            sName = words[1]
            fee = float(words[3])
            advance = float(words[4])
            due = fee - advance

            # append one student's record as a list
            student_data.append([fName, sName, fee, advance, due])

    return student_data


def display_fee_owing(data):
    # print each student's name and amount owing
    for record in data:
        fName, sName, fee, advance, due = record
        print(f"{(fName + ' ' + sName):<20} {due:>10.2f}")


def main():
    filename = "student.txt"
    data = read_data(filename)
    display_fee_owing(data)


if __name__ == "__main__":
    main()


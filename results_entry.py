"""
Step 1
Write a program that allows a teacher to enter exam marks.
Valid marks are decimal numbers in the range of 0-100. The program should terminate when the teacher enters '999'
and display the average mark for the class, rounded to one decimal place.

Sample run:
INPUT: 56, 99, 23.5
OUTPUT: "Average mark for 3 students is: 59.5"

Additionally, handle the following errors::
If the entered mark is a numeric value but outside the range of 0-100, display an error message,
ignore the entry, and proceed to the next input.
If the entered mark is not a numeric value, display an error message stating "Not a number,"
ignore the entry, and proceed to the next input.
If '999' is entered as before the first valid input, display a message saying "No results entered"

Implementation:
Must use while loop.

Student Name: Kim Kha Nguyen
Student ID: s8199557
    
"""
total_marks = 0
student_count = 0

while True:
    user_input = input("Enter mark(0-100) or 999 to quit: ")

    # Check if user enter 999 before have valid mark 
    if user_input == "999" and student_count == 0:
        print("No results entered")
        break

    # Check if mark is not a number
    try:
        mark = float(user_input)
    except ValueError:
        print("Not a number")
        continue

    # if user enter 999 so break and not print anything
    if mark == 999:
        break

    # CHeck if mark outside the range 
    if mark < 0 or mark > 100:
        print("Number outside the range 0-100 inclusive")
        continue

    # Calculate total marks if valid    
    total_marks += mark
    student_count += 1

# after ending loop
if student_count > 0:
    average = total_marks / student_count
    print(f"Average mark for {student_count} students is: {average:.1f}")






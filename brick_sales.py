"""
Student Name:
Student ID:

"""
total_marks = 0.0
student_count = 0

while True:
    user_input = input("Enter mark(0-100) or 999 to quit: ")

    if user_input == "999" and student_count == 0:
        print("No results entered")
        break

    try:
        mark = float(user_input)
    except ValueError:
        print("Not a number")
        continue

    if mark == 999:
        break

    if mark < 0 or mark > 100:
        print("Number outside the range 0-100 inclusive")
        continue

    total_marks += mark
    student_count += 1

if student_count > 0:
    average = total_marks / student_count
    print(f"Average mark for {student_count} students is: {average:.1f}")


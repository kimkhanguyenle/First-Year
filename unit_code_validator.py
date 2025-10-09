"""
Student Name: Kim Kha Nguyen
Student ID: s8199557

"""

#validate course code will include 3 letters following by 4 digits
def validate_unit_code(course_code):
    # Check the length of the string
    if len(course_code) != 7:
        return False

    # check 3 beginning letters 
    if not course_code[:3].isalpha():
        return False

    # check last 4 digits
    if not course_code[3:].isdigit():
        return False

    return True


if __name__ == "__main__":
    units = ['NIT1102', 'vit220t', 'VAB1234', 'vzz4321', 'vit1102']

    for unit in units:
        print(f"Testing '{unit}':")
        if validate_unit_code(unit):
            print(f"'{unit}' is valid unit code\n")
        else:
            print(f"'{unit}' is NOT valid unit code\n")


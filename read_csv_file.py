"""
Student Name:
Student ID:

"""


def load_to_dict(filename):
    student_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # Split by comma instead of space
            parts = line.split(',')
            if len(parts) == 2:
                student_id, mark = parts
                student_dict[student_id] = int(mark)
    return student_dict

def main():
    filename = 'studData.txt'
    marks_dict = load_to_dict(filename)
    print("Marks dictionary:", marks_dict)

if __name__ == "__main__":
    main()

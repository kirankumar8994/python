students = {
    1: {"name": "RAM", "roll_no": 101, "total_mark": 85},
    2: {"name": "RONY", "roll_no": 102, "total_mark": 92},
    3: {"name": "RATHIN", "roll_no": 103, "total_mark": 78},
}

max_total_mark = -1
student_with_max_mark = None

for student_id, details in students.items():
    if details["total_mark"] > max_total_mark:
        max_total_mark = details["total_mark"]
        student_with_max_mark = details

if student_with_max_mark is not None:
    # Print details of the student with the highest total mark
    print("Student with the highest total mark:")
    print(f"Name: {student_with_max_mark['name']}")
    print(f"Roll Number: {student_with_max_mark['roll_no']}")
    print(f"Total Marks: {student_with_max_mark['total_mark']}")
else:
    print("No students found.")

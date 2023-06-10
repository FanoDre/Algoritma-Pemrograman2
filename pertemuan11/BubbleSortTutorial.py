
def bubble_sort_students(students):
    n = len(students)

    # Traverse through all student records
    for i in range(n - 1):
        # Last i student records are already in place
        for j in range(0, n - i - 1):
            # Swap if the current student's grade is greater than the next student's grade
            if students[j][2] < students[j + 1][2]:
                students[j], students[j + 1] = students[j + 1], students[j]


# Example usage:
student_records = [
    [12345, "John Doe", 80],
    [23456, "Jane Smith", 75],
    [34567, "Alice Johnson", 90],
    [45678, "Bob Williams", 85]
]

# Sort the student records by grade using bubble sort
bubble_sort_students(student_records)

# Print the sorted student records
print("Sorted student records:")
for student in student_records:
    print(f"NIM: {student[0]}, Name: {student[1]}, Grade: {student[2]}")

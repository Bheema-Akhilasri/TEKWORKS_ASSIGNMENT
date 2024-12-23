def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    else:
        return 'F'

student_number = input("Enter student number: ")
name = input("Enter student name: ")

marks_c,marks_cp,marks_java = map(float,input('Enter the marks of c,c++,java:').split())

total_marks = marks_c + marks_cp + marks_java
average_marks = total_marks / 3

result = "Pass" if average_marks >= 70 else "Fail"
grade = calculate_grade(average_marks) if result == "Pass" else "F"

print("\nResults:")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Result: {result}")
print(f"Grade: {grade}")

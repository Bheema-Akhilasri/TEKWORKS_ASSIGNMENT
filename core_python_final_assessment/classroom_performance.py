class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

def class_top_performer(students):
    averages = {student.name: student.average() for student in students}
    top_performer = max(students, key=lambda s: s.average()).name
    return averages, top_performer

students = [Student("John", [85, 78, 92]),Student("Alice", [88, 79, 95]),Student("Bob", [70, 75, 80])]
averages, top_performer = class_top_performer(students)
print("Average Marks:", {k: round(v, 2) for k, v in averages.items()})
print("Top Performer:", top_performer)

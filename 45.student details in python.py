class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def display_student_info(self):
        print(f"Name: {self.name}, Marks: {self.marks}, Average: {self.calculate_average():.2f}")

students = Student("Alice", [85, 90, 92])
students.display_student_info()

#Output:
Name: Alice, Marks: [85, 90, 92], Average: 89.00

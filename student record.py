class Student:
    def __init__(self, student_id, name, age, grades):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = grades

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grades: {self.grades}"

class StudentRecordManagement:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, grades):
        student = Student(student_id, name, age, grades)
        self.students.append(student)

    def view_students(self):
        if not self.students:
            print("No student records available.")
            return
        for student in self.students:
            print(student)

    def remove_student(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]

# Example usage
if __name__ == "__main__":
    student_record_management = StudentRecordManagement()
    student_record_management.add_student(1, "Alice", 20, {"Math": "A", "Science": "B"})
    student_record_management.add_student(2, "Bob", 22, {"Math": "B", "Science": "A"})

    print("Current Student Records:")
    student_record_management.view_students()

    print("\nRemoving student with ID 1")
    student_record_management.remove_student(1)

    print("\nUpdated Student Records:")
    student_record_management.view_students()
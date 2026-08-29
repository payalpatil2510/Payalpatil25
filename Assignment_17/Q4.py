class College:
    def __init__(self, numberOfStudents):
        self.numberOfStudents = numberOfStudents
        self.students = []
    def AddStudent(self, student):
        if len(self.students) < self.numberOfStudents:
            self.students.append(student)
            print("Student added successfully.")
        else:
            print("College is full.")
    def GetStudent(self, studentId):
        for student in self.students:
            if student.studentId == studentId:
                return student
        return None
    def RemoveStudent(self, studentId):
        student = self.GetStudent(studentId)
        if student is not None:
            self.students.remove(student)
            print("Student removed successfully.")
        else:
            print("Student not found.")
    def __str__(self):
        result = "Students in College:\n"

        for student in self.students:
            result += str(student) + "\n"

        return result
class Student:
    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage
    def __str__(self):
        return (f"Id: {self.studentId}, "
                f"Name: {self.name}, "
                f"Age: {self.age}, "
                f"Percentage: {self.percentage}")

college = College(3)

s1 = Student(101, "Rahul", 20, 75)
s2 = Student(102, "Amit", 21, 82)
s3 = Student(103, "Priya", 20, 68)

college.AddStudent(s1)
college.AddStudent(s2)
college.AddStudent(s3)

print("\n", college)

print("Getting Student with ID 102:")
student = college.GetStudent(102)

if student is not None:
    print(student)
else:
    print("Student not found.")
print("\nRemoving Student with ID 101:")
college.RemoveStudent(101)
print("\n", college)
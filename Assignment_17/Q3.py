class Student:
    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage
    def Accept(self):
        self.studentId = int(input("Enter Student Id: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))
    def Display(self):
        print("Student Id:", self.studentId)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)
    def CalculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        else:
            return "Pass Class"
    def __str__(self):
        return f"{self.studentId} {self.name} {self.age} {self.percentage}"


class MedicalStudent(Student):
    def __init__(self, studentId, name, age, percentage,
                 specialization, marksOfInternship):
        super().__init__(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship
    def Accept(self):
        super().Accept()
        self.specialization = input("Enter Specialization: ")
        self.marksOfInternship = float(input("Enter Marks of Internship: "))
    def Display(self):
        super().Display()
        print("Specialization:", self.specialization)
        print("Marks of Internship:", self.marksOfInternship)
    def CalculateRank(self):
        total = self.percentage + self.marksOfInternship
        if total >= 150:
            return "Excellent"
        elif total >= 120:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        else:
            return "Pass"
    def __str__(self):
        return (f"Student Id: {self.studentId}, "
                f"Name: {self.name}, "
                f"Age: {self.age}, "
                f"Percentage: {self.percentage}, "
                f"Specialization: {self.specialization}, "
                f"Internship Marks: {self.marksOfInternship}, "
                f"Rank: {self.CalculateRank()}")

m1 = MedicalStudent(101, "Priya", 22, 82, "Cardiology", 85)
m1.Display()
print("Rank:", m1.CalculateRank())
print(m1)
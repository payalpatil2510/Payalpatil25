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

class EnggStudent(Student):
    def __init__(self, studentId, name, age, percentage, branch, internalMarks):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks
    def Accept(self):
        super().Accept()
        self.branch = input("Enter Branch: ")
        self.internalMarks = float(input("Enter Internal Marks: "))
    def Display(self):
        super().Display()
        print("Branch:", self.branch)
        print("Internal Marks:", self.internalMarks)
    def CalculateRank(self):
        total = self.percentage + self.internalMarks
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
                f"Branch: {self.branch}, "
                f"Internal Marks: {self.internalMarks}, "
                f"Rank: {self.CalculateRank()}")

e1 = EnggStudent(101, "Amit", 21, 75, "Computer", 80)
e1.Display()
print("Rank:", e1.CalculateRank())
print(e1)
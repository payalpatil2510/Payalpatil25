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
        elif self.percentage >= 40:
            return "Pass Class"
        else:
            return "Fail"
    def __str__(self):
        return (f"Student Id: {self.studentId}, "
                f"Name: {self.name}, "
                f"Age: {self.age}, "
                f"Percentage: {self.percentage}, "
                f"Rank: {self.CalculateRank()}")

s1 = Student(101, "Rahul", 20, 78)
s1.Display()
print("Rank:", s1.CalculateRank())
print(s1)
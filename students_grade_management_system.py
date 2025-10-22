class Student:
    def __init__(self, name):
        self.__name = name
        self.__grades = {}

    def add_grade(self, subject, score):
        if 0 <= score <= 100:
            self.__grades[subject] = score
        else:
            print("Score must be between 0 and 100.")

    def calculate_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def get_info(self):
        avg = self.calculate_average()
        return f"Name: {self.__name}, Average: {avg:.2f}"

student = Student("Ryan")
student.add_grade("Math", 90)
student.add_grade("Science", 80)

print(student.get_info())

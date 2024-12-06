class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'FULL NAME: {self.full_name}, AGE: {self.age}, IS MARRIED: {self.is_married}')



class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = dict(marks)

    def average_rating(self):
        return sum(self.marks.values()) / len(self.marks.values())



class Teacher(Person):
    base_salary = 30000
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def bonus(self):
        print(f'опыт работы: {self.experience}')
        if self.experience > 3:
            ln = self.experience -3
            while ln > 0:
                bonus = self.base_salary * 0.05
                self.base_salary = self.base_salary + bonus
                ln -= 1
        return f"зарплата: {self.base_salary}"




teacher = Teacher('aikokul', 39, False, 3)
teacher.introduce_myself()
print(teacher.bonus())

def create_students():
    student_1 = Student('Said Karimberdiev', 20, False, {'history': 5, 'algebra': 4, 'chemy': 3})
    student_2 = Student('Ernest Mamataliev', 20, False, {'history': 4, 'algebra': 5, 'chemy': 3})
    student_3 = Student('Mukhammad Iskandar uulu', 20, False, {'history': 3, 'algebra': 4, 'chemy': 5})
    students = [student_1, student_2, student_3]
    return students

for student in create_students():
    student.introduce_myself()
    print(student.marks)
    print(student.average_rating())
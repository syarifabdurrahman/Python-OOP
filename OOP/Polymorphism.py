class Student:
    def __init__(self,name,number):
        self.name =name
        self.number = number

    def class_number(self):
        pass


class MaleStudent(Student):
    def __init__(self, name, number):
        Student.__init__(self,name,number)

    def class_number(self):
        print(f"My name is {self.name} and my class number is {self.number}")

class FemaleStudent(Student):
    def __init__(self, name, number):
            Student.__init__(self,name,number)

    def class_number(self):
        print(f"My name is {self.name} and my class number is {self.number}")


if __name__ == "__main__":

    female_student=FemaleStudent("Milly", 15)
    male_student= MaleStudent("Syarif",20)

    students = [female_student,male_student]

    print("\nmenampilkan data")

    for student in students:
        student.class_number()
       

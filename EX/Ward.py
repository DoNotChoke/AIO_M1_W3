class Person:
    def __init__(self, name, yob):
        self.__name = name
        self.__yob = yob

    def describe(self):
        return f"Name: {self.__name} - Yob: {self.__yob}"

    def get_yob(self):
        return self.__yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(f"Student - {super().describe()} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(f"Teacher - {super().describe()} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor - {super().describe()} - Specialist: {self.__specialist}")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list = []

    def add_person(self, p):
        self.__list.append(p)

    def describe(self):
        print(self.__name)
        for p in self.__list:
            p.describe()

    def count_doctor(self):
        cnt = 0
        for p in self.__list:
            if (type(p) is Doctor):
                cnt += 1
        return cnt

    def sort_age(self):
        self.__list.sort(reverse=True, key=Person.get_yob)

    def compute_average(self):
        num_teachers = 0
        su = 0
        for p in self.__list:
            if type(p) is Teacher:
                su += p.get_yob()
                num_teachers += 1
        su /= num_teachers
        return su


student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()
print()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()
print(f"\nNumber of doctors: {ward1.count_doctor()}")
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")

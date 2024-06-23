"""
Module: 1
Week: 3
HW: class
"""


class Person:
    """
    Person class.
    """

    def __init__(self, name: str = "None", yob: int = 0):
        self._name = name
        self._yob = yob

    def describe(self):
        print(f"Name: {self._name}")
        print(f"YoB: {self._yob}")


class Student(Person):
    """
    Student class.
    """

    def __init__(self, name: str = "None", yob: int = 0, grade: str = None):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        super().describe()
        print(f"Grade: {self.grade}")


class Teacher(Person):
    """
    Teacher class.
    """

    def __init__(self, name: str = "None", yob: int = 0, subject: str = None):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        super().describe()
        print(f"Subject: {self.subject}")


class Doctor(Person):
    """
    Doctor class.
    """

    def __init__(self, name: str = "None", yob: int = 0, specialty: str = None):
        super().__init__(name, yob)
        self.specialty = specialty

    def describe(self):
        super().describe()
        print(f"Specialty: {self.specialty}")


class Ward:
    """
    Ward class.
    """

    def __init__(self, name: str = "AIO", people: list = []):
        self._name = name
        self.__people = people

    def add_person(self, person: Person):
        self.__people.append(person)

    def describe(self):
        print(f"Ward name: {self._name}")
        print(f"Total people: {len(self.__people)}")
        for person in self.__people:
            person.describe()
            print()

    def count_doctors(self):
        count = 0
        for person in self.__people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_people(self):
        self.__people.sort(key=lambda x: x.yob)
        return self.__people

    def compute_average(self):
        return sum([person.yob for person in self.__people]) / len(self.__people)


if __name__ == "__main__":
    s1 = Student("Duong", 2010, "Super")

    t1 = Teacher("Nhien", 1995, "CV")
    t2 = Teacher("Cuong", 1975, "RL")

    d1 = Doctor("Vinh", 1969, "AI")
    d2 = Doctor("Dinh Vinh", 1945, "AI")

    w1 = Ward("AIO", [s1, t1, t2, d1])
    w1.add_person(d2)

    # w1.describe()

    print(f"Total doctors: {w1.count_doctors()}")
    print("Sorted people:")
    for person in w1.sort_people():
        person.describe()
        print()

    print(f"Average YoB: {w1.compute_average()}")

class Student:
    number_of_students = 0
    def __init__(self,
                 first_name="",
                 middle_name="",
                 last_name="",
                 year=0,
                 degree="",
                 university=None,
                 email="",
                 tel=None):
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._year = year
        self._degree = degree
        self._university = university
        self._email = email
        self._tel = tel
        Student.number_of_students += 1

    @property
    def year(self):
        return self._year
    
    
#john = Student()

#print(type(john))
#print(type(john._first_name))
#print(john._first_name)

john = Student()
print(Student.number_of_students)
smith = Student()
print(Student.number_of_students)







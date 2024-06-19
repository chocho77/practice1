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
    
    def print_info(self):
        print(
            self._first_name,
            self._middle_name,
            self._last_name,
            self._email,
            self._university
        )
    
    def __str__(self):
        return f"{self._first_name} {self._middle_name} {self._last_name} {self._email} {self._university}"


    @property
    def year(self):
        return self._year
    
    @property
    def tel(self):
        return self._tel
    
    @tel.setter
    def tel(self, value):
        self._tel = value
    
    
#john = Student()

#print(type(john))
#print(type(john._first_name))
#print(john._first_name)

john = Student("John", "Eduard", "Smith", 1977, 'programer', \
               'TU-Varna', 'chavmom@gmail.com', '0889234567')
print(Student.number_of_students)
smith = Student()
print(Student.number_of_students)
john.tel = "0882345678"
print(john.tel)
john.print_info()
print("----------")
print(john)






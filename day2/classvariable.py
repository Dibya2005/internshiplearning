#class variable are shared by all instances of the class
#define outside the constructor
#instace variable are defined inside the constructor
# allow you share data across all instances of the class
class student:
    # class variable
    school = "ABC School"  # shared by all instances of the class
    num_students = 0  # shared by all instances of the class
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
        student.num_students += 1
s1= student("John", 15)
s2= student("Jane", 16)
print(s1.name)  # John
print(s2.name)  # Jane
print(s1.age)   # 15
print(s2.age)   # 16
print(student.school)  # ABC School
print(student.school)  # ABC School # it is a good practiced to acces the class variable using the class name
print(s1.school)  # ABC School not recommended
print(student.num_students)  # 2
print(s1.num_students)  # 2 not recommended
print(f"Total number of students: {student.num_students}")  # Total number of students: 2

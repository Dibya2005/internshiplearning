#class method = alows operations on the class itself rather than on instances of the class
# take (self) as first argument which refers to the class itself
#class method are best for class level data or required to access class itself
class student:
    #class variable
    count=0
    total_gpa=0
    #constructor
    def __init__(self, name, gpa):
        self.name=name
        self.gpa=gpa
        student.count+=1
        student.total_gpa+=gpa
    #instance method
    def info(self):
        return f"{self.name} has a gpa of {self.gpa}"
    #class method
    @classmethod
    def get_count(cls): #it takes cls as first argument which refers to the class itself
        return f"Total number of students: {cls.count}"
    #class method to get the average gpa
    @classmethod  

    def get_average_gpa(cls):
        if cls.count==0:
            return "No students"
        else:
            return f"Average gpa: {cls.total_gpa/cls.count:.2f}"
student.get_count() # this will return Total number of students: 0
s1=student("John", 3.5)
s2=student("Jane", 3.8)
s3=student("Jack", 3.2)
print(student.get_count()) # this will return Total number of students: 3
print(student.get_average_gpa()) # this will return Average gpa: 3.5
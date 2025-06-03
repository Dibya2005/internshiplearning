name="bro code"
age=25
gpa=3.2
is_student=True
print(type(gpa))
gpa= int(gpa)
print(gpa) #floating to int
age=float(age)
print(age)
age=str(age)
#TypeError: can only concatenate str (not "int") to str
print(age)
print(type(age))
#age+=1 #TypeError: can only concatenate str (not "int") to str
age+="1"
print(age)#25.01
name=bool(name)
print(name) #if the string contains qany content it will give true if not gives false

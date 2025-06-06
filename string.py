name=input("enter your name")
r=len(name)
# r1=name.find("i")
#index of the seach
r1=name.rfind("i") # search ele from revese
#if it dont find the seach ele it will give -1
#for make a string capital we use capitalize
# name = name.capitalize() #all letters are string only the first letter is capitallize example we enter bro then it return Bro
name=name.lower() # all letters are in lower case
# name=name.upper() # all letters are in upper case
r2=name.isdigit() #it gives boolean value return true if it contain only digit partial part is digit it return false
r3=name.isalpha() #true if the content contain only alphabate if there is a space then also it retunns false or other things
phonenum=input('enter your phone num')
r4=phonenum.count('-') #count how many - in the phone num
r5= phonenum.replace("-"," ")
print(r5)

print(r)
print(name)
print(r1)
print(help(str)) #know about all str method

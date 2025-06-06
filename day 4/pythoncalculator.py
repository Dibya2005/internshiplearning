op=input("eneter a opetrator (+ - * /)")
num1=float(input("enter the 1st num"))
num2=float(input("enter the 2nd num"))
if op=="+":
  r=num1+num2
  print(round(r,3)) #round(r,3) round the reasult upto 3 decimal place
elif op=="-":
  r=num1-num2
  print(round(r,3))
elif op=="/":
  r=num1/num2
  print(round(r,3))
elif op=="*":
  r=num1*num2;
  print(round(r,3))
else:
  print("enter a valid operator")


 

#validate input
#1. username is no more than 12 chareecter
#2. username doesnot conatain spaces 
# 3. username doesnot contain digit
username= input("enter an username: ")
if len(username) >12 :
  print("udername cant be more than 12 charracter")
elif not username.find(" ")==-1:
  print("your username can't contain spaces")
elif not username.isalpha():
  print("username cant contain number")
else:
  print(f"welcome {username}")
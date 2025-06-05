#exception - an event that interupts the flow of a program
#(zerodicisor err,type err,value err)
#1.try 2.except 3.finally
# try:
#   #trysomecode
# except Exception:
#   #handke an exception
# finally:
#   #do some cleanup
try:
  number=int(input("enter the number-"))
  print(1/number)
except ZeroDivisionError:
  print("you cant divide by zero")
except ValueError:
  print("enter a number-")
except Exception:
  print("somethoing went wrong")
finally:
  print("do some clean up here")
#finaallly will always executes regardless there is exception or not
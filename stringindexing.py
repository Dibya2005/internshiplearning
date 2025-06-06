#accesing ele of a sequece using [] (indeximng operator (start : end :step))
credit_number="1234-5678-9012-3456"
# print(credit_number[0])
# print(credit_number[0:4])
# print(credit_number[5:9])
# print(credit_number[5:])# if we dont declare ending index python understand that you need everything upto the end
# print(credit_number[-1])# if we need last ele 

# #strating index is 0 and ending index is 4
# #using steps
# print(credit_number[::4]) # every 4th charecter
#last 4 digit of a credit card
lastdigit=credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{lastdigit}")
#to revese a string
credit_number=credit_number[::-1]
print(credit_number)
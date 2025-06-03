fruits=["apple","orange","banana","coconut"]
vegitables=["calery","carrot","potatoes"]
meat=["chicken","fish","turkey"]
groceries=[fruits,vegitables,meat]
# print(groceries[0])#return the list of fruits
print(groceries[0][0])#1st ele of 1st list
#if we ever need to iterate over the ele of a 2d list
#you can use nested loops
for collection in groceries:
  for food in collection:
    print(food,end=" ")
  print()
    #you can use any thing tuple in list set in list everything

# #collection = single variable used to store multiple values 
# #list= [] oredered and changable duplicate ok
# # set = {} unordered and immutable , but add remove ok no duplicates
# # tuple = () ordered and unchangable duplicate ok faster
f=["apple","orange","banana","coconut"]
# print(f)
# print(f[0])
# # print(f[4])#index error occur
# print(f[0:2]) #range set it will return fruit in 0 and 1 index
# print(f[::2])#step after every 2 ele
# print(f[::-1])#backward
# #you can iterate over them using for loop
# for x in f:
# #   print(x)
print(dir(f)) # method can use in this list
#print(help(f))
print(len(f))
print("apple" in f)
#f[0]="pineaple"change the ele of A LIST
f.append("grape")#add ele to the end of list
print(f)
f.remove("orange")
# appemnd by index we use insert
f.insert(1,"red r")
f.sort() #it will sort the list in alphabatical order
f.reverse()
print(f)
# f.clear()#clear the list
# print(f)
# return index of a value we use index method
print(f.index('banana')) #if we dont find the ele in list it gives ValueError: 'banana' is not in list
#count the number of time the element occur using count
print(f.count("banana"))

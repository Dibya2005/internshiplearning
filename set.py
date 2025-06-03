# # set = {} unordered and immutable , but add remove ok no duplicates
f={"apple","orange","banana","coconut"}
print(f) # they not print as same order as we input
print(len(f))
print("pineple" in f)
#print(f[0]) #we cant able to do indexing because they are unordered
#we cant change the value of the set
# but we can add or remove value in the set
f.add("pineple")
f.remove("apple")
print(f)
f.pop() #will remove whatever element is first but the list is unordered rendom pop will happen
print(f)
#clear also can be used
#if we have two same value then it print only one as duplicate isnot allowed
#set may work well if you working with constants
#may be color if we want ton find color within a set
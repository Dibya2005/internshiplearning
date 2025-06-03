# # tuple = () ordered and unchangable duplicate ok faster
f=("apple","orange","banana","coconut")
print(f)
print(len(f))
print("pinapple" in f)
print(f.index("apple"))
print(f.count("apple"))
for x in f:
  print(x)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(type(thisset))

thisset.add("orange")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset.discard("thisset")

x = thisset.pop()
print(x)
print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)
x.symmetric_difference_update(y)
print(x)
x.difference(y)
print(x)

z = x.symmetric_difference(y)
print(z)
z = x.intersection(y)
print(y)
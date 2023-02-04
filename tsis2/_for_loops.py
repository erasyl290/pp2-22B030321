fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

for x in fruits:
  if x == "banana":
    break
  print(x)

for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(2, 30, 3):
  print(x)


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

for x in [0, 1, 2]:
  for y in [3, 4, 5]:
    pass
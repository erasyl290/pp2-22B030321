l = list((1, 1, 2, 2, 3))
iterator = iter(l)
m = 1
for i in range(len(l)):
    m *= next(iterator)
print(m)

s = "HeLLo 01$"
j = 0
k = 0
for char in s:
    if ord('A') <= ord(char) <= ord('Z'):
        j += 1
    elif ord('a') <= ord(char) <= ord('z'):
        k += 1
print("Number of upper case letters - {}, lower case letters - {}.".format(j, k))

s = input()
if(tuple(s) == tuple(reversed(s))):
    print("Your word is a palindrome.")
else:
    print("Your word is not a palindrome.")



t = tuple((1, 1, 1, 1))
print(all(t))
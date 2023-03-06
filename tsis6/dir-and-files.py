import os
from shutil import copyfile

print()
print(os.listdir('../'), end='\n\n')
print(list(os.walk('../tsis4')), end='\n\n')

print(os.path.abspath('.'))
print("Existence: ", os.access('.', os.F_OK))
print("Readability: ", os.access('.', os.R_OK))
print("Writability: ", os.access('.', os.W_OK))
print("Executability: ", os.access('.', os.X_OK))
print()

p = os.getcwd()
print(os.path.exists(p))
print("File name: ", os.path.basename(p))
print("Dir name: ", os.path.dirname(p))
print()

with open('dir-and-files.py', 'r') as f:
    print("Number of lines: ", len(f.readlines()))

with open('file.txt', 'w') as f:
    f.writelines(['a', 'b', 'c'])

for i in range(26):
    j = chr(ord('A') + i)
    open(f"{j}.txt", 'x')
    os.remove(f"{j}.txt")

copyfile("file.txt", "another_file.txt")

p = os.path.abspath('another_file.txt')
if(os.access(p, os.F_OK)):
    os.remove(p)
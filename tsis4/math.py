import math

radians = math.radians(int(input("Input degree: ")))
print(f"In radians is: {radians}\n")

h = int(input("Trapezoid's height: "))
b1 = int(input("First base: "))
b2 = int(input("Second base: "))
print("Trapezoid's area: {}\n".format(h * (b1+b2)/2))

sides = int(input("Number of regular polygon's sides: "))
side_len = int(input("Length of a side: "))
polygon_area = sides*pow(side_len, 2) / (4*math.tan(math.pi/sides))
print("Polygon's area: {}\n".format(int(polygon_area)))

base_len = int(input("Length of parallelogram's base: "))
height = int(input("Parallelogram's height: "))
print("Parallelogram's area: {}\n".format(base_len*height))
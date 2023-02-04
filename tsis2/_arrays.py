cars = ["Ford", "Volvo", "BMW"]

x = cars[0]
print(x)

x = len(cars)
print(x)

cars[0] = "Toyota"
cars.append("Honda")
cars.pop(1)
cars.remove("Volvo")
for x in cars:
    print(x)
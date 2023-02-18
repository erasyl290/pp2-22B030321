class String:
    def getString():
        global s
        s = str(input())
        return s

    def printString():
        print(s.upper())

class Shape:
    def area():
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.l = length
    
    def area():
        print(self.l * self.l)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.l = length
        self.w = width
    
    def area():
        return self.l * self.w

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5
    



class Account:
    def __init__(self, owner, balance):
        self.o = owner
        self.b = balance
    
    d = 0
    def deposit(self, count):
        if(self.b - count >= 0):
            self.b -= count
            self.d += count
            print(f"{self.o}'s balance now {self.b} KZT. ({self.d} in the deposit)\n")
        else: print(f"There is not enough money in {self.o}'s bank ({self.b} KZT)\n")
    
    def withdraw(self, count):
        if(self.b - count >= 0):
            self.b -= count
            print(f"{self.o}'s balance now {self.b} KZT. ({count} taken)\n")
        else: print(f"There is not enough money in {self.o}'s bank ({self.b} KZT)\n")

acc1 = Account("Yerasyl Baimukhan", 10000)
acc1.deposit(2500)
acc1.deposit(2500)
acc1.withdraw(2500)
acc1.deposit(2501)
acc1.withdraw(2500)
acc1.withdraw(1)
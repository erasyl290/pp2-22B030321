class Square_to:
    def __init__(self, N):
        self.N = N
        self.n = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if (self.n + 1) ** 2 < self.N:
            self.n += 1
            return self.n*self.n
        raise StopIteration()
    
class Even_to:
    def __init__(self, n):
        self.n = n
        self.even = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.even + 2 < self.n:
            self.even += 2
            return self.even
        raise StopIteration
    
class down_from:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.n > 0:
            self.n -= 1
            return self.n
        raise StopIteration
    
def divby3_4(n):
    num = 3
    while num < n:
        if num % 3 == 0 or num % 4 == 0:
            yield num
        num += 1

def squares(a, b):
    while a <= b:
        yield a*a
        a += 1

print(list(Square_to(15)))




print()

n = int(input())
even_list = list(Even_to(n))
for i in range(len(even_list)-2):
    print(even_list[i], end=', ')
print(even_list[len(even_list)-1])

print(list(divby3_4(n)))

print()




for i in squares(6, 10):
    print(i, end= ' ')
print()

print(list(down_from(10)))
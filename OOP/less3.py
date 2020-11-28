class Rectangle:
    x = 1
    y = 1
    a = 5
    b = 7
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

r2 = Rectangle(1,1,2,2)
print(r2.x, r2.y, r2.a, r2.b)
# r1 = Rectangle()
# r1.x = 2
# r1.y = 4
# r1.a = 6
# r1.b = 8
# print(r1.x, ';', r1.y, ';', r1.a, ';',  r1.b)
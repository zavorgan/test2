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
    def __str__(self):
        return "Прямоугольник с координатами (" + str(self.x) +  " ; " + str(self.y) + ") шириной " + str(self.a) +  " и высотой " + str(self.b)
    def area(self):
        return self.a * self.b
    def pl(self):
        return (self.a + self.b) * 2

r2 = Rectangle(1,1,19,22)
print(r2.x, r2.y, r2.a, r2.b)
print(r2)
print(r2.area())
print(r2.pl())
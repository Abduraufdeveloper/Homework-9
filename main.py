import math

class Radius :
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimetr(self):
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    radius = float(input("Sonni kiriting : "))
    b = Radius(radius)
    print("radius :", Radius.area())
    print("perimetr :", Radius.perimetr())
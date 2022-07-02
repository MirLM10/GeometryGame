from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def inRectangle(self, rec):
        if (rec.point1.x < self.x < rec.point2.x) and (rec.point1.y < self.y < rec.point2.y):
            return True

        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def drawRectangle(self, draw):
        draw.penup()
        draw.goto(self.point1.x, self.point1.y)
        draw.pendown()
        draw.forward(self.point2.x - self.point1.x)
        draw.left(90)
        draw.forward(self.point2.y - self.point1.y)
        draw.left(90)
        draw.forward(self.point2.x - self.point1.x)
        draw.left(90)
        draw.forward(self.point2.y - self.point1.y)
        draw.penup()


class GuiPoint(Point):

    def drawPoint(self, draw, size=5, color='red'):
        draw.penup()
        draw.goto(self.x, self.y)
        draw.pendown()
        draw.dot(size, color)


rectangle = GuiRectangle(Point(randint(0, 100), randint(0, 100)), Point(randint(100, 200), randint(100, 200)))
print(f"Rectangle coordinates: ({rectangle.point1.x}, {rectangle.point1.y}) and ({rectangle.point2.x}, {rectangle.point2.y})")
userPoint = Point(int(input("Guess the x-coordinate of the rectangle: ")), int(input("Guess the y-coordinate of the rectangle: ")))
print(f"Is your point inside the rectangle? {userPoint.inRectangle(rectangle)}")
userArea = int(input("Guess the area of the rectangle: "))
print(f"Does your area match? {userArea == rectangle.area()}")
print(f"Your area is off by: {rectangle.area() - userArea} sq.units")
canvas = turtle.Turtle()
rectangle.drawRectangle(canvas)
point = GuiPoint(userPoint.x, userPoint.y)
point.drawPoint(canvas)
turtle.done()

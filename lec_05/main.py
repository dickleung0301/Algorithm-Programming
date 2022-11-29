from shape import Shape
from circle import Circle
from triangle import Triangle
from square import Square
from point import Point
import math


def create_shapes() -> list[Shape]:
    # create points
    p1 = Point(5.1, -8.6)
    p2 = Point(17.3, 9.5)
    p3 = Point(-4.2, 10.0)

    # using points to create one of each shapes
    circle = Circle(p1, 3)
    triangle = Triangle(p2, 5)
    square = Square(p3, 2)

    # create list of type shape
    shapesList: list[Shape] = [circle, triangle, square]
    return shapesList


def manage_shapes(shapes: list[Shape]) -> None:
    # prints information of all objects in list
    print("Print information about shapes:")
    for shape in shapes:
        print(f'{shape} has an area of {shape.calculate_area()}')

    # moves circle to (0|0) and sets radius to 2
    p4 = Point(0.0, 0.0)
    shapes[0].move_to(p4)
    shapes[0].scale(2.0)

    # prints all information again to check if previous worked
    print("Print information about shapes:")
    for shape in shapes:
        print(f'{shape} has an area of {shape.calculate_area()}')


if __name__ == "__main__":
    shapes = create_shapes()
    manage_shapes(shapes)

import math
from point import Point
from shape import Shape

class Circle(Shape):
    # constructor
    def __init__(self, center: Point, radius: int) -> None:
        super().__init__(center)
        self.__radius = radius
    # class functions
    def scale(self, scaling_factor: float) -> None:
        self.__radius = scaling_factor
    
    def calculate_area(self) -> float:
        return (math.pi * (self.__radius**2))

    def __str__(self) -> str:
        return "x: {}, y: {}, radius: {}, area: {}".format(
            self.get_x(),
            self.get_y(),
            self.__radius,
            self.calculate_area(),
        )   
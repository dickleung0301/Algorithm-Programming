import math
from point import Point
from shape import Shape

class Triangle(Shape):
    # constructor
    def __init__(self, center: Point, side_length: int) -> None:
        super().__init__(center)
        self.__side_length = side_length
    # class functions
    def scale(self, scaling_factor: float) -> None:
        self.__side_length = scaling_factor
    
    def calculate_area(self) -> float:
        return (math.sqrt(3) * (self.__side_length**2) / 4)

    def __str__(self) -> str:
        return "x: {}, y: {}, side length: {}, area: {}".format(
            self.get_x(),
            self.get_y(),
            self.__side_length,
            self.calculate_area(),        
        )
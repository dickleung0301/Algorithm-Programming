from point import Point

class Square(Point):
    # constructor
    def __init__(self, center: Point, side_length: float) -> None:
        super().__init__(center.get_x(),center.get_y())
        self.__side_length = side_length
    # class functions 
    def scale(self, scaling_factor: float) -> None:
        self.__side_length = scaling_factor

    def calculate_area(self) -> float:
        return self.__side_length**2
        
    def __str__(self) -> str:
        return "x: {}, y: {}, side length: {}, area:{}".format(
            self.get_x(),
            self.get_y(),
            self.__side_length,
            self.calculate_area(),
        )
from abc import ABC, abstractmethod
from point import Point

class Shape(Point):
    # constructor
    def __init__(self, center: Point) -> None:
        super().__init__(center.get_x(), center.get_y())
    # class function
    def move_to(self, new_center: Point) -> None:
        self.__x = new_center.get_x()
        self.__y = new_center.get_y()
    # virtual functions
    @abstractmethod
    def scale(self, scaling_factor: float) -> None:
        raise NotImplementedError
    @abstractmethod
    def calculate_area(self) -> float:
        raise NotImplementedError
    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
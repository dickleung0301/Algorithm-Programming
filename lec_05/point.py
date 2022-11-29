class Point:
    # constructor
    def __init__(self, x: float, y: float) -> None:
        self.__x = x
        self.__y = y
    # acessor of x
    def get_x(self) -> float:
        return self.__x
    # acessor of y
    def get_y(self) -> float:
        return self.__y
    # calculate distance
    def distance_to(self, other: 'Point') -> float:
        return ((other.get_x() - self.get_x())**2 + (other.get_y() - self.get_y())**2)
    # return statement
    def __str__(self) -> str:
        return "x: {}, y: {}".format(
            self.get_x(),
            self.get_y(),
        )
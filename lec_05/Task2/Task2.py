import math
from point import Point
from circle import Circle
from square import Square

if __name__ == "__main__":
    A = Point(1.0,2.0)
    B = Point(-1.0,-2.0)
    print(A)
    print(B)
    print(A.distance_to(B))
    C = Circle(A, 3)
    print(C)
    C.scale(2)
    print(C)
    S = Square(B, 3)
    print(S)
    S.scale(2)
    print(S)
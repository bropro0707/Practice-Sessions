import math


class Polygon:
    def __init__(self, points):
        self.points = points

    def distance(self, point_a, point_b):
        return math.dist(point_a, point_b)

    def perimeter(self):
        if len(self.points) < 2:
            return 0.0

        total = 0.0
        for index in range(len(self.points)):
            current = self.points[index]
            next_point = self.points[(index + 1) % len(self.points)]
            total += self.distance(current, next_point)

        return total


class Square(Polygon):
    def __init__(self):
        super().__init__([(1, 1), (1, 2), (2, 2), (2, 1)])


def main():
    square = Square()
    print(f"Perimeter: {square.perimeter():.2f}")


if __name__ == "__main__":
    main()

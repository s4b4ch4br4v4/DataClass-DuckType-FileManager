import math

class Point:
    """A simple point class with operations"""
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y

    def sum(self, other):
        return Point(self.get_x + other.get_x, self.get_y + other.get_y)

    def difference(self, other):
        return Point(self.get_x - other.get_x, self.get_y - other.get_y)

    def scalar_multiplication(self, other):
        return self.get_x * other.get_x + self.get_y * other.get_y

    def euclidean_distance(self, other):
        return math.sqrt((self.get_x - other.get_x) ** 2 + (self.get_y - other.get_y) ** 2)

    def round_point(self):
        return Point(abs(self.get_x), abs(self.get_y))

    def __repr__(self):
        return f"Point({self.get_x}; {self.get_y})"


class LinearInterpolator:
    """Linear Interpolation, Lerp gives evenly distributed numbers between two other numbers."""
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @property
    def get_start(self):
        return self.__start

    @property
    def get_end(self):
        return self.__end

    def lerp(self, t):
        """Interpolates between start and end based on t (0 <= t <= 1)."""
        return self.get_start * (1.0 - t) + self.get_end * t


class PointInterpolator:
    """Linear Interpolation(Lerp) but it can now work with points."""
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @property
    def get_start(self):
        return self.__start

    @property
    def get_end(self):
        return self.__end

    def lerp_point(self, t):
        x = LinearInterpolator(self.get_start.get_x, self.get_end.get_x).lerp(t)
        y = LinearInterpolator(self.get_start.get_y, self.get_end.get_y).lerp(t)

        return Point(x, y)

    def segmentation(self, segments):
        """Manage segments to segment the distance evenly between points."""
        if segments <= 0:
            try:
                raise ValueError("The number of segments must be greater than zero.")
            except ValueError as e:
                print(f"Caught error: {e}")
                exit()

        points = []
        for step in range(segments + 1):
            t = step / segments
            points.append(self.lerp_point(t))

        return points


def main():
    P0 = Point(0, 0)
    P1 = Point(5, 5)
    points = PointInterpolator(P0, P1).segmentation(10)
    for point in points:
        print(point.__repr__())


if __name__ == "__main__":
    main()

import math


class QuadraticEquation:
    """A simple quadratic equation class."""
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def get_a(self):
        return self.__a

    @property
    def get_b(self):
        return self.__b

    @property
    def get_c(self):
        return self.__c

    def discriminant(self):
        return self.get_b ** 2 - 4 * self.get_a * self.get_c

    def solve(self):
        discriminant = self.discriminant()
        # If the discriminant is negative, the equation has complex roots
        if discriminant < 0:
            raise ValueError("Discriminant must be greater than or equal to zero.")
        first_root = (-self.get_b + math.sqrt(discriminant)) / (2 * self.get_a)
        second_root = (-self.get_b - math.sqrt(discriminant)) / (2 * self.get_a)
        return first_root, second_root

    def root_representation(self):
        """Helper method to represent roots."""
        if self.discriminant() == 0:
            first_root = self.solve()[0]
            return f"x1, x2 = {first_root}"
        elif self.discriminant() < 0:
            return "The roots are complex numbers."
        else:
            first_root, second_root = self.solve()
            return f"x1 = {first_root}, x2 = {second_root}"

    def __repr__(self):
        equation = f"{self.get_a} * x^2 + {self.get_b} * x + {self.get_c}"
        return f"{equation}\nD = {self.discriminant()}\n{self.root_representation()}"


class ComplexQuadraticEquation(QuadraticEquation):
    """A simple quadratic equation class which can work with complex numbers"""
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def real_part(self):
        return -super().get_b / (2 * super().get_a)

    def imaginary_part(self):
        return math.sqrt(abs(super().discriminant()) / (2 * super().get_a))

    def solve(self):
        if super().discriminant() < 0:
            first_root = f"{self.real_part()} + {self.imaginary_part()} * i"
            second_root = f"{self.real_part()} - {self.imaginary_part()} * i"
            return first_root, second_root
        return super().solve()

    def root_representation(self):
        if self.discriminant() < 0:
            first_root, second_root = self.solve()
            return f"x1 = {first_root}, x2 = {second_root}"
        else:
            return super().root_representation()


def main():
    quadratic_equation = ComplexQuadraticEquation(1, 22, 4)
    print(quadratic_equation)


if __name__ == "__main__":
    main()

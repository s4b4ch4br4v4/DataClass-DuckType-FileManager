class Point:
    __match_args__ = ('x', 'y')

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


def sum_numbers(*args):
    """k"""
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg

    return total


def merge_dict(**kwargs):
    local_dict = {}
    for kwarg, value in kwargs.items():
        lower_kwarg = kwarg.lower()
        if lower_kwarg not in local_dict:
            local_dict[lower_kwarg] = value
        else:
            local_dict[f"{lower_kwarg}_duplicate"] = value

    return local_dict


def main():
    p0 = Point()

    match p0:
        case Point(x, y) if x == y:
            print(f"{x}, {y}")
        case _:
            print(p0)

    print(sum_numbers(1, 2, '2'))

    print(merge_dict(name="Saba", age=20, condition="Pizdec"))


if __name__ == '__main__':
    main()

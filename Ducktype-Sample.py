class Product:
    """A simple class which represents a product."""
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def get_price(self):
        return self._price


class Service:
    """Another even simpler class representing some service."""
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def get_price(self):
        return self._price


def calculate_total(list_of_things):
    total_price = 0
    for thing in list_of_things:
        total_price += thing.get_price
    return total_price


def main():
    my_product = Product("Apple", 5)
    my_service = Service("Massage", 50)
    total_price = calculate_total([my_product, my_service])
    print(total_price)


if __name__ == "__main__":
    main()

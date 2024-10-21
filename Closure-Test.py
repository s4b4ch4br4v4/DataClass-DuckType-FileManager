def create_adder(x):
    def adder(y):
        print(x)
        return x + y

    return adder


def main():
    add_15 = create_adder(15)
    print(add_15.__closure__[0])


if __name__ == "__main__":
    main()

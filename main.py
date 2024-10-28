
def main():
    my_range = range(3).__iter__()
    print(my_range.__next__())
    print(my_range.__next__())
    print(my_range.__next__())

    for n in range(2, 1000):
        divisors = []
        for x in range(1, n):
            if n % x == 0:
                divisors.append(x)

        if sum(divisors) == n:
            print(f"{n} = {divisors}")


if __name__ == '__main__':
    main()


class myRange:

    """A simple class that represents a range of numbers.

    Supports both increasing and decreasing sequences based on the step value.
    The step must be non-zero, and positive or negative step determines the direction.
    """

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise ValueError("Step must be non-zero.")

        self._start = start
        self._stop = stop
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        current = self._start
        if self._step < 0:
            if self._start <= self._stop:
                raise StopIteration
            self._start += self._step
            return current
        else:
            if self._start >= self._stop:
                raise StopIteration
            self._start += self._step
            return current


def main():
    myIter = myRange(0, 10, -1)
    for i in myIter:
        print(i)


if __name__ == "__main__":
    main()

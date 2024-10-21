from dataclasses import dataclass


@dataclass
class Employee:
    """A simple structure for a regular employee."""
    name: str
    surname: str
    department: str
    salary: int


class Office:
    """An office class which can work with the Employee structure."""
    def __init__(self, num_of_employees, location):
        self._num_of_employees = num_of_employees
        self._location = location
        self._employees = []

    @property
    def num_of_employees(self):
        return self._num_of_employees

    @property
    def employees(self):
        return self._employees

    @employees.setter
    def employees(self, employee):
        if len(self._employees) < self.num_of_employees:
            self._employees.append(employee)
        else:
            raise ValueError("There is no space left for more employees.")


def main():
    first_employee = Employee("Giorgi", "Tedoradze", "Back-End", 2000)
    second_employee = Employee("Davit", "Tedoradze", "Front-End", 2000)

    the_office = Office(5, "Somewhere")

    the_office.employees = first_employee
    the_office.employees = second_employee

    print(the_office.employees)


if __name__ == '__main__':
    main()

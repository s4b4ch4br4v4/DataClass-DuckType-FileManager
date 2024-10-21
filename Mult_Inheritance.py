
class Engine:
    def __init__(self, engine_type):
        if not isinstance(engine_type, str):
            raise ValueError("Engine type must be a string.")
        self.__engine_type = engine_type

    @property
    def get_engine_type(self):
        return self.__engine_type

    @staticmethod
    def start_engine():
        return "Engine started."


class Wheels:
    def __init__(self, num_wheels):
        if not isinstance(num_wheels, int):
            raise ValueError("Number of wheels must be an integer.")
        self.__num_wheels = num_wheels

    @property
    def get_num_wheels(self):
        return self.__num_wheels

    def move(self):
        return f"Moving with {self.get_num_wheels} wheels."


class Vehicle(Engine, Wheels):
    def __init__(self, vehicle_name, engine_type, num_wheels):
        Engine.__init__(self, engine_type)
        Wheels.__init__(self, num_wheels)
        if not isinstance(vehicle_name, str):
            raise ValueError("Vehicle name must be a string.")
        self.__vehicle_name = vehicle_name

    @property
    def get_vehicle_name(self):
        return self.__vehicle_name

    def drive(self):
        return super().start_engine(), super().move()


class Car(Vehicle):
    """A simple car class"""
    def __init__(self, car_model, vehicle_name, engine_type, num_wheels):
        super().__init__(vehicle_name, engine_type, num_wheels)
        if not isinstance(car_model, str):
            raise ValueError("Car model must be string.")
        self.__car_model = car_model

    @property
    def get_car_model(self):
        return self.__car_model


def main():
    car_instance = Car("Pony", "Pinky", "Tornado", 4)
    print(car_instance.drive())


if __name__ == "__main__":
    main()





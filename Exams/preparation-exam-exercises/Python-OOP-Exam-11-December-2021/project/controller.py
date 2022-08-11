from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in ["MuscleCar", "SportsCar"]:
            return

        if model in [c.model for c in self.cars]:
            raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar":
            self.cars.append(MuscleCar(model, speed_limit))

        if car_type == "SportsCar":
            self.cars.append(SportsCar(model, speed_limit))

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [d.name for d in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [r.name for r in self.races]:
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created!"

    def __find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        return None

    def __find_car_by_type(self, car_type):
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and car.is_taken == False:
                return car
        return None

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__find_car_by_type(car_type)

        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if car.is_taken == False and driver.car is not None:
            message = f"Driver {driver_name} changed his car from {driver.car.model} to {car.model}."
            driver.car.is_taken = False
            driver.car = car
            car.is_taken = True
            return message

        if driver.car is None and car.is_taken == False:
            message = f"Driver {driver_name} chose the car {car.model}."
            driver.car = car
            car.is_taken = True
            return message

    def __find_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        return None

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race: Race = self.__find_race_by_name(race_name)
        driver = self.__find_driver_by_name(driver_name)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if driver is None:
            raise Exception(f"Driver {driver} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        if driver.car is not None:
            race.drivers.append(driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race: Race = self.__find_race_by_name(race_name)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result = ""

        sort = sorted(race.drivers, key=lambda x: -x.car.speed_limit)
        for index in range(3):
            current_driver = sort[index]
            current_driver.number_of_wins += 1
            result += f"Driver {current_driver.name} wins the {race_name} race with a speed of {current_driver.car.speed_limit}." + "\n"

        return result.strip()

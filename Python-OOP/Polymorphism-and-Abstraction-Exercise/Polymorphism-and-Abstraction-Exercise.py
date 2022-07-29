from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def drive(self, distance):
        fn = distance * (self.fuel_consumption + 0.9)
        if self.fuel_quantity >= fn:
            self.fuel_quantity -= fn

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def drive(self, distance):
        fn = distance * (self.fuel_consumption + 1.6)
        if self.fuel_quantity >= fn:
            self.fuel_quantity -= fn

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel

# ---------------------------------------------------------------------------------


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __str__(self):
        return f"Group {self.name} with members {', '.join([str(p) for p in self.people])}"

    def __getitem__(self, item):
        return f"Person {item}: {str(self.people[item])}"


# ---------------------------------------------------------------------------------



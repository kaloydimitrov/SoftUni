from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.capacity = capacity
        self.name = name
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        if self.__class__.__name__ != fish.__class__.__name__:
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]

    def __str__(self):
        if not self.fish:
            return "none"

        result = f"{self.name}:" + "\n"
        fish_names = [f.name for f in self.fish]
        result += f"Fish: {' '.join(fish_names)}" + "\n"
        result += f"Decorations: {len(self.decorations)}" + "\n"
        result += f"Comfort: {self.calculate_comfort()}"

        return result

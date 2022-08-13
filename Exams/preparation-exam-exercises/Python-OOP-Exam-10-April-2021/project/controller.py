from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."

        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
        if aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."

        if decoration_type == "Ornament":
            self.decorations_repository.decorations.append(Ornament())
        if decoration_type == "Plant":
            self.decorations_repository.decorations.append(Plant())

        return f"Successfully added {decoration_type}."

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium_name
        return None

    def __find_decoration_by_type(self, decoration_type):
        for decoration in self.decorations_repository.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration
        return None

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium: BaseAquarium = self.__find_aquarium_by_name(aquarium_name)
        decoration = self.__find_decoration_by_type(decoration_type)

        if decoration is None:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium.add_decoration(decoration)
        self.decorations_repository.decorations.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium: BaseAquarium = self.__find_aquarium_by_name(aquarium_name)

        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."

        fish = None
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        if fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)

        aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name):
        aquarium: BaseAquarium = self.__find_aquarium_by_name(aquarium_name)

        aquarium.feed()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium: BaseAquarium = self.__find_aquarium_by_name(aquarium_name)
        value = sum(d.price for d in aquarium.decorations) + sum(f.price for f in aquarium.fish)

        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium) + "\n"

        return result.strip()

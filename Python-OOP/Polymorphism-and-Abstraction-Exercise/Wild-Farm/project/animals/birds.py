from project.animals.animal import Bird


class Owl(Bird):
    FOODS = ["Meat"]
    WEIGHT_TO_ADD = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    FOODS = ["Fruit", "Meat", "Vegetable", "Seed"]
    WEIGHT_TO_ADD = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

from project.animal import Animal


class Cat(Animal):
    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} Cat"

    def make_sound(self):
        return "Meow meow!"


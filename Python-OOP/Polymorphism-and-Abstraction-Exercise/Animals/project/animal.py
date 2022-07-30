from abc import ABC, abstractmethod


class Animal:
    def __init__(self, name, age, gender):
        self.gender = gender
        self.name = name
        self.age = age

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

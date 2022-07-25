class Customer:
    def __init__(self, name, age, id):
        self.id = id
        self.name = name
        self.age = age
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join([dvd.name for dvd in self.rented_dvds])})"

from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super().__init__(name, 25)


b = SaltwaterAquarium("Name")

d = SaltwaterAquarium(1)
d2 = SaltwaterAquarium(1)
d3 = SaltwaterAquarium(1)
b.add_decoration(d)
b.add_decoration(d2)
b.add_decoration(d3)

print(b.calculate_comfort())


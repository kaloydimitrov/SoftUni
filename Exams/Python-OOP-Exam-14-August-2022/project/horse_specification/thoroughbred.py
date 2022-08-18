from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return 140

    def train(self):
        horse_speed = self.speed

        if horse_speed + 3 > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += 3

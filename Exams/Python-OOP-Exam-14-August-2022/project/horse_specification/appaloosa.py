from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return 120

    def train(self):
        horse_speed = self.speed

        if horse_speed + 2 > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += 2

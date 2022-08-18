from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return

        horse = None
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
        if horse_type == "Thoroughbred":
            horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None

    def __find_horse_by_type(self, horse_type):
        for index in range(len(self.horses) - 1, -1, -1):
            current_horse: Horse = self.horses[index]
            if current_horse.__class__.__name__ == horse_type and not current_horse.is_taken:
                return self.horses[index]
        return None

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey: Jockey = self.__find_jockey_by_name(jockey_name)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse: Horse = self.__find_horse_by_type(horse_type)

        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if not horse.is_taken and jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def __find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race: HorseRace = self.__find_race_by_type(race_type)

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        jockey: Jockey = self.__find_jockey_by_name(jockey_name)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race: HorseRace = self.__find_race_by_type(race_type)

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        sort = sorted(race.jockeys, key=lambda x: -x.horse.speed)
        winner: Jockey = sort[0]

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

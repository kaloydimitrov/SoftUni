from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player)
        return f"Successfully added: {', '.join([p.name for p in added_players])}"

    def add_supply(self, *supplies):
        [self.supplies.append(s) for s in supplies]

    def find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def find_supply_by_sustenance_type(self, sustenance_type, supplies):
        for index in range(len(supplies)):
            if supplies[index].__class__.__name__ == sustenance_type:
                return index

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.find_player_by_name(player_name)

        if player is None:
            return
        if sustenance_type not in ["Food", "Drink"]:
            return

        supplies = self.supplies[::-1]
        supply_index = self.find_supply_by_sustenance_type(sustenance_type, supplies)

        if supply_index is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        player.stamina = min(player.stamina + supplies[supply_index].energy, 100)
        supplies.pop(supply_index)
        self.supplies = supplies[::-1]

        if player.stamina > 100:
            player.stamina = 100

        return f"{player.name} sustained successfully with {supplies[supply_index].name}."

    @staticmethod
    def duel_attack(p1, p2):
        p1_attack_value = p1.stamina / 2
        p2.stamina = max(p2.stamina - p1_attack_value, 0)
        if p2.stamina <= 0:
            p2.stamina = 0
            return f"Winner: {p1.name}"

        p2_attack_value = p2.stamina / 2
        p1.stamina = max(p1.stamina - p2_attack_value, 0)
        if p1.stamina <= 0:
            p1.stamina = 0
            return f"Winner: {p2.name}"

        if p1.stamina > p2.stamina:
            return f"Winner: {p1.name}"
        else:
            return f"Winner: {p2.name}"

    def duel(self, first_player_name: str, second_player_name: str):
        player_one: Player = self.find_player_by_name(first_player_name)
        player_two: Player = self.find_player_by_name(second_player_name)

        if player_one.stamina == 0 and player_two.stamina == 0:
            return f"Player {player_one.name} does not have enough stamina.\nPlayer {player_two.name} does not have enough stamina."
        if player_one.stamina == 0:
            return f"Player {player_one.name} does not have enough stamina."
        if player_two.stamina == 0:
            return f"Player {player_two.stamina} does not have enough stamina."

        if player_one.stamina < player_two.stamina:
            return self.duel_attack(player_one, player_two)
        if player_two.stamina < player_one.stamina:
            return self.duel_attack(player_two, player_one)

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""

        for player in self.players:
            result += str(player) + "\n"

        for supply in self.supplies:
            result += supply.details() + "\n"

        return result.strip()

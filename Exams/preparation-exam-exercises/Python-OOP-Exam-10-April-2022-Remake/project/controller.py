from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return None

    def __find_last_supply_by_type(self, sustenance_type):
        for index in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[index].__class__.__name__ == sustenance_type:
                return index
        return None

    def sustain(self, player_name: str, sustenance_type: str):
        player: Player = self.__find_player_by_name(player_name)

        if player is None:
            return

        if sustenance_type not in ["Food", "Drink"]:
            return

        supply_index = self.__find_last_supply_by_type(sustenance_type)
        supply: Supply = self.supplies[supply_index]

        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        player_stamina = player.stamina
        supply_energy = supply.energy

        if player_stamina + supply_energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy

        self.supplies.pop(supply_index)

        return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def duel_attack(first, second):
        second_stamina = second.stamina
        reduce_value = first.stamina / 2

        if second_stamina - reduce_value <= 0:
            second.stamina = 0
            return f"Winner: {first.name}"
        else:
            second.stamina -= reduce_value

        first_stamina = first.stamina
        reduce_value = second.stamina / 2

        if first_stamina - reduce_value <= 0:
            first.stamina = 0
            return f"Winner: {second.name}"
        else:
            first.stamina -= reduce_value

        if first.stamina > second.stamina:
            return f"Winner: {first.name}"
        else:
            return f"Winner: {second.name}"

    def duel(self, first_player_name: str, second_player_name: str):
        first_player: Player = self.__find_player_by_name(first_player_name)
        second_player: Player = self.__find_player_by_name(second_player_name)

        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina." + "\n" + f"Player {second_player.name} does not have enough stamina."

        if first_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina."
        if second_player.stamina == 0:
            return f"Player {second_player.name} does not have enough stamina."

        if first_player.stamina < second_player.stamina:
            return self.duel_attack(first_player, second_player)
        else:
            return self.duel_attack(second_player, first_player)

    def next_day(self):
        for player in self.players:
            player_stamina = player.stamina
            reduce_value = player.age * 2

            if player_stamina - reduce_value < 0:
                player.stamina = 0
            else:
                player.stamina -= reduce_value

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for player in self.players:
            result += str(player) + "\n"

        for supply in self.supplies:
            result += supply.details() + "\n"

        return result.strip()

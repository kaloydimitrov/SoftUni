from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.__name in [x.__name for x in self.pokemons]:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.__name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        if pokemon_name not in [x.__name for x in self.pokemons]:
            return "Pokemon is not caught"
        for pokemon in self.pokemons:
            if pokemon.__name == pokemon_name:
                self.pokemons.remove(pokemon)
                break
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"
        for name_health in self.pokemons:
            result += f"\n- {name_health.__name} with health {name_health.health}"

        return result

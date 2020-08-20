class Pokemon:
    def __init__(self, name, type, level):

        # saving variables as attributes
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_knocked_out = False

    def __repr__(self):

        # Pokemon information
        return "-----Pokemons----- \nNAME/ {name} \nTYPE/ {type} \nLVL/ {level} \nHEALTH/ {health}".format(level=self.level, name=self.name, health=self.health, type=self.type)

    def revive(self):
        self.is_knocked_out = False

        # A revived pokemon cant have 0 health
        if self.health == 0:
            self.health = 1
        print("{name} was revived".format(name=self.name))

        # KO function
    def knock_out(self):
        self.is_knocked_out = True
        if self.health != 0:
            self.health = 0
        print("{name} was knocked out!".format(name=self.name))

        # Losing health function
    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.knock_out()
        else:
            print("{name} now has {health} health.".format(
                name=self.name, health=self.health))

        # Gaining health function
    def gain_health(self, amount):
        if self.health == 0:
            self.revive()
        self.health += amount
        if self.health >= self.max_health:
            self.health = self.max_health
        print("{name} now has {health} health.".format(
            name=self.name, health=self.health))

        # Creating attack function
    def attack(self, other_pokemon):
        if self.is_knocked_out:
            print("{name} can't attack because it is knocked out!".format(
                name=self.name))
            return

        version = ["Fire", "Water", "Grass"]

        for i, k in enumerate(version):
            if self.type == k:
                # other_pokemon is STRONG
                if other_pokemon.type == version[(i+1) % 3]:
                    print("{my_name} attacked {other_name} for {damage} damage.".format(
                        my_name=self.name, other_name=other_pokemon.name, damage=round(self.level * 0.5)))
                    print("It's not very effective")
                    other_pokemon.lose_health(round(self.level * 0.5))
                    # both are same type
                if other_pokemon.type == k:
                    print("{my_name} attacked {other_name} for {damage} damage.".format(
                        my_name=self.name, other_name=other_pokemon.name, damage=self.level))
                    other_pokemon.lose_health(self.level)
                    print("It's not very effective")
                    # other_pokemon is WEAK
                if other_pokemon.type == version[(i+2) % 3]:
                    print("{my_name} attacked {other_name} for {damage} damage.".format(
                        my_name=self.name, other_name=other_pokemon.name, damage=self.level * 2))
                    print("It's super effective")
                    other_pokemon.lose_health(self.level * 2)

# Subclasses of Pokemon


class Charmander(Pokemon):
    def __init__(self, level=5):
        super().__init__("Charmander", "Fire", level)


class Squirtle(Pokemon):
    def __init__(self, level=5):
        super().__init__("Squirtle", "Water", level)


class Bulbasaur(Pokemon):
    def __init__(self, level=5):
        super().__init__("Bulbasaur", "Grass", level)


class Charmeleon(Pokemon):
    def __init__(self, level=5):
        super().__init__("Charmeleon", "Fire", level)


class Wartortle(Pokemon):
    def __init__(self, level=5):
        super().__init__("Wartortle", "Water", level)


class Ivysaur(Pokemon):
    def __init__(self, level=5):
        super().__init__("Ivysaur", "Grass", level)


class Trainer:

    # Pokemon list
    def __init__(self, pokemon_list, num_potions, name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name

    def __repr__(self):

        #    Current active pokemon
        print("The trainer {name} has the following pokemon".format(
            name=self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return "The current active pokemon is {name}\n".format(name=self.pokemons[self.current_pokemon].name)

    def switch_active_pokemon(self, new_active):
        if new_active < len(self.pokemons) and new_active >= 0:
            # You can't switch to a pokemon that is knocked out
            if self.pokemons[new_active].is_knocked_out:
                print("{name} is knocked out. You can't make it your active pokemon".format(
                    name=self.pokemons[new_active].name))
            # You can't switch to your current pokemon
            elif new_active == self.current_pokemon:
                print("{name} is already your active pokemon".format(
                    name=self.pokemons[new_active].name))
            # Switches the pokemon
            else:
                self.current_pokemon = new_active
                print("Go {name}, it's your turn!".format(
                    name=self.pokemons[self.current_pokemon].name))

    def use_potion(self):
        if self.potions > 0:
            print("You used a potion on {name}.".format(
                name=self.pokemons[self.current_pokemon].name))
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else:
            print("You don't have any more potions")

    def attack_other_trainer(self, other_trainer):
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)


# Six pokemon are made

a = Charmander(4)
b = Squirtle()
c = Bulbasaur(10)
d = Wartortle(6)
e = Ivysaur(2)
f = Charmeleon(11)


trainer_one = Trainer([a, b, c], 3, "Tom")
trainer_two = Trainer([d, e, f], 5, "Liza")

print(trainer_one)
print(trainer_two)

# Testing attacking, giving potions, and switching pokemon.

trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)
trainer_two.use_potion()
trainer_one.attack_other_trainer(trainer_two)
trainer_two.switch_active_pokemon(0)
trainer_two.switch_active_pokemon(1)

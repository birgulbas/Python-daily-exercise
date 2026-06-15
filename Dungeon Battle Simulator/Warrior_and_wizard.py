from Hero import *
import random

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, health_level = 150, base_damage = 15)

    def attack(self):
        chance = random.randint(3,30) #savaşçıya özel şans faktörü
        total_damage = super().attack() + chance
        print(f"Warrior {self.name} attack sword!")
        return total_damage


class Wizard(Hero):
    def __init__(self, name):
        super().__init__(name,health_level=150, base_damage = 30)

    def attack(self):
        total_damage = super().attack()
        print(f"Wizard {self.name} threw a ball of fire! ")
        return total_damage

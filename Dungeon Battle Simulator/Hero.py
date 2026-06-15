from Character import *

class Hero(Character):
    def __init__(self, name,health_level, base_damage):
        super().__init__(name,health_level)
        self.base_damage = base_damage
        self.item = None

    def equip(self,new_item):
        self.item = new_item
        print(f"{self.name} {new_item.name} equipped! (+{new_item.power} damage!)")

    def take_damage(self,amount):
        self.health = self.get_health_level()
        new_health = self.health - amount
        self.set_health_level(new_health)
        print(f"{self.name} {amount} take damage! New health: {self.get_health_level()}")

    def attack(self):
        if self.item is not None:
            total_damage = self.base_damage + self.item.power
        else:
            total_damage = self.base_damage
        return total_damage

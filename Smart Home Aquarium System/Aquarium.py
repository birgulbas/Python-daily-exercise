class Aquarium:
    def __init__(self,heater,filter):
        self.heater = heater
        self.filter = filter
        self.fishes = []

    def add_fish(self,fish):
        self.fishes.append(fish)
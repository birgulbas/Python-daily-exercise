class Character:
    def __init__(self, name, health_level):
        self.name = name
        self.__health_level = health_level

    def get_health_level(self):
        return self.__health_level

    def set_health_level(self, new_health):
        if new_health < 0:
            self.__health_level = 0
        else:
            self.__health_level = new_health



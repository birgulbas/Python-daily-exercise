class Fish():
    def __init__(self,name,health):
        self.name = name
        self.__health = health

    def get_health(self):
        return self.__health

    def set_health(self,new_health):
        if new_health > 100  :
            self.__health = 100
            print(f"{self.name} health is full!")

        elif new_health <= 0 :
            self.__health = 0
            print(f"{self.name} is died! ")
        else:
            self.__health = new_health   #normalse yeni sağlık ata


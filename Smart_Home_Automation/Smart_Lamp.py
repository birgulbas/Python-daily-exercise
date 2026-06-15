from Electronic_Device import *

class SmartLamp(ElectronicDevice):
    def __init__(self,brand,status,color= "Yellow"):
        super().__init__(brand,status)
        self.color = color
        self.__brightness = 60 #brightness default startup

    def increase_brightness(self):
        if not self.status:
            print("Lamp is off. Turn on!")
            return

        if  self.__brightness < 100:
            self.__brightness += 10
            print(f"Brightness increased to  {self.__brightness}")
        else:
            print("Maximum brightness !")

    def decrease_brightness(self):
        if not self.status:
            print("Lamp is off. Turn on!")
            return
        if self.__brightness > 0:
            self.__brightness -= 10
            print(f"Brightness decrease to  {self.__brightness}")
        else:
                print("Minimum brightness !")

    def change_color(self,new_color):
        if not self.status:
            print("Lamp is off. Turn on!")
            return
        self.color = new_color
        print(f"Color is changed to {new_color}")

    def get_brightness(self): #getter method
        return self.__brightness

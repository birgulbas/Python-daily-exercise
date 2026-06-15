from Electronic_Device import *

class SmartTv(ElectronicDevice):
    def __init__(self,brand,status,active_channel = "NBR 1"):
        super().__init__(brand,status)
        self.active_channel = active_channel
        self.__volume_level= 50 #Default volume

    def increase_volume(self):
        if not self.status:
            print("Tv is off. Please turn on first.")
            return

        if  self.__volume_level < 100:
            self.__volume_level += 5
            print(f"Volume increased to {self.__volume_level}")
        else:
            print("maximum volume level!")

    def decrease_volume(self):
        if  self.__volume_level > 0:
            self.__volume_level -= 5
            print(f"Volume decreased to {self.__volume_level}")
        else:
            print(" Volume is muted.")

    def change_channel(self,new_channel):
        if not self.status:
            print("Tv is off. Please turn on first.")
            return
        self.active_channel = new_channel
        print(f"Channel changed to: {new_channel}")

    def get_volume_level(self):
        return self.__volume_level





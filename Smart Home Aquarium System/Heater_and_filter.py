from Device import *

class Heater(Device):
    def __init__(self,brand,power_consumption,target_temprature):
        super().__init__(brand,power_consumption)
        self.target_temprature = target_temprature


class Filter(Device):
    def __init__(self,brand,power_consumption,cleaning_capacity):
        super().__init__(brand,power_consumption)
        self.cleaning_capacity = cleaning_capacity


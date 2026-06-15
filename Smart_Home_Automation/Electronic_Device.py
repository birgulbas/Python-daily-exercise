class ElectronicDevice:

    def __init__(self,brand,status = False):
        self.brand = brand
        self.status = status #False: off / True: on

    def turn_on(self):
        self.status = True
        print(f"{self.brand} is turn on.")

    def turn_off(self):
        self.status = False
        print(f"{self.brand} is turn off.")



from Aquarium import *
from Device import *
from Fishes import *
from Heater_and_filter import *


heater1 = Heater("Philips",100, 25)
filter1 = Filter("Tesla",29,234)

#akvaryum oluşturma
my_aquarium = Aquarium(heater1,filter1)
nemo = Fish("Nemo",100)
billy = Fish("Billy",87)

my_aquarium.add_fish(nemo)
my_aquarium.add_fish(billy)

total_watt = my_aquarium.heater.power_consumption + my_aquarium.filter.power_consumption
print("*** Aquarium Otomation System ***")
print("*"*30)
print(f"Aquarium Heater Brand: {my_aquarium.heater.brand}")
print(f"Aquarium Filter Brand: {my_aquarium.filter.brand}")
print(f"Total Fish Count: {len(my_aquarium.fishes)}")
print(f"Total Energy Consumption: {total_watt} Watt")

print("\n***Health Test***")
nemo.set_health(120)

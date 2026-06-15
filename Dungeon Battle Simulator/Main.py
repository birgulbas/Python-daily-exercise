from Hero import *
from Character import *
from Item import *
from Warrior_and_wizard import *


def start_duello(k1,k2):
    print(f"started duello: {k1.name} VS {k2.name}\n")

    while k1.get_health_level()>0 and k2.get_health_level() > 0:  # canları 0 dan büyük oldugu sürece:

        damage1=k1.attack()  # birinci kahraman saldırıyo
        k2.take_damage(damage1)

        if k2.get_health_level()<=0:
            print(f"{k1.name} Wins!")
            break

        print("*"*30)

        damage2=k2.attack()
        k1.take_damage(damage2)

        if k1.get_health_level()<=0:
            print(f"{k2.name} Wins!")
            break

        print("\n"+"="*30+"\n")



arthur=Warrior("Arthur")
merlin=Wizard("Merlin")
sword1=Item("Justice of Sword",22)  # güçlü bir kılıç

arthur.equip(sword1)
print("\n")
start_duello(arthur,merlin)
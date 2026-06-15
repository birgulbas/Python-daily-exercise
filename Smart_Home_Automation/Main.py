from Smart_Television import *
from Smart_Lamp import *


tv = SmartTv("LG",status= False,active_channel = "King tv") #example
lamp = SmartLamp("İkea", status= False, color = "green")#example

while True:
    print("\n")
    print("\n" + "="*30)
    print("Smart Home Automation")
    print("="*30)
    print("1- Smart Tv Menu")
    print("2- Smart Lamp Menu")
    print("q- Quit")
    print("\n")

    choice = input("Please select a device to operate: ")
    print("\n")
    if choice == "1": #Tv menu

        while True:

            current_status = "True" if tv.status else "False"
            print(f"\n*** Smart TV Menu(status: {current_status}) ***")
            print("1. Turn TV On")
            print("2. Turn TV Off")
            print("3. Increase Volume")
            print("4. Decrease Volume")
            print("5. Change Channel")
            print("6. Return to Main Menu")

            tv_choice = input("Enter your choice: ")

            if tv_choice == "1":
                print("\n")
                print("\n" + "-"*30)
                tv.turn_on()

            elif tv_choice == "2":
                print("\n")
                print("\n" + "-"*30)
                tv.turn_off()

            elif tv_choice == "3":
                print("\n")
                print("\n" + "-"*30)
                tv.increase_volume()

            elif tv_choice == "4":
                print("\n")
                print("\n" + "-"*30)
                tv.decrease_volume()

            elif tv_choice == "5":
                print("\n")
                print("\n" + "-"*30)
                new_channel = input("Enter new channel: ")
                tv.change_channel(new_channel)

            elif tv_choice == "6":
                break

            else:
                print("\n")
                print("\n" + "-"*30)
                print("Invalid choice!")


    if choice == "2" : #Lamp menu

        while True:
            print("\n")
            current_status = "True" if lamp.status else "False"
            print(f"\n*** Smart Lamp Menu(status: {current_status}) ***")
            print("1. Turn Lamp On")
            print("2. Turn Lamp Off")
            print("3. Increase Brightness")
            print("4. Decrease Brightness")
            print("5. Change Color")
            print("6. Return to Main Menu")
            print("\n")

            lamp_choice = input("Enter your choice: ")

            if lamp_choice == "1":
                print("\n")
                print("\n" + "-"*30)
                lamp.turn_on()

            elif lamp_choice == "2":
                print("\n")
                print("\n" + "-"*30)
                lamp.turn_off()

            elif lamp_choice == "3":
                print("\n")
                print("\n" + "-"*30)
                lamp.increase_brightness()

            elif lamp_choice == "4":
                print("\n")
                print("\n" + "-"*30)
                lamp.decrease_brightness()

            elif lamp_choice == "5":
                print("\n")
                print("\n" + "-"*30)
                new_color = input("Enter new color: ")
                lamp.change_color(new_color)

            elif lamp_choice == "6":
                break
            else:
                print("\n")
                print("\n" + "-"*30)
                print("Invalid choice!")

    elif choice == "q":
        print("\n")
        print("\n"+"-"*30)
        print ("***Exiting*** \n See you soon bye!")
        break
    else:
        print("\n")
        print("\n"+"-"*30)
        print("Invalid choice!")






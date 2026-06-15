**Smart Home Automation System (OOP Practice)**
A modular, console-based Smart Home Simulation built with Python to practice and demonstrate core Object-Oriented Programming (OOP) concepts.

**Purpose of the Project**
After taking a short break from coding, I developed this project to reinforce my understanding of OOP principles. It simulates a basic smart home setup where a user can interact with different electronic devices through an interactive command-line interface.

**OOP Concepts Applied**
* **Inheritance (Kalıtım):** Created a base class called `ElectronicDevice` that holds common properties (`brand`, `status`) and methods (`turn_on`, `turn_off`). Both `SmartTv` and `SmartLamp` inherit from this class to prevent code duplication.
* **Encapsulation (Kapsülleme):** Restrictive variables like `__volume_level` and `__brightness` are marked as private (using double underscores) so they cannot be accessed or modified directly from outside the class. They are safely manipulated via validation-checked methods and accessed using Getter methods.
* **Abstraction (Soyutlama) & Logic Control:** Real-world logic is applied (e.g., you cannot change channels or adjust brightness if the device is currently turned off).

---
## Project Structure
```text
├── Main.py                  # The interactive user interface and system loop
├── Electronic_Device.py     # Base/Parent class for all devices
├── Smart_Television.py      # Child class inheriting for TV operations
└── Smart_Lamp.py            # Child class inheriting for Lamp operations
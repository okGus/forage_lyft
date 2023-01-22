from abc import ABC
from battery import Battery

class SpindlerBattery(Battery, ABC):
    def __init__(self, battery_percentage):
        super().__init__(battery_percentage)

    def battery_should_be_charged(self):
        return self.battery_percentage < 0.20
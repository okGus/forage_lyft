# Refactored Carrigan
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Carrigan:
    sensors: list[int]

    def tire_should_be_serviced(self):
        """One or more of the values in the tire wear
        array is greater than or equal to 0.9"""
        return True in (el >= 0.9 for el in self.sensors)
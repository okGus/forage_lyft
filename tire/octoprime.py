# Refactored Octoprime
from dataclasses import dataclass

@dataclass
class Octoprime:
    sensors: list[int]

    def tire_should_be_serviced(self):
        """Only when the sum of all values in the tire wear
        is greater than or equal to 3"""
        return sum(self.sensors) >= 3
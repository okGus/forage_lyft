from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, battery_percentage):
        self.battery_percentage = battery_percentage

    @abstractmethod
    def needs_service(self):
        pass

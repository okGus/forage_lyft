# Refactored Calliope Car model
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from batterys.spindler_battery import SpindlerBattery
from dataclasses import dataclass

@dataclass
class Calliope:
    """Model of Car"""
    engine: CapuletEngine
    battery: SpindlerBattery

    def needs_service(self):
        service_threshold_date = self.battery.last_service_date.replace(year=self.battery.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date() or self.engine.engine_should_be_serviced():
            return True
        else:
            return False
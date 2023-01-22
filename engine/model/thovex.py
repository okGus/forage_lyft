# Refactored Thovex Car model
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from batterys.nubbin_battery import NubbinBattery
from dataclasses import dataclass

@dataclass
class Thovex:
    """Model of Car"""
    engine: CapuletEngine
    battery: NubbinBattery

    def needs_service(self) -> bool:
        service_threshold_date = self.battery.last_service_date.replace(year=self.battery.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine.engine_should_be_serviced():
            return True
        else:
            return False
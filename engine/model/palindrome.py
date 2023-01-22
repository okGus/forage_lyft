from datetime import datetime

# Refactored Palindrome Car model
from datetime import datetime
from engine.sternman_engine import SternmanEngine
from batterys.spindler_battery import SpindlerBattery
from dataclasses import dataclass

@dataclass
class Palindrome:
    """Model of Car"""
    engine: SternmanEngine
    battery: SpindlerBattery

    def needs_service(self):
        service_threshold_date = self.battery.last_service_date.replace(year=self.battery.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine.engine_should_be_serviced():
            return True
        else:
            return False
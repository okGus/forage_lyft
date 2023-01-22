# Refactored Rorschach Car model
from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine
from batterys.nubbin_battery import NubbinBattery
from tire.carrigan import Carrigan
from dataclasses import dataclass

@dataclass
class Rorschach:
    """Model of Car"""
    engine: WilloughbyEngine
    battery: NubbinBattery
    tire: Carrigan

    def needs_service(self) -> bool:
        service_threshold_date = self.battery.last_service_date.replace(year=self.battery.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine.engine_should_be_serviced() or self.tire.tire_should_be_serviced():
            return True
        else:
            return False
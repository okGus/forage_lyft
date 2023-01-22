# Refactored SpindlerBattery
from dataclasses import dataclass
from datetime import datetime

@dataclass
class SpindlerBattery:
    last_service_date: datetime
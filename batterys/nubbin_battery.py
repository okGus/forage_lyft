# Refactored NubbinBattery
from dataclasses import dataclass
from datetime import datetime

@dataclass
class NubbinBattery:
    last_service_date: datetime
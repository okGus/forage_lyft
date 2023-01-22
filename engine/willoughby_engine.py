# Refactored WilloughbyEngine
from dataclasses import dataclass

@dataclass
class WilloughbyEngine:
    current_mileage: int
    last_service_mileage: int

    def engine_should_be_serviced(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000
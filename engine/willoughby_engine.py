# Refactored WilloughbyEngine
from dataclasses import dataclass

@dataclass
class WilloughbyEngine:
    current_milage: int
    last_service_milage: int

    def engine_should_be_serviced(self) -> bool:
        return self.current_milage - self.last_service_milage > 60000
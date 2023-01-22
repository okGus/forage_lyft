# Refactored SternmanEngine
from dataclasses import dataclass

@dataclass
class SternmanEngine:
    warning_light_is_on: bool

    def engine_should_be_serviced(self):
        return self.warning_light_is_on
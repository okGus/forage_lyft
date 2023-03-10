import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from batterys.spindler_battery import SpindlerBattery
from batterys.nubbin_battery import NubbinBattery

from tire.carrigan import Carrigan
from tire.octoprime import Octoprime

# Refactored TestCalliope
class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        engine = CapuletEngine(current_mileage=0, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Calliope(engine, battery, tire)
        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        engine = CapuletEngine(current_mileage=0, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Calliope(engine, battery, tire)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()

        engine = CapuletEngine(current_mileage=30001, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Calliope(engine, battery, tire)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        
        engine = CapuletEngine(current_mileage=30000, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Calliope(engine, battery, tire)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        
        engine = CapuletEngine(current_mileage=0, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.9, 0.9, 0.9, 0.4])

        car = Calliope(engine, battery, tire)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        
        engine = CapuletEngine(current_mileage=0, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([1.0, 1.0, 0.0, 0.0])

        car = Calliope(engine, battery, tire)
        self.assertFalse(car.needs_service())

# Refactored TestGlissade
class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        engine = WilloughbyEngine(current_mileage=0, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Glissade(engine, battery, tire)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        engine = WilloughbyEngine(current_mileage=0, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Glissade(engine, battery, tire)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()

        engine = WilloughbyEngine(current_mileage=60001, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Glissade(engine, battery, tire)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()

        engine = WilloughbyEngine(current_mileage=60000, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Glissade(engine, battery, tire)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()

        engine = WilloughbyEngine(current_mileage=0, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.9, 0.9, 0.9, 0.4])

        car = Glissade(engine, battery, tire)
        self.assertTrue(car.needs_service())
    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()

        engine = WilloughbyEngine(current_mileage=0, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([1.0, 1.0, 0.0, 0.0])

        car = Glissade(engine, battery, tire)
        self.assertFalse(car.needs_service())

# Refactored TestPalindrome
class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        engine = SternmanEngine(warning_light_is_on=False)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Palindrome(engine, battery, tire)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        
        engine = SternmanEngine(warning_light_is_on=False)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Palindrome(engine, battery, tire)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        
        engine = SternmanEngine(warning_light_is_on=True)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Palindrome(engine, battery, tire)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        
        engine = SternmanEngine(warning_light_is_on=False)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.0, 0.0, 0.0, 0.0])

        car = Palindrome(engine, battery, tire)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        
        engine = SternmanEngine(warning_light_is_on=False)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([0.9, 0.9, 0.9, 0.4])

        car = Palindrome(engine, battery, tire)
        self.assertTrue(car.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        
        engine = SternmanEngine(warning_light_is_on=False)
        battery = SpindlerBattery(last_service_date)
        tire = Octoprime([1.0, 1.0, 0.0, 0.0])

        car = Palindrome(engine, battery, tire)
        self.assertFalse(car.needs_service())

# Refactored TestRorschach
class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        engine = WilloughbyEngine(current_mileage=0, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 0.0, 0.0, 0.0])
        
        car = Rorschach(engine, battery, tire)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        engine = WilloughbyEngine(current_mileage=0, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 0.0, 0.0, 0.0])
        
        car = Rorschach(engine, battery, tire)
        self.assertFalse(car.needs_service())
    
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()

        engine = WilloughbyEngine(current_mileage=60001, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 0.0, 0.0, 0.0])
        
        car = Rorschach(engine, battery, tire)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()

        engine = WilloughbyEngine(current_mileage=60000, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 0.0, 0.0, 0.0])
        
        car = Rorschach(engine, battery, tire)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()

        engine = WilloughbyEngine(current_mileage=0, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 1.0, 0.0, 0.0])

        car = Rorschach(engine, battery, tire)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()

        engine = WilloughbyEngine(current_mileage=0, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 0.0, 0.0, 0.0])

        car = Rorschach(engine, battery, tire)
        self.assertFalse(car.needs_service())

# Refactored TestRorschach
class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        engine = CapuletEngine(current_mileage=0, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 0.0, 0.0, 0.0])

        car = Thovex(engine, battery, tire)
        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        engine = CapuletEngine(current_mileage=0, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 0.0, 0.0, 0.0])

        car = Thovex(engine, battery, tire)
        self.assertFalse(car.needs_service())
    
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()

        engine = CapuletEngine(current_mileage=30001, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 0.0, 0.0, 0.0])

        car = Thovex(engine, battery, tire)
        self.assertTrue(car.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        
        engine = CapuletEngine(current_mileage=30000, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 0.0, 0.0, 0.0])

        car = Thovex(engine, battery, tire)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        
        engine = CapuletEngine(current_mileage=0, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 1.0, 0.0, 0.0])

        car = Thovex(engine, battery, tire)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        
        engine = CapuletEngine(current_mileage=0, last_service_mileage=0)
        battery = NubbinBattery(last_service_date)
        tire = Carrigan([0.0, 0.0, 0.0, 0.0])

        car = Thovex(engine, battery, tire)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()

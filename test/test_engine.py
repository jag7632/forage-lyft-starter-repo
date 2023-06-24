import unittest
from datetime import datetime

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import sternmanEngine
from engines.willoughby_engine import WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())   

    def test_engine_should_not_be_serviced(self):
        current_mileage = 200
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())   



class TestStrenmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light = True
        engine = sternmanEngine(warning_light)

        self.assertTrue(engine.needs_service())   

    def test_engine_should_not_be_serviced(self):
        warning_light = False
        engine = sternmanEngine(warning_light)

        self.assertFalse(engine.needs_service())   


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())   

    def test_engine_should_not_be_serviced(self):
        current_mileage = 200
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())   
    

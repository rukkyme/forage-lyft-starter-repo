from car import Car
from abc import ABC

class SternmanEngine(Car,ABC):
    def _init__(self, last_service_date, warning_light_is_on):
        """last_service_mileage is set to False because 
        its not applicable to capulet engine
        """
        super().__int__(last_service_date, False, warning_light_is_on)
        self.warning_light_is_on = warning_light_is_on
        
    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
        
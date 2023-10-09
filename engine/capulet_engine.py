
from car import Car
from abc import ABC

class CapuletEngine(Car,ABC):
    def _init__(self, last_service_date, current_mileage, last_service_mileage):
        """warning_light_is_on is set to False because 
        its not applicable to capulet engine
        """
        super().__int__(last_service_date, last_service_mileage, False)
        self.current_mileage = current_mileage
        
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000

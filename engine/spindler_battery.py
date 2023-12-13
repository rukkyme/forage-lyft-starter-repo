from car import Car
from abc import ABC

class SpindlerBattery(Car, ABC):
    def _init__(self, last_service_date, current_date):
        """warning_light_is_on and last_service_mileage is set to False because 
        its not applicable to capulet engine
        """
        super().__int__(last_service_date, False, False)
        self.current_date = current_date
        
    def battery_should_be_serviced(self):
        if self.current_date - self.last_service_date > 3:
            return True
        else:
            return False
        


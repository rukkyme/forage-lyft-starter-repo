from engine.sternman_engine import SternmanEngine
from engine.spindler_battery import SpindlerBattery
from datetime import datetime 

class Palindrome(SternmanEngine, SpindlerBattery):
    def __init__(self, last_service_date, warning_light_is_on, current_date):
        super().__init__(last_service_date, warning_light_is_on, current_date)
    
    def needs_service(self):
        # Calculate the service threshold date for the battery
        battery_service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)

        # Use self.engine_should_be_serviced() to determine if the engine needs service
        engine_needs_service = self.engine_should_be_serviced()

        # Check if either the engine or the battery needs service
        if engine_needs_service or battery_service_threshold_date < datetime.today().date() \
           or self.battery_should_be_serviced():
            return True
        else:
            return False

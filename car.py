
from abc import ABC, abstractmethod

class car(ABC):
    def __init__(self, last_service_date, last_service_mileage, warning_light_is_on):
        self.last_service_date = last_service_date
        self.last_service_mileage = last_service_mileage
        self.warning_light_is_on = warning_light_is_on

    @abstractmethod
    def needs_service(self):
        pass


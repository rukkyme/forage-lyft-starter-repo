from car import Car
from abc import ABC

class CarriganTires(Car, ABC):
    def __int__(self, tire_wear_array):

        super().__init(False, False, False, False, tire_wear_array)
        self.tire_wear_array = tire_wear_array

    def tire_needs_to_be_serviced(self):
        return any(tire_wear >= 0.9 for tire_wear in self.tire_wear_array)

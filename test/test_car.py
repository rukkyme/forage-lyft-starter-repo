import unittest
from datetime import datetime
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def setUp(self):
        # Create a Calliope instance for testing
        self.calliope = Calliope(
            last_service_date=datetime(2021, 1, 1),
            current_mileage=40000,
            current_date=datetime(2023, 10, 9)
        )

    def test_needs_service_engine(self):
        # Test when the engine needs service, but the battery does not
        # Exceeds the 30,000 mileage threshold
        self.calliope.current_mileage = 70000  
        self.assertTrue(self.calliope.needs_service())

    def test_needs_service_battery(self):
        # Test when the battery needs service, but the engine does not
        # Battery service threshold is reached
        self.calliope.last_service_date = datetime(2022, 1, 1)  
        self.assertTrue(self.calliope.needs_service())

    def test_needs_service_both(self):
        # Test when both the engine and battery need service
        self.calliope.current_mileage = 70000
        self.calliope.last_service_date = datetime(2022, 1, 1)
        self.assertTrue(self.calliope.needs_service())

    def test_needs_service_neither(self):
        # Test when neither the engine nor the battery needs service
        self.assertFalse(self.calliope.needs_service())

class TestGlissade(unittest.TestCase):
    def setUp(self):
        # Create a Glissade instance for testing
        self.glissade = Glissade(
            last_service_date=datetime(2021, 1, 1),
            current_mileage=40000,
            current_date=datetime(2023, 10, 9)
        )

    def test_needs_service_engine(self):
        # Test when the engine needs service, but the battery does not
        self.glissade.current_mileage = 70000  # Exceeds the 30,000 mileage threshold
        self.assertTrue(self.glissade.needs_service())

    def test_needs_service_battery(self):
        # Test when the battery needs service, but the engine does not
        self.glissade.last_service_date = datetime(2022, 1, 1)  # Battery service threshold is reached
        self.assertTrue(self.glissade.needs_service())

    def test_needs_service_both(self):
        # Test when both the engine and battery need service
        self.glissade.current_mileage = 70000
        self.glissade.last_service_date = datetime(2022, 1, 1)
        self.assertTrue(self.glissade.needs_service())

    def test_needs_service_neither(self):
        # Test when neither the engine nor the battery needs service
        self.assertFalse(self.glissade.needs_service())

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        # Create a Palindrome instance for testing
        self.palindrome = Palindrome(
            last_service_date=datetime(2021, 1, 1),
            warning_light_is_on=False,  # Assuming the warning light is off
            current_date=datetime(2023, 10, 9)
        )

    def test_needs_service_engine(self):
        # Test when the engine needs service, but the battery does not
        self.palindrome.warning_light_is_on = True  # Simulating the warning light being on
        self.assertTrue(self.palindrome.needs_service())

    def test_needs_service_battery(self):
        # Test when the battery needs service, but the engine does not
        self.palindrome.last_service_date = datetime(2022, 1, 1)  # Battery service threshold is reached
        self.assertTrue(self.palindrome.needs_service())

    def test_needs_service_both(self):
        # Test when both the engine and battery need service
        self.palindrome.warning_light_is_on = True
        self.palindrome.last_service_date = datetime(2022, 1, 1)
        self.assertTrue(self.palindrome.needs_service())

    def test_needs_service_neither(self):
        # Test when neither the engine nor the battery needs service
        self.assertFalse(self.palindrome.needs_service())

class TestRorschach(unittest.TestCase):
    def setUp(self):
        # Create a Rorschach instance for testing
        self.rorschach = Rorschach(
            last_service_date=datetime(2021, 1, 1),
            current_mileage=40000,
            current_date=datetime(2023, 10, 9)
        )

    def test_needs_service_engine(self):
        # Test when the engine needs service, but the battery does not
        self.rorschach.current_mileage = 70000  # Exceeds the 30,000 mileage threshold
        self.assertTrue(self.rorschach.needs_service())

    def test_needs_service_battery(self):
        # Test when the battery needs service, but the engine does not
        self.rorschach.last_service_date = datetime(2022, 1, 1)  # Battery service threshold is reached
        self.assertTrue(self.rorschach.needs_service())

    def test_needs_service_both(self):
        # Test when both the engine and battery need service
        self.rorschach.current_mileage = 70000
        self.rorschach.last_service_date = datetime(2022, 1, 1)
        self.assertTrue(self.rorschach.needs_service())

    def test_needs_service_neither(self):
        # Test when neither the engine nor the battery needs service
        self.assertFalse(self.rorschach.needs_service())


class TestThovex(unittest.TestCase):
    def setUp(self):
        # Create a Thovex instance for testing
        self.thovex = Thovex(
            last_service_date=datetime(2021, 1, 1),
            current_mileage=40000,
            current_date=datetime(2023, 10, 9)
        )

    def test_needs_service_engine(self):
        # Test when the engine needs service, but the battery does not
        self.thovex.current_mileage = 70000  # Exceeds the 30,000 mileage threshold
        self.assertTrue(self.thovex.needs_service())

    def test_needs_service_battery(self):
        # Test when the battery needs service, but the engine does not
        self.thovex.last_service_date = datetime(2022, 1, 1)  # Battery service threshold is reached
        self.assertTrue(self.thovex.needs_service())

    def test_needs_service_both(self):
        # Test when both the engine and battery need service
        self.thovex.current_mileage = 70000
        self.thovex.last_service_date = datetime(2022, 1, 1)
        self.assertTrue(self.thovex.needs_service())

    def test_needs_service_neither(self):
        # Test when neither the engine nor the battery needs service
        self.assertFalse(self.thovex.needs_service())


if __name__ == '__main__':
    unittest.main()

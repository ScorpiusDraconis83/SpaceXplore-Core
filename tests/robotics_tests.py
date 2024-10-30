import unittest
from src.robotics.robotic_probe import RoboticProbe  # Adjust the import based on your actual structure

class TestRoboticProbe(unittest.TestCase):
    def setUp(self):
        self.probe = RoboticProbe(name="Explorer", battery_level=100)

    def test_probe_activation(self):
        self.probe.activate()
        self.assertTrue(self.probe.is_active)

    def test_battery_consumption(self):
        self.probe.consume_battery(20)
        self.assertEqual(self.probe.battery_level, 80)

    def test_battery_overconsumption(self):
        with self.assertRaises(ValueError):
            self.probe.consume_battery(150)

    def test_probe_navigation(self):
        initial_position = self.probe.position
        self.probe.navigate(10, 5)  # Move to (10, 5)
        self.assertEqual(self.probe.position, (10, 5))

if __name__ == "__main__":
    unittest.main()

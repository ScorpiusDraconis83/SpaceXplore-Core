import unittest
from src.propulsion.propulsion_system import PropulsionSystem  # Adjust the import based on your actual structure

class TestPropulsionSystem(unittest.TestCase):
    def setUp(self):
        self.propulsion = PropulsionSystem(thrust=1000, fuel_capacity=5000)

    def test_thrust_output(self):
        self.assertEqual(self.propulsion.get_thrust(), 1000)

    def test_fuel_consumption(self):
        self.propulsion.consume_fuel(100)
        self.assertEqual(self.propulsion.fuel_level, 4900)

    def test_fuel_overconsumption(self):
        with self.assertRaises(ValueError):
            self.propulsion.consume_fuel(6000)

    def test_reach_distance(self):
        distance = self.propulsion.reach_distance(100)  # Assuming 100 seconds of thrust
        self.assertAlmostEqual(distance, 1000, places=1)  # Adjust based on your actual distance calculation

if __name__ == "__main__":
    unittest.main()

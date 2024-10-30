import unittest
from src.communication.laser_comm import LaserCommunication  # Adjust the import based on your actual structure
from src.communication.relay_network import RelayNetwork
from src.communication.error_correction import ErrorCorrection

class TestLaserCommunication(unittest.TestCase):
    def setUp(self):
        self.laser_comm = LaserCommunication(power=150, distance=5000)

    def test_signal_strength(self):
        strength = self.laser_comm.calculate_signal_strength()
        self.assertGreater(strength, 0.1)

    def test_data_transmission(self):
        result = self.laser_comm.transmit_data("Test message")
        self.assertTrue(result)

class TestRelayNetwork(unittest.TestCase):
    def setUp(self):
        self.relay_network = RelayNetwork()
        self.relay_network.add_relay("Relay1")
        self.relay_network.add_relay("Relay2")

    def test_transmit_via_relays(self):
        result = self.relay_network.transmit_via_relays("Test message")
        self.assertTrue(result)

class TestErrorCorrection(unittest.TestCase):
    def setUp(self):
        self.error_correction = ErrorCorrection()

    def test_hamming_code(self):
        encoded = self.error_correction.hamming_code("1011")
        self.assertEqual(encoded.tolist(), [1, 0, 1, 1, 0, 1, 1])  # Adjust based on actual encoding

    def test_error_detection_and_correction(self):
        received_data = [1, 0, 1, 1, 0, 1, 0]  # Simulate an error
        corrected_data = self.error_correction.detect_and_correct(received_data)
        self.assertEqual(corrected_data.tolist(), [1, 0, 1, 1])  # Adjust based on actual correction

if __name__ == "__main__":
    unittest.main()

import logging
import numpy as np

class LaserCommunication:
    def __init__(self, power=100, distance=10000):
        self.power = power  # Power of the laser in watts
        self.distance = distance  # Distance to the receiver in meters
        self.efficiency = 0.9  # Efficiency of the communication system
        logging.basicConfig(level=logging.INFO)

    def calculate_signal_strength(self):
        # Signal strength decreases with distance
        signal_strength = self.power * self.efficiency / (self.distance ** 2)
        logging.info(f"Calculated signal strength: {signal_strength:.2f} W")
        return signal_strength

    def transmit_data(self, data):
        signal_strength = self.calculate_signal_strength()
        if signal_strength > 0.1:  # Threshold for successful transmission
            logging.info(f"Transmitting data: {data}")
            return True
        else:
            logging.error("Transmission failed: Signal too weak.")
            return False

# Example usage
if __name__ == "__main__":
    laser_comm = LaserCommunication(power=150, distance=5000)
    laser_comm.transmit_data("Hello, interstellar world!")

from src.communication.laser_comm import LaserCommunication  # Adjust the import based on your actual structure
from src.communication.relay_network import RelayNetwork
from src.communication.error_correction import ErrorCorrection

def main():
    # Create a laser communication instance
    laser_comm = LaserCommunication(power=150, distance=5000)

    # Calculate signal strength
    signal_strength = laser_comm.calculate_signal_strength()
    print(f"Signal Strength: {signal_strength}")

    # Transmit data
    message = "Hello, World!"
    transmission_result = laser_comm.transmit_data(message)
    print(f"Data transmission successful: {transmission_result}")

    # Create a relay network instance
    relay_network = RelayNetwork()
    relay_network.add_relay("Relay1")
    relay_network.add_relay("Relay2")

    # Transmit data via relays
    relay_result = relay_network.transmit_via_relays(message)
    print(f"Data transmitted via relays: {relay_result}")

    # Error correction example
    error_correction = ErrorCorrection()
    encoded_data = error_correction.hamming_code("1011")
    print(f"Encoded Data: {encoded_data}")

    # Simulate an error in transmission
    received_data = [1, 0, 1, 1, 0, 1, 0]  # Simulated erroneous data
    corrected_data = error_correction.detect_and_correct(received_data)
    print(f"Corrected Data: {corrected_data}")

if __name__ == "__main__":
    main()

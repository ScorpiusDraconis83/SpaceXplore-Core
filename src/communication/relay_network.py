import logging

class RelayNetwork:
    def __init__(self):
        self.relays = []  # List of relay nodes
        logging.basicConfig(level=logging.INFO)

    def add_relay(self, relay_id):
        self.relays.append(relay_id)
        logging.info(f"Relay {relay_id} added to the network.")

    def transmit_via_relays(self, data):
        if not self.relays:
            logging.error("No relays in the network. Transmission failed.")
            return False

        for relay in self.relays:
            logging.info(f"Transmitting data through relay {relay}: {data}")
        logging.info("Data successfully transmitted through all relays.")
        return True

# Example usage
if __name__ == "__main__":
    relay_network = RelayNetwork()
    relay_network.add_relay("Relay1")
    relay_network.add_relay("Relay2")
    relay_network.transmit_via_relays("Hello, interstellar world!")

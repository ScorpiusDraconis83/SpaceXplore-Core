import logging
import numpy as np

class AutonomousNavigation:
    def __init__(self, initial_position=(0, 0), destination=(10, 10)):
        self.position = np.array(initial_position)  # Current position (x, y)
        self.destination = np.array(destination)  # Destination (x, y)
        self.speed = 1.0  # Speed of the probe
        logging.basicConfig(level=logging.INFO)

    def calculate_direction(self):
        direction = self.destination - self.position
        distance = np.linalg.norm(direction)
        if distance == 0:
            logging.warning("Already at the destination.")
            return None
        return direction / distance  # Normalize direction vector

    def move(self):
        direction = self.calculate_direction()
        if direction is not None:
            self.position += direction * self.speed
            logging.info(f"Moved to position: {self.position}")

    def has_reached_destination(self):
        return np.allclose(self.position, self.destination)

    def navigate(self):
        while not self.has_reached_destination():
            self.move()
        logging.info("Destination reached.")

# Example usage
if __name__ == "__main__":
    nav = AutonomousNavigation(initial_position=(0, 0), destination=(5, 5))
    nav.navigate()

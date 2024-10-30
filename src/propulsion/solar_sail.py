import logging

class SolarSail:
    def __init__(self, area=100, reflectivity=0.9):
        self.area = area  # Area of the sail in square meters
        self.reflectivity = reflectivity  # Reflectivity of the sail
        self.is_deployed = False
        logging.basicConfig(level=logging.INFO)

    def deploy(self):
        self.is_deployed = True
        logging.info("Solar Sail deployed.")

    def retract(self):
        self.is_deployed = False
        logging.info("Solar Sail retracted.")

    def calculate_thrust(self, solar_constant=1361):
        if self.is_deployed:
            thrust = (solar_constant * self.area * self.reflectivity) / 299792458  # Thrust calculation
            return thrust
        return 0

    def status(self):
        return {
            "is_deployed": self.is_deployed,
            "thrust": self.calculate_thrust()
        }

    def simulate(self, duration):
        if not self.is_deployed:
            logging.error("Solar Sail is not deployed. Cannot simulate.")
            return
        for t in range(duration):
            logging.info(f"Time: {t}s, Status: {self.status()}")

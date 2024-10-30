import logging

class NuclearThermal:
    def __init__(self, thrust=0, fuel_mass=1000, specific_impulse=900):
        self.thrust = thrust  # Thrust in Newtons
        self.fuel_mass = fuel_mass  # Fuel mass in kg
        self.specific_impulse = specific_impulse  # Specific impulse in seconds
        self.is_active = False
        logging.basicConfig(level=logging.INFO)

    def activate(self):
        if self.fuel_mass <= 0:
            logging.error("Cannot activate Nuclear Thermal: Insufficient fuel.")
            return
        self.is_active = True
        logging.info("Nuclear Thermal Propulsion activated.")

    def deactivate(self):
        self.is_active = False
        logging.info("Nuclear Thermal Propulsion deactivated.")

    def calculate_acceleration(self):
        if self.is_active:
            return self.thrust / self.fuel_mass  # F = ma => a = F/m
        return 0

    def consume_fuel(self, time):
        if not self.is_active:
            logging.warning("Nuclear Thermal is not active. No fuel consumed.")
            return self.fuel_mass

        fuel_consumed = (self.thrust / (self.specific_impulse * 9.81)) * time  # Fuel consumption formula
        self.fuel_mass -= fuel_consumed
        if self.fuel_mass < 0:
            logging.warning("Fuel depleted. Deactivating Nuclear Thermal.")
            self.fuel_mass = 0
            self.deactivate()
        return self.fuel_mass

    def status(self):
        return {
            "is_active": self.is_active,
            "thrust": self.thrust,
            "fuel_mass": self.fuel_mass,
            "acceleration": self.calculate_acceleration()
        }

    def simulate(self, duration):
        if not self.is_active:
            logging.error("Nuclear Thermal is not active. Cannot simulate.")
            return
        for t in range(duration):
            self.consume_fuel(1)  # Simulate fuel consumption per second
            logging.info(f"Time: {t}s, Status: {self.status()}")

# Example usage
if __name__ == "__main__":
    nuclear_thermal = NuclearThermal(thrust=5000, fuel_mass=1000, specific_impulse=900)
    nuclear_thermal.activate()
    nuclear_thermal.simulate(duration=10)
    nuclear_thermal.deactivate()

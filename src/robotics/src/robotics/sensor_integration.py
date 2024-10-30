import logging
import random

class SensorIntegration:
    def __init__(self):
        self.sensors = {
            "temperature": self.read_temperature,
            "humidity": self.read_humidity,
            "pressure": self.read_pressure,
            "biosensor": self.read_biosensor
        }
        logging.basicConfig(level=logging.INFO)

    def read_temperature(self):
        # Simulate reading temperature
        temp = random.uniform(-50, 50)  # Random temperature between -50 and 50 degrees Celsius
        logging.info(f"Temperature: {temp:.2f} °C")
        return temp

    def read_humidity(self):
        # Simulate reading humidity
        humidity = random.uniform(0, 100)  # Random humidity percentage
        logging.info(f"Humidity: {humidity:.2f} %")
        return humidity

    def read_pressure(self):
        # Simulate reading pressure
        pressure = random.uniform(900, 1100)  # Random pressure in hPa
        logging.info(f"Pressure: {pressure:.2f} hPa")
        return pressure

    def read_biosensor(self):
        # Simulate reading biosensor data
        biosignal = random.choice([True, False])  # Randomly simulate biosignature detection
        logging.info(f"Biosignature detected: {biosignal}")
        return biosignal

    def collect_data(self):
        data = {sensor: func() for sensor, func in self.sensors.items()}
        return data

# Example usage
if __name__ == "__main__":
    sensor_integration = SensorIntegration()
    sensor_data = sensor_integration.collect_data()
    logging.info(f"Collected Sensor Data: {sensor_data}")

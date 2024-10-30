from src.robotics.robotic_probe import RoboticProbe  # Adjust the import based on your actual structure

def main():
    # Create a robotic probe instance
    probe = RoboticProbe(name="Explorer", battery_level=100)

    # Activate the probe
    probe.activate()
    print(f"Probe '{probe.name}' activated: {probe.is_active}")

    # Navigate to a new position
    probe.navigate(10, 5)
    print(f"Probe position: {probe.position}")

    # Simulate battery consumption
    probe.consume_battery(20)
    print(f"Battery level after consumption: {probe.battery_level}")

    # Attempt to consume more battery than available
    try:
        probe.consume_battery(150)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

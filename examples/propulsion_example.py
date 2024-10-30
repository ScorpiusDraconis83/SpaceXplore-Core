from src.propulsion.propulsion_system import PropulsionSystem  # Adjust the import based on your actual structure

def main():
    # Create a propulsion system instance
    propulsion = PropulsionSystem(thrust=1000, fuel_capacity=5000)

    # Display initial thrust
    print(f"Initial Thrust: {propulsion.get_thrust()} N")

    # Simulate fuel consumption
    propulsion.consume_fuel(100)
    print(f"Fuel Level after consumption: {propulsion.fuel_level} units")

    # Calculate distance reached
    time = 100  # seconds
    distance = propulsion.reach_distance(time)
    print(f"Distance reached in {time} seconds: {distance} meters")

    # Attempt to consume more fuel than available
    try:
        propulsion.consume_fuel(6000)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

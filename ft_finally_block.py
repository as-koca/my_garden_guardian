#!/usr/bin/env python3

# finally RUNS NO MATTER WHAT! EVEN AFTER return

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name: str = "Unknown") -> None:
        super().__init__(f"Invalid plant name to water: '{name}'")


def water_plant(plant_name: str) -> None:
    check: str = plant_name.capitalize()
    if (check == plant_name):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(plant_name)


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering systems")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering systems\n")
    print("Testing invalid plants")
    print("Opening watering systems")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("carrots")
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering systems\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")

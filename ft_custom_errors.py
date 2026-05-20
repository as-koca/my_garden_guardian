#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name):
        self.msg = f"The {name} plant is wilting!"


class WaterError(GardenError):
    def __init__(self):
        self.msg = "Not enough water in the tank!"


def set_water_level(level: int) -> int:
    if (level < 10):
        raise WaterError
    return (level)


def set_last_in_sun(plant_name, days) -> int:
    if (days > 5):
        raise PlantError(plant_name)
    return days


def ft_custom_errors() -> None:
    print("Testing PlantError...")
    try:
        set_last_in_sun("tomato", 6)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e.msg}")

    print("\nTesting WaterError...")
    try:
        set_water_level(5)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e.msg}")

    print("\nTesting catching all garden errors...")
    try:
        set_last_in_sun("tomato", 6)
        set_water_level(5)
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    ft_custom_errors()
    print("\nAll custom error types work correctly!")

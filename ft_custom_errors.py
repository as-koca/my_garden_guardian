#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name: str = "Unknown") -> None:
        super().__init__(f"The {name} plant is wilting!")


class WaterError(GardenError):
    def __init__(self) -> None:
        super().__init__("Not enough water in the tank!")


def set_water_level(level: int) -> int:
    if (level < 10):
        raise WaterError()
    return (level)


def set_last_in_sun(plant_name: str, days: int) -> int:
    if (days > 5):
        raise PlantError(plant_name)
    return days


def ft_custom_errors() -> None:
    print("Testing PlantError...")
    try:
        set_last_in_sun("tomato", 6)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting WaterError...")
    try:
        set_water_level(5)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting catching all garden errors...")
    try:
        set_last_in_sun("tomato", 6)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        set_water_level(5)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    ft_custom_errors()
    print("\nAll custom error types work correctly!")

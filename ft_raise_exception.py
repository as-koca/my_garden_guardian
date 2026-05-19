#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    try:
        int(temp_str)
        if (int(temp_str) > 40):
            raise ValueError(
                f"{temp_str} is too hot for plants (max 40°C)", 40)
        elif (int(temp_str) < 0):
            raise ValueError(f"{temp_str} is too cold for plants (min 0°C)", 0)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    return (int(temp_str))


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        inp = input_temperature("25")
        print(f"Temperature is now {inp}°C\n")
        print("Input data is 'abc'")
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("\nInput data is '100'")
    inp = input_temperature("100")
    print(f"Temperature is now {inp}°C\n")
    print("Input data is '-50'")
    inp = input_temperature("-50")
    print(f"Temperature is now {inp}°C\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - Program didn't crash!")

#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    inp = int(temp_str)
    if (inp > 40):
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    elif (inp < 0):
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    return (inp)


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        inp = input_temperature("25")
        print(f"Temperature is now {inp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print("Input data is 'abc'")
        input_temperature("abc")
    # ValueError creates its own message
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print("\nInput data is '100'")
        inp = input_temperature("100")
    # ValueError uses whatever message it was given
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print("Input data is '-50'")
        inp = input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("\nAll tests completed - Program didn't crash!")

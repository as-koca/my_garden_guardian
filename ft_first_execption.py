#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
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


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("\nAll tests completed - Program didn't crash!")

#!/usr/bin/env python3

def garden_operation(operation_number) -> None:
    if (operation_number == 0):
        try:
            int("abc")
        except ValueError as e:
            raise ValueError(e)
    elif (operation_number == 1):
        try:
            100 / 0
        except ZeroDivisionError as e:
            raise ZeroDivisionError(e)
    elif (operation_number == 2):
        try:
            open("/non/existent/file")
        except FileNotFoundError as e:
            raise FileNotFoundError(e)
    elif (operation_number == 3):
        try:
            print("should not print" + 1)
        except TypeError as e:
            raise TypeError(e)
    else:
        print("Operation completed succesfully")


def test_error_types() -> None:
    op_num = [0, 1, 2, 3, 4]
    print("=== Garden Error Types Demo ===\n")
    for num in op_num:
        print(f"Testing operation {num}...")
        try:
            garden_operation(num)
        except Exception as e:
            # each classes instance (e) has a "class" and "class.name" attrbute
            print(f"Caught {e.__class__.__name__}: {e}")
    print("\nAll error types tested succesfully!")


if __name__ == "__main__":
    test_error_types()

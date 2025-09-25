import pytest

def test_f_to_c():
    try:
        from Student_code import fahrenheit_to_celsius
        result = fahrenheit_to_celsius(32)
        assert result == 0, print(f"expected result: 0\n result recieved: {result}")
    except SyntaxError as e:
        print(f"error importing fahrenheit_to_celsius: {e}")

def test_c_to_f():
    try:
        from Student_code import celsius_to_fahrenheit
        result = celsius_to_fahrenheit(0)
        assert result == 32, print(f"expected result: 0\n result recieved: {result}")
    except SyntaxError as e:
        print(f"error importing celsius_to_fahrenheit: {e}")

def main():
    test_f_to_c()
    test_f_to_c()
if __name__ == "__main__":
    main()

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def test_celsius_0():
    assert celsius_to_fahrenheit(0) == 32.0


def test_celsius_25():
    assert celsius_to_fahrenheit(25) == 77.0


def test_celsius_100():
    assert celsius_to_fahrenheit(100) == 212.0

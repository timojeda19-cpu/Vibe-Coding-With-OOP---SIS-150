import unittest


class SmartLight:
    def __init__(self, brightness=50):
        self.is_on = False
        self.brightness = brightness

    def turn_on(self):
        self.is_on = True
        print("Light is on")

    def turn_off(self):
        self.is_on = False
        print("Light is off")

    def set_brightness(self, level):
        if not isinstance(level, int) or level < 0 or level > 100:
            raise ValueError("Brightness must be an integer from 0 to 100")
        self.brightness = level
        print(f"Brightness set to {level}")


class TestSmartLight(unittest.TestCase):
    def setUp(self):
        self.light = SmartLight()

    def test_starts_off(self):
        self.assertFalse(self.light.is_on)

    def test_turn_on(self):
        self.light.turn_on()
        self.assertTrue(self.light.is_on)

    def test_turn_off(self):
        self.light.turn_on()
        self.light.turn_off()
        self.assertFalse(self.light.is_on)

    def test_set_brightness(self):
        self.light.set_brightness(75)
        self.assertEqual(self.light.brightness, 75)

    def test_brightness_too_high(self):
        with self.assertRaises(ValueError):
            self.light.set_brightness(150)

    def test_brightness_negative(self):
        with self.assertRaises(ValueError):
            self.light.set_brightness(-5)


if __name__ == "__main__":
    # Create an object to test the class
    light = SmartLight()
    light.turn_on()
    light.set_brightness(80)
    light.turn_off()
    print()

    # Run the unit tests
    unittest.main(argv=["ignored"], exit=False)
import unittest
from Car import Car

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b


class MyTestCase(unittest.TestCase):
    def test_init_default_values(self):
        car = Car()
        self.assertEqual(sum(2,2), 4)
        self.assertEqual(sub(4, 3), 1)
        self.assertEqual(sub(4, 2), 2)
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(car._model, "")


if __name__ == '__main__':
    unittest.main()
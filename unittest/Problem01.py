import unittest

def sum(a, b):
    return a + b

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sum(2,2), 4)


if __name__ == '__main__':
    unittest.main()


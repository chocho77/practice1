import unittest
from Problem10 import Cat

class CatTestCase(unittest.TestCase):
    def test_cat_class(self):
        cat = Cat()
        self.assertEqual(cat._name, "")
        self.assertEqual(cat._age, 0)

       
   

if __name__ == '__main__':
    unittest.main()
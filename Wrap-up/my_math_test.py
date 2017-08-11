import unittest
from my_math import power

class SimplisticTest(unittest.TestCase):

    def test_true(self):
        assert power(3, 2) == 9

    def test_false(self):
        assert not power(3, 3) == 9

if __name__ == '__main__':
    unittest.main()

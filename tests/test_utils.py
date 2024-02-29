
import unittest
from packaging101 import fastfactorial, slowfactorial

print(f"Slow factorial: {slowfactorial(10)}")
print(f"Fast factorial: {fastfactorial(10)}")

class TestFactorials(unittest.TestCase):

    def test_slowfactorial(self):
        result = slowfactorial(10)
        assert result == 3628800
    
    def test_fastfactorial(self):
        result = fastfactorial(10)
        assert result == 3628800

if __name__ == '__main__':
    unittest.main()

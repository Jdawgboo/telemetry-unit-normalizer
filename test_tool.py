import unittest
from tool import convert
class Tests(unittest.TestCase):
 def test_units(self): self.assertEqual(convert(0,'celsius','fahrenheit'),32)
if __name__=='__main__': unittest.main()

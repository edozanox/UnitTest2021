import unittest
from src import roman_numbers

class TestRomanNumbers (unittest.TestCase):

    
    def test_should_return_error_on_invalid_string (self):
        #roman_num = roman_numbers.RomanNumber("XCP")
        #self.assertTrue(False)

        with self.assertRaises(Exception):
            roman_num = roman_numbers.RomanNumber("XVIL")

        #self.assertRaises(Exception, roman_numbers.RomanNumber("XCP"))
        


if __name__ == '__main__':
unittest.main()

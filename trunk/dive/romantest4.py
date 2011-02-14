import unittest, roman4

class ToRomanBadInput(unittest.TestCase):
   def test_too_large(self):
      '''to_roman should fail with larget input'''
      self.assertRaises(roman4.OutOfRangeError, roman4.to_roman, 4000)

   def test_zero(self):
      '''to_roman should fail with 0 input'''
      self.assertRaises(roman4.OutOfRangeError, roman4.to_roman, 0)

   def test_negative(self):
      '''to_roman should fail with negative input'''
      self.assertRaises(roman4.OutOfRangeError, roman4.to_roman, -1)

   def test_non_integer(self):
      '''to_roman should fail with non-integer input'''
      self.assertRaises(roman4.NotIntegerError, roman4.to_roman, 0.5)


if __name__ == '__main__':
   unittest.main()

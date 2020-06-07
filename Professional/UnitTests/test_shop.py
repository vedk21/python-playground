# test file for shop.py

import unittest
import shop

class TestShop(unittest.TestCase):
  def test_add_to_cart_success(self):
    cart = []
    item = (1, 'apples')
    result = shop.add_to_cart(item, cart)
    expected_result = [{'id': 11, 'item': 'apples'}]
    self.assertEqual(result, expected_result)

  def test_add_to_cart_failure(self):
    cart = []
    item = ('or', 'oranges')
    result = shop.add_to_cart(item, cart)
    self.assertIsInstance(result, ValueError)

  def test_add_to_cart_none_type(self):
    cart = []
    item = (None, 'oranges')
    result = shop.add_to_cart(item, cart)
    self.assertEqual(result, 'Invalid item')

if __name__ == '__main__':
  unittest.main()

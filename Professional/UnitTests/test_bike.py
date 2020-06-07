# test file for bike.py

import unittest
import bike

class TestBike(unittest.TestCase):

  def setUp(self):
    print('This will run before every test case') # we can setup some state before running test case here

  def test_bike_success(self):
    '''We can add docs string for our test cases''' # docs string
    action = 'emergency'
    result = bike.drive(action)
    expected_result = 45
    self.assertEqual(result, expected_result)

  def test_bike_failure(self):
    action = 15
    result = bike.drive(action)
    self.assertIsInstance(result, AttributeError)

  def test_bike_none_type(self):
    action = None
    result = bike.drive(action)
    self.assertIsInstance(result, AttributeError)

  def test_bike_not_available_action(self):
    action = 'not available action'
    result = bike.drive(action)
    self.assertEqual(result, 'Invalid Action')

  def tearDown(self):
    print('This will run after every test case') # we can close resources before existing the test case to avoid memory leaks

if __name__ == '__main__':
  unittest.main()

# In order to run all tests from directory, move to that directory and run following command:
# python3 -m unittest -v
# -v -> verbose mode (more details)

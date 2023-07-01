"""
Test select module.
"""


import unittest
import numpy as np

from pinar.util.select import get_attributes_with_matching_dimension

class Dummy():

    def __init__(self):
        self.oneD3 = [1, 2, 3]
        self.oneD4 = [1, 2, 3, 4]
        self.twoD2 = [[1, 2, 3], [1, 2, 3, 4]]
        self.twoD3 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
        self.twoD4 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3 ,4]]
        self.twonp = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])

class TestGetAttributesDimension_pass(unittest.TestCase):
    """Test get_attributes_with_matching_dimension function"""

    def test_select_pass(self):
        """test get_attributes_with_matchin_dimension pass"""

        dummy = Dummy()
        list_attrs = get_attributes_with_matching_dimension(dummy, [3])
        self.assertTrue(np.array_equal(list_attrs, ['oneD3', 'twoD3', 'twonp']))

        list_attrs = get_attributes_with_matching_dimension(dummy, [4, 4])
        self.assertTrue(np.array_equal(list_attrs, ['twoD4']))
        list_attrs = get_attributes_with_matching_dimension(dummy, [3, 4])
        self.assertTrue(np.array_equal(list_attrs, ['twoD3', 'twonp']))

        list_attrs = get_attributes_with_matching_dimension(dummy, [5])
        self.assertTrue(np.array_equal(list_attrs, []))



# Execute Tests
if __name__ == "__main__":
    TESTS = unittest.TestLoader().loadTestsFromTestCase(TestGetAttributesDimension_pass)
    unittest.TextTestRunner(verbosity=2).run(TESTS)

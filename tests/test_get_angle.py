
""""This is test module for the class get_angle.py Angle class"""
from unittest import TestCase
from get_angle import Angle


class TestSum(TestCase):
    """"
    Test case
    """
    def test_sum(self):
        """first store the expected result in a variable"""
        obj = Angle(3, 00)
        result = obj.calculate_angle()
        # check if the result is equal to expected result
        # here the angle should be equal to 90.0.
        self.assertEqual({'response': '90.0'}, result)



# if __name__ == '__main__':
#     unittest.main()

from one_hot_enc import fit_transform
import unittest


class TestOneHotEncoder(unittest.TestCase):
    """Testing function fit_transform() from one_hot_enc.py"""

    def test_args_str(self):
        """Test a function with arguments - strings"""
        actual = fit_transform('Moscow', 'New York', 'Moscow', 'London')
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_args_list_str(self):
        """Test a function with arguments - list of strings"""
        actual = fit_transform(['Moscow', 'Moscow', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 1]),
            ('Moscow', [0, 1]),
            ('Moscow', [0, 1]),
            ('London', [1, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_args_list_int(self):
        """Test a function with arguments - list of integers"""
        actual = fit_transform([1, 2, 2, 3])
        expected = [
            (1, [0, 0, 1]),
            (2, [0, 1, 0]),
            (2, [0, 1, 0]),
            (3, [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_args_list_float(self):
        """Test a function with arguments - list of floats"""
        actual = fit_transform([1.5, 2.9, 3.4, 1.5])
        expected = [
            (1.5, [0, 0, 1]),
            (2.9, [0, 1, 0]),
            (3.4, [1, 0, 0]),
            (1.5, [0, 0, 1]),
        ]
        self.assertEqual(actual, expected)

    def test_args_empty(self):
        """Test a function with empty arguments"""
        with self.assertRaises(TypeError):
            fit_transform()

    def test_contains(self):
        """
        Test for a function where it is checked that the element
        is not in 'fit_transform'
        """
        actual = fit_transform([1, 2, 3, 4, 4])
        self.assertNotIn((2, [0, 1, 0, 0]), actual)

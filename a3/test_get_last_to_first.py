"""A3. Test cases for function club_functions.get_last_to_first.
"""

import unittest
import club_functions


class TestGetLastToFirst(unittest.TestCase):
    """Test cases for function club_functions.get_last_to_first.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_last_to_first(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_02_one_person_no_friend_same_last(self):
        param = {'Clare Dunphy': []}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_03_two_person_no_friend_same_last(self):
        param = {'Clare Dunphy': [], 'Stephanie Tanner': []}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Tanner': ['Stephanie']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_04_two_person_one_friend_same_last(self):
        param = {'Clare Dunphy': [], 'Stephanie Tanner': ['Michelle Tanner']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Tanner':['Michelle', 'Stephanie']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_05_two_person_two_friend_same_last(self):
        param = {'Clare Dunphy': ['Luke Dunphy'], 'Stephanie Tanner': ['Michelle Tanner']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Luke'], 'Tanner': ['Michelle', 'Stephanie']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_06_one_person_one_friend_same_last_space_in_name(self):
        param = {'Clare Dunphy': ['Phil Mike Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil Mike']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_07_one_person_no_friend_same_last_space_in_name(self):
        param = {'Clare Madison Dunphy': []}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare Madison']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_08_two_person_no_friend_same_last_space_in_name(self):
        param = {'Clare Madison Dunphy': [], 'Stephanie J Tanner': []}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare Madison'], 'Tanner': ['Stephanie J']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_09_two_person_one_friend_same_last_space_in_name(self):
        param = {'Clare Madison Dunphy': [], 'Stephanie J Tanner': ['Michelle Tanner']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare Madison'], 'Tanner':['Michelle', 'Stephanie J']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_10_two_person_two_friend_same_last_space_in_name(self):
        param = {'Clare Madison Dunphy': ['Luke Dunphy'], 'Stephanie J Tanner': ['Michelle Tanner']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare Madison', 'Luke'], 'Tanner':['Michelle', 'Stephanie J']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

if __name__ == '__main__':
    unittest.main(exit=False)

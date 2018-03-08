# -*- coding: utf-8 -*-
import unittest


class testAddition(unittest.TestCase):
    def setUp(self):
        print('Setting up the test.')

    def tearDown(self):
        print('Tearing down the test.')

    def test_twoplustwo(self):
        count = 2 + 2
        self.assertEqual(4, count)


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map
"""
import unittest
from parameterized import parameterized, parameterized_class
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    TestCase class that will hold
    the test methods
    """
    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, mapp, path, expected):
        """Tests for the return of utils.access_nested_map"""
        self.assertEqual(access_nested_map(mapp, path), expected)

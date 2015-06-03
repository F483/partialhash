#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals
import json
import unittest
import partialhash


fixtures = json.load(open("tests/fixtures.json"))


class TestPartialHash(unittest.TestCase):

    def test_fullfile(self):
        path = fixtures["full"]["path"]
        expected = fixtures["full"]["sha256"]
        digest = partialhash(path)
        self.assertEqual(digest, expected)

    def test_offset(self):
        path = fixtures["offset"]["path"]
        offset = fixtures["offset"]["offset"]
        expected = fixtures["offset"]["sha256"]
        digest = partialhash(path, offset=offset)
        self.assertEqual(digest, expected)

    def test_length(self):
        path = fixtures["length"]["path"]
        length = fixtures["length"]["length"]
        expected = fixtures["length"]["sha256"]
        digest = partialhash(path, length=length)
        self.assertEqual(digest, expected)

    def test_bounds_exceeded(self):
        def callback():
            path = fixtures["bounds_exceeded"]["path"]
            length = fixtures["bounds_exceeded"]["length"]
            partialhash(path, length=length)
        self.assertRaises(partialhash.BoundsError, callback)

    def test_negative_length(self):
        def callback():
            path = fixtures["negative_length"]["path"]
            length = fixtures["negative_length"]["length"]
            partialhash(path, length=length)
        self.assertRaises(partialhash.BoundsError, callback)

    def test_negative_offset(self):
        def callback():
            path = fixtures["negative_offset"]["path"]
            offset = fixtures["negative_offset"]["offset"]
            partialhash(path, offset=offset)
        self.assertRaises(partialhash.BoundsError, callback)

    def test_offset_length(self):
        path = fixtures["offset_length"]["path"]
        length = fixtures["offset_length"]["length"]
        offset = fixtures["offset_length"]["offset"]
        expected = fixtures["offset_length"]["sha256"]
        digest = partialhash(path, length=length, offset=offset)
        self.assertEqual(digest, expected)


if __name__ == '__main__':
    unittest.main()

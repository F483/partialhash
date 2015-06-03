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


class TestHash(unittest.TestCase):

    def test_negative_offset(self):
        def callback():
            path = fixtures["negative_offset"]["path"]
            offset = fixtures["negative_offset"]["offset"]
            partialhash.compute(path, offset=offset)
        self.assertRaises(partialhash.BoundsError, callback)

    def test_negative_length(self):
        def callback():
            path = fixtures["negative_length"]["path"]
            length = fixtures["negative_length"]["length"]
            partialhash.compute(path, length=length)
        self.assertRaises(partialhash.BoundsError, callback)

    def test_bounds(self):
        def callback():
            path = fixtures["bounds"]["path"]
            length = fixtures["bounds"]["length"]
            partialhash.compute(path, length=length)
        self.assertRaises(partialhash.BoundsError, callback)

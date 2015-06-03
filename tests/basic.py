#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals
import binascii
import json
import unittest
import partialhash


fixtures = json.load(open("tests/fixtures.json"))


def h2b(h):
    return binascii.unhexlify(h.encode("ascii"))


class TestHash(unittest.TestCase):

    def test_full(self):
        path = fixtures["full"]["path"]
        expected = h2b(fixtures["full"]["sha256"])
        digest = partialhash.sum(path)
        self.assertEqual(digest, expected)

    def test_partial(self):
        path = fixtures["partial"]["path"]
        length = fixtures["partial"]["length"]
        offset = fixtures["partial"]["offset"]
        expected = h2b(fixtures["partial"]["sha256"])
        digest = partialhash.sum(path, length=length, offset=offset)
        self.assertEqual(digest, expected)

    def test_bounds(self):
        def callback():
            path = fixtures["bounds"]["path"]
            length = fixtures["bounds"]["length"]
            partialhash.sum(path, length=length)
        self.assertRaises(partialhash.BoundsError, callback)


class TestLength(unittest.TestCase):

    def test_length(self):
        path = fixtures["length"]["path"]
        length = fixtures["length"]["length"]
        expected = h2b(fixtures["length"]["sha256"])
        digest = partialhash.sum(path, length=length)
        self.assertEqual(digest, expected)

    def test_negative_length(self):
        def callback():
            path = fixtures["negative_length"]["path"]
            length = fixtures["negative_length"]["length"]
            partialhash.sum(path, length=length)
        self.assertRaises(partialhash.BoundsError, callback)


class TestOffset(unittest.TestCase):

    def test_offset(self):
        path = fixtures["offset"]["path"]
        offset = fixtures["offset"]["offset"]
        expected = h2b(fixtures["offset"]["sha256"])
        digest = partialhash.sum(path, offset=offset)
        self.assertEqual(digest, expected)

    def test_negative_offset(self):
        def callback():
            path = fixtures["negative_offset"]["path"]
            offset = fixtures["negative_offset"]["offset"]
            partialhash.sum(path, offset=offset)
        self.assertRaises(partialhash.BoundsError, callback)


class TestSeed(unittest.TestCase):

    def test_seed(self):
        seed_path = fixtures["seed"]["seed_path"]
        file_path = fixtures["seed"]["file_path"]
        expected = h2b(fixtures["seed"]["sha256"])
        with open(seed_path, 'rb') as seed:
            digest = partialhash.sum(file_path, seed=seed.read())
            self.assertEqual(digest, expected)


class TestScatter(unittest.TestCase):

    def test_scatter(self):
        path = fixtures["scatter"]["path"]
        length = fixtures["scatter"]["length"]
        offset = fixtures["scatter"]["offset"]
        partialhash.sum(path, length=length, offset=offset, scatter=4)
        # FIXME how to test correctness?


if __name__ == '__main__':
    unittest.main()
